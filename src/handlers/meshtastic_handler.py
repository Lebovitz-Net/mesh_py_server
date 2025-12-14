import asyncio
from meshcore_py import EventEmitter
from ..meshtastic.tcp_connection import TcpConnection
from ..meshtastic.serial_connection import SerialConnection


class MeshtasticHandler(EventEmitter):
    def __init__(self, conn_id: str, host: str, port: int, opts: dict = None):
        super().__init__()
        opts = opts or {}
        reconnect = opts.get("reconnect", {"enabled": True})
        get_config_on_connect = opts.get("getConfigOnConnect", False)

        # Single TCP connection
        self.connection = TcpConnection(host, port, conn_id)

        # Serial connection
        self.serial_conn = SerialConnection("/dev/ttyUSB0", 115200, "serial-1")

        # Subscribe to packet events
        for conn in [self.connection, self.serial_conn]:
            conn.on("packet", self._handle_packet)
            conn.on("connect", lambda meta: print(f"[Bridge] Connected: {meta}"))
            conn.on("error", lambda meta, err: print(f"[Bridge] Error: {meta}, {err}"))

    def _handle_packet(self, meta, buffer: bytes):
        """
        Handle incoming packets directly here instead of routing through meshGateway.
        Consumers can subscribe to 'packet' events on this handler.
        """
        self.emit("packet", meta, buffer)

    def send(self, packet: bytes):
        if isinstance(packet, (bytes, bytearray)):
            self.connection.write(packet)
        else:
            raise TypeError("[MeshtasticHandler] send packet must be bytes")

    def end(self):
        self.connection.stop()

    # Convenience wrappers for event subscription
    def on(self, event_name, callback):
        return super().on(event_name, callback)

    def off(self, event_name, callback):
        return super().off(event_name, callback)

    # --- Shutdown ---
    def shutdown(self):
        """Gracefully shutdown TCP and Serial connections, then close handler."""
        print("[MeshtasticHandler] Shutting down...")

        # TCP connection
        if self.connection:
            try:
                self.connection.shutdown()
                print("[MeshtasticHandler] TCP connection shut down.")
            except Exception as e:
                print(f"[MeshtasticHandler] Error shutting down TCP connection: {e}")
            finally:
                self.connection = None

        # Serial connection
        if self.serial_conn:
            try:
                self.serial_conn.shutdown()
                print("[MeshtasticHandler] Serial connection shut down.")
            except Exception as e:
                print(f"[MeshtasticHandler] Error shutting down serial connection: {e}")
            finally:
                self.serial_conn = None

        # Close event emitter
        try:
            super().close()
            print("[MeshtasticHandler] EventEmitter closed.")
        except Exception as e:
            print(f"[MeshtasticHandler] Error closing EventEmitter: {e}")

        print("[MeshtasticHandler] Shutdown complete.")
