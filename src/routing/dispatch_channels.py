# src/routing/dispatch_channels.py

import json
from src.utils import get_text_from_key, hash_public_key, get_public_key_value
from src.db.insert_handlers import InsertHandlers


class DispatchChannels:
    def handle_ChannelInfo(self, packet: dict):
        outer_data = packet["data"]
        data = outer_data["data"]
        meta = outer_data["meta"]
        channel_idx, name, secret = data["channelIdx"], data["name"], data["secret"]
        print(".../ChannelInfo", channel_idx, name, secret)

        shaped = {
            "channelIdx": channel_idx,
            "channelNum": channel_idx,
            "nodeNum": hash_public_key(secret),
            "protocol": "meshcore",
            "name": name,
            "role": None,
            "psk": get_text_from_key(secret),
            "options": json.dumps({}),
            **meta,
        }

        if name and name.strip() and get_public_key_value(secret):
            InsertHandlers.insertChannel(shaped)

    def handle_channel(self, sub_packet: dict):
        data, meta = sub_packet["data"], sub_packet["meta"]
        channel = data.get("channel", {})
        settings = channel.get("settings", {})

        channel_num = settings.get("channelNum", 0)
        name = settings.get("name", "default")
        psk = settings.get("psk")
        uplink_enabled = settings.get("uplinkEnabled")
        downlink_enabled = settings.get("downlinkEnabled")
        module_settings = settings.get("moduleSettings")

        if channel.get("role"):
            InsertHandlers.insertChannel({
                "channelNum": channel_num,
                "channelIdx": channel.get("index", 0),
                "nodeNum": meta["fromNodeNum"],
                "protocol": 0,
                "name": name,
                "role": channel["role"],
                "psk": psk,
                "options": {
                    "moduleSettings": json.dumps(module_settings) if module_settings else None,
                    "uplinkEnabled": uplink_enabled,
                    "downlinkEnabled": downlink_enabled,
                },
                "connId": meta["connId"],
                "timestamp": meta["timestamp"],
            })
