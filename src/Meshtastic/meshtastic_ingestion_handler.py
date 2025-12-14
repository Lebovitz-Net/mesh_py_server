# src/meshtastic/handlers/meshtastic_ingestion_handler.py
from external.meshcore_py.src.events import EventEmitter
from .protobufs.proto_decode import decode_from_radio_frame
from .route_packet import route_packet

class MeshtasticIngestionHandler(EventEmitter):
    """
    Event-driven ingestion handler.
    Subscribes to packet events from a MeshtasticHandler and routes them.
    """

    def __init__(self):
        super().__init__()

    def register(self, mesh_handler):
        """
        Subscribe to 'packet' events from a mesh handler.
        """
        mesh_handler.on("packet", self.ingest)

    def ingest(self, meta: dict, buffer: bytes):
        """
        Ingest a raw packet from the Meshtastic runtime.
        Decodes the frame and routes it into the packet pipeline.
        """
        try:
            frame = decode_from_radio_frame(buffer)
            if not frame:
                print("[meshtasticIngest] Failed to decode frame")
                return

            # Hand off to the router
            route_packet(frame, meta)

            # Re-emit for downstream consumers (optional)
            self.emit("ingest", frame, meta)

        except Exception as err:
            print("[meshtasticIngest] Error ingesting packet:", err)
