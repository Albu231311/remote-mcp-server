"""
QuoteOfTheDay — Remote MCP Server

A lightweight MCP server that serves famous quotes.  Designed to run
on a cloud platform (Render, Cloud Run, etc.) using the Streamable HTTP
transport so any MCP host can call it over the Internet.

Local testing:
    python server.py          # starts on http://0.0.0.0:8080/mcp

The MCP endpoint is at /mcp (the FastMCP default for streamable-http).
"""

import os
from datetime import datetime, timezone
from typing import Any

from mcp.server.fastmcp import FastMCP

import quotes_data
from mcp.server.transport_security import TransportSecuritySettings

mcp = FastMCP(
    name="remote_quotes",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False
    ),
    instructions=(
        "A remote MCP server that provides famous and motivational quotes. "
        "Use obtener_frase_del_dia for a random daily quote, buscar_frases "
        "to search by author or keyword, and obtener_fecha_hora_servidor to "
        "confirm the server is running remotely in the cloud."
    ),
)


@mcp.tool()
def obtener_frase_del_dia() -> dict[str, str]:
    """Devuelve una frase celebre aleatoria del dia.

    Returns:
        Un diccionario con 'autor' y 'frase'.
    """
    return quotes_data.frase_aleatoria()


@mcp.tool()
def buscar_frases(texto: str) -> list[dict[str, str]]:
    """Busca frases por nombre de autor o por una palabra clave.

    Args:
        texto: Texto a buscar (coincidencia parcial, sin importar mayusculas).

    Returns:
        Lista de frases que coinciden.  Cada elemento tiene 'autor' y 'frase'.
    """
    resultados = quotes_data.buscar(texto)
    if not resultados:
        return [{"mensaje": f"No se encontraron frases con '{texto}'."}]
    return resultados


@mcp.tool()
def obtener_fecha_hora_servidor() -> dict[str, Any]:
    """Devuelve la fecha y hora actual del servidor remoto.

    Util para confirmar que el servidor esta ejecutandose en la nube
    y no de forma local.

    Returns:
        Diccionario con la fecha, hora y zona horaria del servidor.
    """
    ahora = datetime.now(timezone.utc)
    return {
        "fecha": ahora.strftime("%Y-%m-%d"),
        "hora": ahora.strftime("%H:%M:%S"),
        "zona_horaria": "UTC",
        "timestamp_iso": ahora.isoformat(),
        "mensaje": "Este timestamp proviene del servidor remoto en la nube.",
    }


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8080))
    app = mcp.streamable_http_app()
    uvicorn.run(app, host="0.0.0.0", port=port)
