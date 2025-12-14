# packet_router.py
from  src.routing.dispatch_packet import dispatch_packet
from .utils.node_mapping import get_mapping
from .protobufs.proto_utils import deserialize, get_protobufs

def enrich_meta(value: dict = None, meta: dict = None):
    ts = int(__import__("time").time() * 1000)
    mapping = get_mapping(meta.get("sourceIp"))
    return {
        **(meta or {}),
        "timestamp": ts,
        "fromNodeNum": value.get("from") or meta.get("fromNodeNum") or mapping.get("num"),
        "toNodeNum": value.get("to") or meta.get("toNodeNum") or 0xFFFFFFFF,
        "device_id": meta.get("sourceIp") or mapping.get("device_id"),
    }

def route_packet(input, meta: dict = None):
    diag_packet = None
    try:
        # Decode into a protobuf object
        if isinstance(input, (bytes, bytearray)):
            # Assume meta["type"] tells us which class to use
            cls = get_protobufs(meta.get("type"))
            if not cls:
                return
            data = deserialize(cls, input)
        else:
            data = input  # already a protobuf object

        if not data:
            return

        diag_packet = data
        desc = data.DESCRIPTOR

        # Handle oneofs
        for oneof in desc.oneofs:
            field = data.WhichOneof(oneof.name)
            if field:
                value = getattr(data, field)
                dispatch_packet({
                    "type": field,
                    "data": data,
                    "meta": enrich_meta(value, meta),
                })
                return

        # Fallback: dispatch by message type name
        dispatch_packet({
            "type": desc.name,
            "data": data,
            "meta": enrich_meta(data, meta),
        })

    except Exception as err:
        print("[routePacket] Failed to route packet:", err, diag_packet)
