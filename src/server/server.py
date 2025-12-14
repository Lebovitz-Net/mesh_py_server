from aiohttp import web
import aiohttp_cors

from src.server.startup_meshcore import start_meshcore, shutdown_meshcore
from src.server.startup_meshtastic import start_meshtastic, shutdown_meshtastic
from src.server.startup_mqtt import start_mqtt_server, shutdown_mqtt_server
from src.server.sse import sse_events, shutdown as sse_shutdown
from src.api.routes import register_routes
from src.api.services_manager import shutdown as services_shutdown

async def root(request):
    return web.Response(text="MeshManager v2 is running")

async def get_sse_events(request):
    events = await sse_events()
    return web.json_response(events)


async def startup(app: web.Application):
    # loop = app.loop
    # set_event_loop(loop)
    # set_socket_loop(loop)

    print("step 1 start_meshcore")
    app["meshcore"] = await start_meshcore()

    print("step 2 start_meshtastic")
    # app["meshtastic"] = await start_meshtastic()

    print("step 3 start_mqtt_server")
    app["mqtt_client"] = await start_mqtt_server()

    print("✅ completed startups")


async def shutdown(app: web.Application):
    print("🔻 Shutting down...")

    if "mqtt_client" in app:
        shutdown_mqtt_server(app["mqtt_client"])
        print("MQTT client shut down.")

    if "meshcore" in app:
        shutdown_meshcore(app["meshcore"]["meshcore"])
        print("Meshcore shut down.")

    if "meshtastic" in app:
        shutdown_meshtastic(app["meshtastic"])
        print("Meshtastic shut down.")

    sse_shutdown()
    services_shutdown("shutdown")
    print("SSE and services shut down.")
    print("✅ Server shutdown complete.")


def create_app() -> web.Application:
    app = web.Application()

    # routes
    app.router.add_get("/", root)
    app.router.add_get("/sse/events", get_sse_events)
    register_routes(app)

    # hooks
    app.on_startup.append(startup)
    app.on_cleanup.append(shutdown)

    # CORS
    cors = aiohttp_cors.setup(app, defaults={
        "http://localhost:5173": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)

    return app
