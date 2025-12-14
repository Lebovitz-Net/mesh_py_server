from aiohttp import web
from src.api.handlers import api_handlers
from src.config.config import get_node_ip, set_node_ip


def register_routes(app: web.Application):

    # --- Root ---
    app.router.add_get("/", api_handlers["health"])

    # --- Runtime Config ---
    async def get_node_ip_route(request):
        return web.json_response({"ip": get_node_ip()})
    app.router.add_get("/api/v1/node-ip", get_node_ip_route)

    async def set_node_ip_route(request):
        body = await request.json()
        ip = body.get("ip")
        if not ip or ":" not in ip:
            return web.json_response(
                {"error": 'Invalid IP format. Expected "host:port".'},
                status=400,
            )
        set_node_ip(ip)
        return web.json_response({"success": True, "ip": ip})
    app.router.add_post("/api/v1/node-ip", set_node_ip_route)

    # --- System ---
    app.router.add_get("/api/v1/config", api_handlers["getConfig"])
    app.router.add_get("/api/v1/version", api_handlers["getVersion"])
    app.router.add_get("/api/v1/health", api_handlers["getHealth"])

    # --- Nodes ---
    async def list_connections(request):
        return await api_handlers["listConnections"](request.match_info["id"])
    app.router.add_get("/api/v1/nodes/{id}/connections", list_connections)

    async def get_node_handler(request):
        return await api_handlers["getNodeHandler"](request.match_info["id"])
    app.router.add_get("/api/v1/nodes/{id}", get_node_handler)

    async def delete_node_handler(request):
        return await api_handlers["deleteNodeHandler"](request.match_info["id"])
    app.router.add_delete("/api/v1/nodes/{id}", delete_node_handler)

    app.router.add_get("/api/v1/nodes", api_handlers["listNodesHandler"])

    async def list_channels(request):
        return await api_handlers["listChannels"](request.match_info["id"])
    app.router.add_get("/api/v1/channels/{id}", list_channels)

    # --- Messages ---
    app.router.add_get("/api/v1/messages", api_handlers["listMessagesHandler"])

    async def send_message_handler(request):
        body = await request.json()
        return await api_handlers["sendMessageHandler"](body)
    app.router.add_post("/api/v1/messages", send_message_handler)

    # --- My Info ---
    app.router.add_get("/api/v1/myinfo", api_handlers["listMyInfoHandler"])

    # --- Contacts ---
    app.router.add_get("/api/v1/contacts", api_handlers["listContactsHandler"])

    # --- Packets ---
    app.router.add_get("/api/v1/packets", api_handlers["listPacketsHandler"])

    async def get_packet_handler(request):
        return await api_handlers["getPacketHandler"](request.match_info["id"])
    app.router.add_get("/api/v1/packets/{id}", get_packet_handler)

    async def inject_packet_handler(request):
        body = await request.json()
        return await api_handlers["injectPacketHandler"](body)
    app.router.add_post("/api/v1/packets", inject_packet_handler)

    # --- Metrics ---
    async def get_packet_logs(request):
        return await api_handlers["getPacketLogs"](request.match_info["id"])
    app.router.add_get("/api/v1/nodes/{id}/packet-logs", get_packet_logs)

    async def get_telemetry(request):
        return await api_handlers["getTelemetry"](request.match_info["id"])
    app.router.add_get("/api/v1/nodes/{id}/telemetry", get_telemetry)

    async def get_events(request):
        return await api_handlers["getEvents"](request.match_info["id"])
    app.router.add_get("/api/v1/nodes/{id}/events", get_events)

    app.router.add_get("/api/v1/metrics", api_handlers["getMetrics"])

    # --- Diagnostics & Logs ---
    app.router.add_get("/api/v1/logs", api_handlers["getLogsHandler"])

    # --- Config ---
    app.router.add_get("/api/v1/config/full", api_handlers["getFullConfigHandler"])

    async def get_config_handler(request):
        return await api_handlers["getConfigHandler"](request.match_info["id"])
    app.router.add_get("/api/v1/config/{id}", get_config_handler)

    app.router.add_get("/api/v1/configs", api_handlers["listAllConfigsHandler"])

    async def get_module_config_handler(request):
        return await api_handlers["getModuleConfigHandler"](request.match_info["id"])
    app.router.add_get("/api/v1/module-config/{id}", get_module_config_handler)

    app.router.add_get("/api/v1/module-configs", api_handlers["listAllModuleConfigsHandler"])

    async def get_metadata_by_key_handler(request):
        return await api_handlers["getMetadataByKeyHandler"](request.match_info["key"])
    app.router.add_get("/api/v1/metadata/{key}", get_metadata_by_key_handler)

    app.router.add_get("/api/v1/metadata", api_handlers["listAllMetadataHandler"])
    app.router.add_get("/api/v1/files", api_handlers["listFileInfoHandler"])

    # --- Control ---
    app.router.add_post("/api/v1/restart", api_handlers["restartServicesHandler"])
    app.router.add_post("/api/v1/reload-config", api_handlers["reloadConfigHandler"])
