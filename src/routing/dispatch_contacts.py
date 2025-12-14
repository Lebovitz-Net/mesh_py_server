# src/routing/dispatch_contacts.py

import json
from src.utils import get_text_from_key, hash_public_key, get_public_key_value
from src.db.insert_handlers import InsertHandlers


class DispatchContacts:
    def handle_Contact(self, packet: dict):
        outer_data = packet["data"]
        data = outer_data["data"]
        meta = outer_data["meta"]

        public_key = data["publicKey"]
        shaped = {
            "contactId": data["advName"],
            "type": data["type"],
            "name": data["advName"],
            "publicKey": get_text_from_key(public_key),
            "protocol": "meshcore",
            "nodeNum": hash_public_key(public_key),
            "shortName": None,
            "times": json.dumps({
                "lastHeard": data["lastAdvert"],
                "lastMod": data["lastMod"]
            }),
            "options": json.dumps({
                "outPath": data["outPath"].hex(),
                "outPathLen": data["outPathLen"],
                "flags": data["flags"],
            }),
            "position": json.dumps({
                "lat": data["advLat"],
                "lon": data["advLon"]
            }),
            **meta,
        }

        # NOTE: if InsertHandlers.insertUsers is raising an error,
        # double‑check the schema of `shaped` against your DB expectations.
        InsertHandlers.insertUsers(shaped)

    def handle_ContactsStart(self, packet: dict):
        print(".../ContactsStart")

    def handle_EndOfContacts(self, packet: dict):
        print(".../EndOfContacts")
