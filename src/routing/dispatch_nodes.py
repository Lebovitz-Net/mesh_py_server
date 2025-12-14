# src/routing/dispatch_nodes.py

import json
from src.utils import get_text_from_key, hash_public_key, get_public_key_value
from src.db.insert_handlers import InsertHandlers
from src.meshcore.utils.string_utils import decode_node_info

# Convenience alias
insert_my_info = InsertHandlers.insertMyInfo


class DispatchNodes:
    def handle_SelfInfo(self, packet: dict):
        print(".../dispatchNodes SelfInfo")
        outer_data = packet["data"]
        data = outer_data["data"]
        meta = outer_data["meta"]

        shaped = {
            "id": data["name"],
            "myNodeNum": hash_public_key(data["publicKey"]),
            "type": data["type"],
            "name": data["name"],
            "publicKey": get_text_from_key(data["publicKey"]),
            "options": json.dumps({
                "txPower": data["txPower"],
                "maxTxPower": data["maxTxPower"],
                "advLat": data["advLat"],
                "advLon": data["advLon"],
                "reserved": data["reserved"].hex(),
                "manualAddContacts": data["manualAddContacts"],
                "radioFreq": data["radioFreq"],
                "radioBw": data["radioBw"],
                "radioSf": data["radioSf"],
                "radioCr": data["radioCr"],
            }),
            "protocol": "meshcore",
            **meta,
        }
        insert_my_info(shaped)

    def handle_Ok(self, packet: dict):
        print(".../dispatchNodes Ok")

    def handle_ContactMsgResponse(self, packet: dict):
        outer_data = packet["data"]
        data = outer_data["data"]
        meta = outer_data["meta"]
        d = data
        shaped = {
            "contactId": d["advName"],
            "nodeNum": hash_public_key(d["publicKey"]),
            "type": d.get("type"),
            "name": d["advName"],
            "shortName": None,
            "publicKey": d["publicKey"],
            "times": json.dumps({
                "lastAdvert": d["lastAdvert"],
                "lastMod": d.get("lastMod")
            }),
            "position": json.dumps({
                "advlat": d["advlat"],
                "advlon": d["advlon"]
            }),
            "path": json.dumps({
                "outPath": d["outPath"],
                "outPathLen": d["outPathLen"]
            }),
            "options": json.dumps({"flags": d["flags"]}),
            **meta,
        }
        # TODO: InsertHandlers.insertUser(shaped)

    def handle_MyNodeInfo(self, sub_packet: dict):
        print(".../dispatchNodes MyNodeInfo")

    def handle_myInfo(self, sub_packet: dict):
        data, conn_id, timestamp, meta = (
            sub_packet["data"],
            sub_packet["connId"],
            sub_packet.get("timestamp"),
            sub_packet["meta"],
        )
        my_info = data["myInfo"]
        print(".../dispatchNodes myInfo")

        InsertHandlers.insertMyInfo({
            **my_info,
            "connId": conn_id,
            "currentIP": meta["sourceIp"],
            "timestamp": timestamp or meta["timestamp"],
        })

    def handle_NodeFilter(self, sub_packet: dict):
        data, meta = sub_packet["data"], sub_packet["meta"]
        print("[dispatchNodes] NodeFilter", sub_packet,
              decode_node_info(data["nodeName"]))

    def handle_NodeHighlight(self, sub_packet: dict):
        print("[dispatchNodes] NodeHighlight", sub_packet)

    def handle_NodeInfo(self, sub_packet: dict):
        print("[dispatchNodes] NodeInfo", sub_packet)

    def handle_nodeInfo(self, sub_packet: dict):
        data, meta = sub_packet["data"], sub_packet["meta"]
        num = data["num"]
        # TODO: shape nodeInfo, user, metrics, position
        print("[dispatchNodes] nodeInfo detailed")

    def handle_position(self, sub_packet: dict):
        data, meta = sub_packet["data"], sub_packet["meta"]
        pos = data["position"]

        InsertHandlers.insertPosition({
            "fromNodeNum": data["fromNodeNum"],
            "toNodeNum": data["toNodeNum"],
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "altitude": data.get("altitude"),
            "sats_in_view": data.get("satsInView"),
            "batteryLevel": data.get("batteryLevel"),
            "device_id": meta["device_id"],
            "conn_id": meta["connId"],
            "timestamp": meta["timestamp"],
        })

    def handle_Waypoint(self, sub_packet: dict):
        print("[dispatchNodes] Waypoint", sub_packet)

    def handle_User(self, sub_packet: dict):
        print("[dispatchNodes] User", sub_packet)

    def handle_Position(self, packet: dict):
        print("[dispatchNodes] Position", packet)
