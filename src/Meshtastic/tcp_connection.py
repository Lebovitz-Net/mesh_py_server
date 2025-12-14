# src/meshtastic/tcp_connection.py
import uuid
from .connection import Connection
from .tcp_socket import TcpSocket
from .schedule_reconnect import schedule_reconnect

class TcpConnection(Connection):
    def __init__(self, host: str, port: int, conn_id: str = None, *args, **kwargs):
        super().__init__(conn_id or str(uuid.uuid4()), *args, **kwargs)
        self.host = host
        self.port = port
        self.tcp_connections = {}
        self.reconnect_policy = True
        self.is_shutting_down = False

    def connect(self, conn_id=None):
        conn_id = conn_id or self.conn_id
        tcp = TcpSocket(conn_id, self.host, self.port)
        self.tcp_connections[conn_id] = {
            "tcp": tcp,
            "host": self.host,
            "port": self.port,
            "reconnectTimer": None,
        }
        return tcp

    async def start(self):
        tcp = self.connect(self.conn_id)
        await tcp.connected_promise
        print(f"[TcpConnection {self.conn_id}] Startup complete")
        return tcp

    def stop(self):
        self.is_shutting_down = True
        for entry in self.tcp_connections.values():
            tcp = entry["tcp"]
            if entry["reconnectTimer"]:
                entry["reconnectTimer"].cancel()
            tcp.end()
        self.tcp_connections.clear()

    def write(self, buf: bytes, conn_id=None):
        conn_id = conn_id or self.conn_id
        entry = self.tcp_connections.get(conn_id)
        tcp = entry["tcp"] if entry else None
        if not tcp:
            return False
        tcp.write(buf)
        return True

    # --- Shutdown ---
    def shutdown(self):
        """Gracefully shutdown all TcpSockets and cancel reconnects."""
        print(f"[TcpConnection {self.conn_id}] Shutting down...")
        self.is_shutting_down = True

        for conn_id, entry in list(self.tcp_connections.items()):
            tcp = entry["tcp"]
            try:
                if entry["reconnectTimer"]:
                    entry["reconnectTimer"].cancel()
                    print(f"[TcpConnection {conn_id}] Reconnect timer cancelled.")
                # Prefer shutdown() if TcpSocket implements it
                if hasattr(tcp, "shutdown"):
                    tcp.shutdown()
                    print(f"[TcpConnection {conn_id}] TcpSocket shutdown called.")
                else:
                    tcp.end()
                    print(f"[TcpConnection {conn_id}] TcpSocket ended.")
            except Exception as e:
                print(f"[TcpConnection {conn_id}] Error during shutdown: {e}")
            finally:
                self.tcp_connections.pop(conn_id, None)

        print(f"[TcpConnection {self.conn_id}] Shutdown complete.")
