# Simple Minecraft Query Flask RESTful API

A lightweight REST API for querying Minecraft server status (Java, legacy, and Bedrock) using the mcstatus library.  
Perfect for dashboards, bots, and monitoring tools.

## Features
- Supports Java (1.7+), legacy Java (Beta 1.8-1.6), and Bedrock.
- Simple **RESTful** endpoints.
- Lightweight Flask backend.
- **Cached** responses.
- **Rate-limited** endpoints.
- Ready for [Heroku](https://heroku.com) and [Render](https://render.com) deployment.

## Running Locally

### Development server
```
python -m app
```

### Production server (Waitress)
```
waitress-serve --listen=127.0.0.1:3000 app:create_app
```

[VSCode](https://code.visualstudio.com/) launch configurations are included.

## Deployment

### Heroku
- Uses the included `Procfile` automatically

### Render
- Set start command to:
```
./Render.sh
```

## API Endpoints

Get full server info:
```
GET /api/{version}/full/{ip}/{port?}
```
Example result:
```
{
  "cached_at": "2026-04-02T01:09:10.903972",
  "message": {
    "ip:port": "mc.hypixel.net:25565",
    "players": "19823",
    "players_max": "200000",
    "ping": "406",
    "version": "Requires MC 1.8 / 1.21",
    "version_protocol": "47",
    "description": "§f                 §aHypixel Network §c[1.8/1.21]\n§f       §b§lEASTER EVENT §7§l+ §6§lANNIVERSARY BINGO"
  }
}
```

Get player count:
```
GET /api/{version}/playercount/{ip}/{port?}
```
Example result:
```
{
  "cached_at": "2026-04-02T01:10:40.548396",
  "message": {
    "players": "19798"
  }
}
```

Get latency:
```
GET /api/{version}/latency/{ip}/{port?}
```
Example result:
```
{
  "cached_at": "2026-04-02T16:59:01.036532",
  "message": {
    "latency": "155"
  }
}
```

The version parameter in the url can be:
- `java` (1.7+)
- `java_legacy` (Beta 1.8-1.6)
- `bedrock`

### Example
```
https://your-app-url.com/api/full/java/mc.hypixel.net
```
