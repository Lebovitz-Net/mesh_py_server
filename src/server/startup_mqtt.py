# startup_mqtt.py
import asyncio
import logging
import socket

from src.config.config import config   # ✅ direct import
from src.handlers.mqtt_handler import MqttHandler   # import the handler we built

class MQTTStartupError(Exception):
    """Raised when MQTT client fails to start/connect gracefully."""


async def start_mqtt_server(connect_timeout: float = 10.0) -> MqttHandler:
    """
    Async start of MQTT bridge client using MqttHandler.
    Validates broker host/port, instantiates handler, connects.
    """

    broker_host = str(config["mqtt"].get("brokerHost", "")).strip()
    broker_port = config["mqtt"].get("brokerPort", 1883)
    broker_url  = config["mqtt"].get("brokerUrl", f"{broker_host}:{broker_port}")
    node_id     = config["mqtt"].get("nodeId", "meshcore-node")

    if not broker_host or not isinstance(broker_port, int):
        msg = f"[MQTT] Invalid configuration: host={broker_host!r} port={broker_port!r}"
        logging.error(msg)
        raise MQTTStartupError(msg)

    # DNS pre-check
    try:
        socket.getaddrinfo(broker_host, broker_port)
    except socket.gaierror as e:
        msg = f"[MQTT] DNS resolution failed for host '{broker_host}': {e}"
        logging.error(msg)
        raise MQTTStartupError(msg)

    logging.info(f"[MQTT] Connecting to {broker_url} as node {node_id}")

    handler = MqttHandler(broker=broker_host, options=config.get("mqttOptions", {}))

    try:
        # run connect in a thread to avoid blocking asyncio loop
        await asyncio.to_thread(handler.connect, node_id)
    except Exception as e:
        msg = f"[MQTT] Connection failed: {e}"
        logging.error(msg)
        raise MQTTStartupError(msg)

    logging.info("[MQTT] Handler started successfully")
    return handler


async def shutdown_mqtt_server(handler: MqttHandler) -> None:
    """Async, graceful shutdown of the MQTT handler."""
    logging.info("[MQTT] Shutting down...")
    if not handler:
        logging.info("[MQTT] No handler to shut down.")
        return
    try:
        await asyncio.to_thread(handler.shutdown)
        logging.info("[MQTT] Handler disconnected.")
    except Exception as e:
        logging.error(f"[MQTT] Error during shutdown: {e}")
    finally:
        logging.info("[MQTT] Shutdown complete.")
