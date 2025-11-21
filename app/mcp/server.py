from mcp.server import Server
from mcp.server.stdio import stdio_server

# servidor inicial básico
server = Server("servicios-mcp")

# entrypoint principal
if __name__ == "__main__":
    stdio_server(server)
