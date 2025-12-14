# src/routing/dispatch_mqtt.py

from src.db.insert_handlers import InsertHandlers
from src.meshcore.utils.string_utils import decode_python_string


class DispatchMqtt:
    def handle_mqtt(self, sub_packet: dict):
        print("[dispatchMqtt] mqtt", sub_packet)

        # Example extension:
        # data, meta = sub_packet.get("data"), sub_packet.get("meta")
        # decoded = decode_python_string(data.get("payload", ""))
        # InsertHandlers.insertMqttMessage({"payload": decoded, **meta})
        # self.emit("mqtt", sub_packet)        # if using EventEmitter
        # self.overlay.emit("mqttReceived", sub_packet)  # if using OverlayEmitter
