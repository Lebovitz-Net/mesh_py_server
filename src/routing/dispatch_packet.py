# src/routing/dispatch_packet.py

import asyncio
import threading
from external.meshcore_py.src.constants import Constants
from external.meshcore_py.src.events import EventEmitter

# Import all dispatch domains as classes
from .dispatch_messages import DispatchMessages
from .dispatch_configs import DispatchConfigs
from .dispatch_contacts import DispatchContacts
from .dispatch_nodes import DispatchNodes
from .dispatch_metrics import DispatchMetrics
from .dispatch_channels import DispatchChannels
from .dispatch_mqtt import DispatchMqtt
from .dispatch_diagnostics import DispatchDiagnostics
from .process_mesh_packet import process_mesh_packet


class DispatchPacket(
    DispatchMessages,
    DispatchConfigs,
    DispatchContacts,
    DispatchNodes,
    DispatchMetrics,
    DispatchChannels,
    DispatchMqtt,
    DispatchDiagnostics,
    EventEmitter
):
    def __init__(self, loop: asyncio.AbstractEventLoop = None):
        EventEmitter.__init__(self, loop=loop)
        self.response_map = self._build_response_map()
        self._lock = threading.RLock()

    def _build_response_map(self):
        response_codes = Constants.ResponseCodes
        push_codes = Constants.PushCodes
        all_codes = {
            **{k: v for k, v in vars(response_codes).items() if not k.startswith("__")},
            **{k: v for k, v in vars(push_codes).items() if not k.startswith("__")},
        }
        return {value: key for key, value in all_codes.items()}

    def get_type_name(self, type_):
        if isinstance(type_, int):
            return self.response_map.get(type_)
        return type_

    def dispatch_packet(self, sub_packet: dict):
        if not sub_packet:
            return
        type_ = sub_packet.get("type")
        key = self.get_type_name(type_)
        handler = getattr(self, f"handle_{key}", None)

        with self._lock:
            if handler:
                try:
                    handler(sub_packet)
                except Exception as err:
                    print(f"[DispatchPacket] Handler {key} failed:", err)
                else:
                    self.emit(key or type_, sub_packet)
            else:
                print(f"[DispatchPacket] No handler for type {key}")

    def handle_mesh_packet(self, packet: dict):
        result = process_mesh_packet(packet)
        if result:
            self.dispatch_packet(result)

    def handle_data(self, packet: dict):
        sub_packet = packet.get("data")
        return sub_packet

    def handle_decoded(self, packet: dict):
        pass


# --- Eager singleton instance created at import time ---
_dispatcher_instance = DispatchPacket()

def get_dispatcher() -> DispatchPacket:
    """Return the singleton DispatchPacket instance."""
    return _dispatcher_instance

def dispatch_packet(sub_packet: dict):
    """Convenience function to dispatch a packet via the singleton instance."""
    _dispatcher_instance.dispatch_packet(sub_packet)
