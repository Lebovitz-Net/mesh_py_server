# src/routing/dispatch_configs.py

import json
from .dispatch_utils import normalize_packet
from ..db.insert_handlers import InsertHandlers


class DispatchConfigs:
    def handle_DeviceInfo(self, packet: dict):
        norm_packet = normalize_packet(packet)
        data, meta = norm_packet["data"], norm_packet["meta"]
        print(".../dispatchConfigs DeviceInfo")

    def handle_Err(self, packet: dict):
        norm_packet = normalize_packet(packet)
        data, meta = norm_packet["data"], norm_packet["meta"]
        print(".../dispatchConfigs Err")

    def handle_config(self, sub_packet: dict):
        meta, data = sub_packet["meta"], sub_packet["data"]
        config = data.get("config", {})
        if data and len(data.keys()):
            key, value = list(config.items())[0]
            InsertHandlers.insertConfig({
                "fromNodeNum": meta["fromNodeNum"],
                "key": key,
                "data": json.dumps(value),
                "timestamp": meta["fromNodeNum"],
                "device_id": meta["device_id"],
                "connId": meta["connId"],
            })

    def handle_device(self, sub_packet: dict):
        print("[dispatchConfig] device")

    def handle_security(self, sub_packet: dict):
        print("[dispatchConfig] security")

    def handle_moduleConfig(self, packet: dict):
        norm_packet = normalize_packet(packet)
        data, meta = norm_packet["data"], norm_packet["meta"]

        config = data.get("moduleConfig", {})
        if not config:
            return
        key, value = list(config.items())[0]
        if not value or len(value.keys()) == 0:
            return

        InsertHandlers.insertModuleConfig({
            "fromNodeNum": meta["fromNodeNum"],
            "key": key,
            "data": json.dumps(value),
            "timestamp": meta["fromNodeNum"],
            "device_id": meta["device_id"],
            "connId": meta["connId"],
        })

    def handle_DeviceUIConfig(self, sub_packet: dict):
        print("[dispatchConfig] Ignoring DeviceUIConfig")

    def handle_deviceuiConfig(self, sub_packet: dict):
        print("[dispatchConfig] Ignoring deviceuiConfig")

    def handle_adminMessage(self, sub_packet: dict):
        print("[dispatchConfig] Ignoring AdminMessage")

    def handle_routingMessage(self, sub_packet: dict):
        print("[dispatchConfig] Ignoring Routing")

    def handle_RouteDiscovery(self, sub_packet: dict):
        print("[dispatchConfig] RouteDiscovery")

    def handle_Routing(self, sub_packet: dict):
        print("[dispatchConfig] Routing")

    def handle_metadata(self, packet: dict):
        norm_packet = normalize_packet(packet)
        data, meta = norm_packet["data"], norm_packet["meta"]

        metadata = data.get("metadata", {})
        if not metadata or len(metadata.keys()) == 0:
            print("[dispatchRegistry] metadata object is empty", metadata)
            return

        InsertHandlers.insertMetadata({
            **metadata,
            "canShutdown": 1 if metadata.get("canShutdown") else 0,
            "hasWifi": 1 if metadata.get("hasWifi") else 0,
            "hasBluetooth": 1 if metadata.get("hasBluetooth") else 0,
            "hasPKC": 1 if metadata.get("hasPKC") else 0,
            "num": meta["fromNodeNum"],
        })

    def handle_DeviceMetadata(self, sub_packet: dict):
        print("[dispatchConfig] ... DeviceMetadata", sub_packet)

    def handle_fileInfo(self, sub_packet: dict):
        data, meta = sub_packet["data"], sub_packet["meta"]
        file_info = data.get("fileInfo", {})
        InsertHandlers.insertFileInfo({
            "filename": file_info.get("fileName"),
            "size": file_info.get("sizeBytes"),
            "mime_type": file_info.get("mime_type"),
            "description": file_info.get("description"),
            "fromNodeNum": meta["fromNodeNum"],
            "device_id": meta["device_id"],
            "connId": meta["connId"],
            "timestamp": meta["timestamp"],
        })

    def handle_mqttClientProxyMessage(self, sub_packet: dict):
        # placeholder
        pass

    def handle_KeyVerification(self, sub_packet: dict):
        print("[dispatchConfigs] KeyVerification")

    def handle_keyVerificationNumberRequest(self, sub_packet: dict):
        print("[dispatchConfig] keyVerificationNumberRequest")

    def handle_configCompleteId(self, sub_packet: dict):
        print("[dispatchConfig] configComplete", sub_packet)
