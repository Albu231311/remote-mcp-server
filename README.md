# QuoteOfTheDay — Remote MCP Server

A remote MCP server that serves famous quotes over the Internet using
the Streamable HTTP transport. Built for Universidad del Valle de
Guatemala's CC3067 Networks course, Project 1, item 7 (remote MCP
server).

## Tools

| Tool | Parameters | Returns |
|---|---|---|
| `obtener_frase_del_dia` | *(none)* | A random famous quote with author |
| `buscar_frases` | `texto: str` | Quotes matching the author name or keyword |
| `obtener_fecha_hora_servidor` | *(none)* | Current server date/time in UTC (proves it runs remotely) |

## Running locally

```bash
pip install -r requirements.txt
python server.py
# Server starts at http://0.0.0.0:8080/mcp
```

## Deploying to Render

1. Push this directory to a GitHub repository.
2. Go to [render.com](https://render.com) and create a new **Web Service**.
3. Connect your GitHub repo and point the root directory to
   `remote-mcp-server/`.
4. Render will detect the `Dockerfile` and build automatically.
5. Once deployed, note the public URL (e.g.
   `https://your-app.onrender.com`). The MCP endpoint will be at
   `https://your-app.onrender.com/mcp`.

## Using from the host chatbot

Add this entry to `host/config.py`:

```python
"remote_quotes": {
    "url": "https://your-app.onrender.com/mcp",
},
```

Then run the chatbot and ask something like:

```
You: Dame la frase del día
You: Busca frases de Einstein
You: ¿Qué hora es en el servidor remoto?
```
