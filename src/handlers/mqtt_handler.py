import json
import logging
import paho.mqtt.client as mqtt
import time

logging.basicConfig(level=logging.INFO)

class MqttHandler:
    def __init__(self, broker: str, options: dict = None):
        self.broker = broker
        self.options = options or {}
        self.client = None
        self.node_id = None

    def connect(self, node_id: str, retries: int = 3, delay: int = 5):
        """Connect to MQTT broker with retry logic."""
        self.node_id = node_id
        self.client = mqtt.Client(client_id=node_id)

        # Apply options (username/password, TLS, etc.)
        if "username" in self.options and "password" in self.options:
            self.client.username_pw_set(
                self.options["username"], self.options["password"]
            )
        if "tls" in self.options:
            self.client.tls_set(**self.options["tls"])

        # Event handlers
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect

        # Retry loop
        for attempt in range(1, retries + 1):
            try:
                self.client.connect(self.broker)
                self.client.loop_start()
                return
            except Exception as e:
                logging.error(f"[MQTT] Connect attempt {attempt} failed: {e}")
                time.sleep(delay)
        raise ConnectionError(f"Failed to connect to MQTT broker {self.broker}")

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logging.info(f"[MQTT] Connected to {self.broker}")
            # Subscriptions
            self.subscribe("meshcore/test", qos=1)
            self.subscribe("meshcore/ingest", qos=1)
            self.subscribe(f"meshcore/{self.node_id}/downlink", qos=1)
            self.subscribe("meshcore/*/uplink", qos=1)

            # Test publish
            self.publish("meshcore/test", "Hello MeshCore!", qos=1)
        else:
            logging.error(f"[MQTT] Connection failed with code {rc}")

    def _on_disconnect(self, client, userdata, rc):
        logging.warning("[MQTT] Connection closed")

    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        parts = topic.split("/")
        node_id = parts[1] if len(parts) > 2 else None

        try:
            payload = json.loads(msg.payload.decode("utf-8"))
        except Exception:
            payload = msg.payload.decode("utf-8")

        if topic.endswith("/uplink") and node_id:
            logging.info(f"[MQTT] Uplink from {node_id}: {payload}")
            # TODO: process uplink payload (store, forward, etc.)
        elif topic.endswith("/downlink") and node_id:
            logging.info(f"[MQTT] Downlink for {node_id}: {payload}")
            # TODO: forward payload into MeshCore
        else:
            logging.info(f"[MQTT] Other message: {topic} {payload}")

    def disconnect(self):
        if self.client:
            self.client.loop_stop()
            self.client.disconnect()
            logging.info("[MQTT] Disconnected")

    def subscribe(self, topic: str, qos: int = 0):
        if self.client:
            result, mid = self.client.subscribe(topic, qos=qos)
            if result == mqtt.MQTT_ERR_SUCCESS:
                logging.info(f"[MQTT] Subscribed to {topic} id {mid}")
            else:
                logging.error(f"[MQTT] Subscribe error: {result}")

    def publish(self, topic: str, payload, qos: int = 0, retain: bool = False):
        if self.client:
            result, mid = self.client.publish(topic, payload, qos=qos, retain=retain)
            if result == mqtt.MQTT_ERR_SUCCESS:
                logging.info(f"[MQTT] Published to {topic}: {payload} id {mid}")
            else:
                logging.error(f"[MQTT] Publish error: {result}")

    def set_on_message(self, callback):
        if self.client:
            self.client.on_message = callback

    def set_on_connect(self, callback):
        if self.client:
            self.client.on_connect = callback

    def set_on_disconnect(self, callback):
        if self.client:
            self.client.on_disconnect = callback

    def shutdown(self):
        """Gracefully stop MQTT loop and disconnect client."""
        logging.info("[MQTT] Shutting down...")
        try:
            if self.client:
                self.client.loop_stop()
                self.client.disconnect()
                logging.info("[MQTT] Client disconnected.")
        except Exception as e:
            logging.error(f"[MQTT] Error during shutdown: {e}")
        finally:
            self.client = None
        logging.info("[MQTT] Shutdown complete.")
