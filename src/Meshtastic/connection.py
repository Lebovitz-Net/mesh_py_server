# src/meshtastic/connection.py
import time
from typing import Any, Dict
from asyncio import Queue
from external.meshcore_py.src.events import EventEmitter

class Connection(EventEmitter):
    mesh_runtime = None

    def __init__(self, conn_id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn_id = conn_id
        self.meta_overrides: Dict[str, Any] = {}
        self._event_queue = Queue()

    @classmethod
    def bind_mesh_runtime(cls, runtime):
        cls.mesh_runtime = runtime

    def on_received_packet(self, meta: Dict[str, Any], buffer: bytes):
        enriched_meta = {
            **meta,
            **self.meta_overrides,
            "connId": self.conn_id,
            "timestamp": int(time.time() * 1000),
        }
        # Instead of EventEmitter, we enqueue events
        self._event_queue.put_nowait(("packet", enriched_meta, buffer))

    async def next_event(self):
        """Async iterator for events."""
        return await self._event_queue.get()

    def send_packet(self, buffer: bytes):
        raise NotImplementedError("send_packet() must be implemented by subclass")

    def send(self, packet: bytes):
        if not Connection.mesh_runtime:
            raise RuntimeError("Mesh runtime not bound")
        Connection.mesh_runtime.send(packet)

    def want_config_id(self):
        from meshtastic.protobufs.proto_utils import build_to_radio_frame
        self.send(build_to_radio_frame("wantConfigId", 0))

    def send_message(self, text: str, to: int = None):
        from meshtastic.protobufs.proto_utils import build_text_message
        self.send(build_text_message({"message": text, "toNodeNum": to}))

    def request_telemetry(self):
        from meshtastic.protobufs.proto_utils import build_request_telemetry_frame
        self.send(build_request_telemetry_frame())

    def request_position(self):
        from meshtastic.protobufs.proto_utils import build_request_position_frame
        self.send(build_request_position_frame())

    def request_node_info(self):
        from meshtastic.protobufs.proto_utils import build_request_node_info_frame
        self.send(build_request_node_info_frame())
