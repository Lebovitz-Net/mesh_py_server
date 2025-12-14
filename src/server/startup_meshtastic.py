# src/startup/meshtastic_startup.py

import os
import asyncio
from src.handlers.meshtastic_handler import MeshtasticHandler
from src.meshtastic.protobufs.proto_utils import build_to_radio_frame, init_proto_types
from src.meshtastic.utils.node_mapping import wait_for_mapping

async def start_meshtastic():
    init_proto_types()
    host = os.getenv("NODE_IP", "192.168.2.79")
    port = int(os.getenv("NODE_PORT", "4403"))
    mesh = MeshtasticHandler("mesh-1", host, port)

    # Startup sequence...
    mesh.send(build_to_radio_frame("want_config_id"))
    mapping = await wait_for_mapping(host, timeout=5000)
    print(f"[mesh-1] Startup complete, mapping ready: {mapping}")

    return mesh

def shutdown_meshtastic(mesh: MeshtasticHandler):
    """Gracefully shutdown Meshtastic handler (TCP + Serial)."""
    print("[MeshtasticStartup] Shutting down Meshtastic...")
    try:
        if mesh:
            mesh.shutdown()
            print("[MeshtasticStartup] Handler shut down.")
    except Exception as e:
        print(f"[MeshtasticStartup] Error during shutdown: {e}")
    print("[MeshtasticStartup] Shutdown complete.")
