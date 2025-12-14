# src/routing/dispatch_messages.py

import json
import asyncio
from ..utils import get_text_from_key, hash_public_key, get_public_key_value, normalize_in
from ..db.insert_handlers import InsertHandlers
from ..meshcore.meshcore_requests import MeshcoreRequests
from ..api.api_utils import generate_message_id, extract_sender_and_mentions
from ..meshcore.utils.string_utils import decode_node_info
from .dispatch_utils import normalize_packet

insert_message = InsertHandlers.insertMessage


class DispatchMessages:
    def handle_Sent(self, packet: dict):
        print(".../dispatchMessages sent", packet)

    def handle_MsgWaiting(self, packet: dict):
        print(".../dispatchMessages MsgWaiting")
        request = MeshcoreRequests.get_instance()
        asyncio.create_task(request.get_waiting_messages())

    def handle_Advert(self, packet: dict):
        key = packet.get("data", {}).get("data", {}).get("publicKey")
        print(".../dispatchMessages Advert key is", get_text_from_key(key))

    def handle_ChannelMsgRecv(self, packet: dict):
        outer_data = normalize_packet(packet)
        data,  meta = outer_data["data"], outer_data["meta"]
        text, txt_type, path_len = data["text"], data["txtType"], data["pathLen"]
        channelId = data.get("channelIdx", 0)
        sender, mentions = extract_sender_and_mentions(text)

        if sender is None:
            print("[dispatchMessage] skipping Message cannot extract sender", packet)
            return

        print(f".../dispatchMessages Channel {channelId} Message is", text)

        shaped = {
            "contactId": sender,
            "messageId": generate_message_id(packet),
            "channelId": data.get("channelIdx", "default"),
            "fromNodeNum": data.get("from", 0),
            "toNodeNum": data.get("to"),
            "message": text,
            "recvTimestamp": meta["timestamp"],
            "sentTimestamp": normalize_in(data["senderTimestamp"]),
            "protocol": "meshcore",
            "sender": sender,
            "mentions": json.dumps(mentions),
            "options": json.dumps({"txtType": txt_type, "pathLen": path_len}),
        }

        insert_message(shaped)

    def handle_NoMoreMessages(self, packet: dict):
        print(".../dispatchMessages NoMoreMessages")

    def handle_ContactMsgReceived(self, packet: dict):
        print(".../dispatchMessages ContactMsgRev", packet)

    def handle_message(self, sub_packet: dict):
        packet, meta = sub_packet["packet"], sub_packet["meta"]
        from_node_num, to_node_num, channel, timestamp, conn_id = (
            meta["fromNodeNum"],
            meta["toNodeNum"],
            meta.get("channel", 0),
            meta["timestamp"],
            meta["connId"],
        )
        data = packet["data"]
        id_, decoded, reply_id, want_reply, want_ack = (
            data["id"],
            data.get("decoded"),
            data.get("replyId"),
            data.get("wantReply"),
            data.get("wantAck"),
        )
        message = decoded.get("payload") if decoded else None

        InsertHandlers.insertMessage({
            "contactId": str(from_node_num),
            "messageId": id_,
            "channelId": channel,
            "message": message,
            "fromNodeNum": from_node_num,
            "toNodeNum": to_node_num,
            "timestamp": timestamp,
            "protocol": "Meshtastic",
            "sender": reply_id,
            "options": json.dumps({
                "replyId": reply_id,
                "wantReply": want_reply,
                "wantAck": want_ack
            }),
            "connId": conn_id,
        })

        print("[dispatchMessages] message")

    def handle_Message(self, sub_packet: dict):
        print("[dispatchMessage] Message", sub_packet)

    def handle_text(self, packet: dict):
        outer_data = normalize_packet(packet)
        data,  meta = outer_data["data"], outer_data["meta"]
        print("[dispatchMessage] text", packet,
              decode_node_info(data["topic"]))

    def handle_ClientNotification(self, packet: dict):
        print("[dispatchMessage] ClientNotification")

    def handle_clientNotification(self, packet: dict):
        print("[dispatchMessage] clientNotification")
