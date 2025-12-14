# src/api/services_manager.py
import time
from src.db.query_handlers import query_handlers

def teardown_services():
    """Tear down backend services (placeholder)."""
    print("⚠️  Tearing down services...")
    # Add explicit shutdown calls here if needed, e.g. meshcore.shutdown(), mqtt.shutdown(), etc.
    print("✅ Teardown complete.")

def init_services(config):
    """Initialize backend services (placeholder)."""
    print("🚀 Initializing backend services...")
    # Add explicit startup calls here if needed, e.g. start_tcp_server(config), start_ws_server(config), etc.
    print("✅ All services initialized.")

def shutdown(signal="manual"):
    """Gracefully shut down services when a signal is received."""
    print(f"\n⚠️  Received {signal}, shutting down gracefully...")
    teardown_services()

def restart_services():
    """Restart backend services by tearing down and reinitializing with fresh config."""
    print("🔄 Restarting backend services...")
    teardown_services()
    time.sleep(1)
    config = query_handlers["getFullConfig"]()
    init_services(config)
    print("✅ Restart complete.")
    return {"restarted": True, "timestamp": int(time.time() * 1000)}
