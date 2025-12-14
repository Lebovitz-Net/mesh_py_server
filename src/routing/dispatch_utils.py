def normalize_packet(packet):
    if "meta" in packet:
        # Meshtastic
        return {
            "packet_type": "meshtastic",
            "data": packet.get("data"),
            "meta": packet.get("meta")
        }
    elif isinstance(packet.get("data"), dict) and "meta" in packet["data"]:
        # Meshcore
        inner = packet["data"]
        return {
            "packet_type": "meshcore",
            "data": inner.get("data"),
            "meta": inner.get("meta")
        }
    else:
        # Unknown shape
        return {
            "packet_type": "unknown",
            "data": packet.get("data"),
            "meta": packet.get("meta")
        }
    