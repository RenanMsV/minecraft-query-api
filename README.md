# Minecraft Query API

A lightweight RESTful API for querying Minecraft server status (Java, legacy, and Bedrock) using the [mcstatus](https://pypi.org/project/mcstatus/) library.
Perfect for dashboards, bots, and monitoring tools.

## Features
- Supports Java (1.7+), legacy Java (Beta 1.8-1.6), and Bedrock.
- Simple **RESTful** endpoints.
- Lightweight Flask backend.
- **Cached** responses.
- [**Rate-limited**](#rate-limit-configs) endpoints.
- Ready for [Heroku](https://heroku.com) and [Render](https://render.com) deployment.

---

## Running Locally

### Development server
```sh
python -m app
```

### Production server (Waitress)
```sh
waitress-serve --listen=127.0.0.1:3000 app:create_app
```

[VSCode](https://code.visualstudio.com/) launch configurations are included.

## Deployment

### Heroku
- Uses the included `Procfile` automatically

### Render
- Set start command to:
```sh
./Render.sh
```

---

## API Endpoints

Get full server info:
```
GET /api/{version}/full/{ip}/{port?}
```
Example result:
```json
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
```json
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
```json
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

---

## Configuring the API

Environment variables are used to configure the API and override default values.

By default, the project runs entirely in memory and does not require external services like Redis. However, this can be changed by setting the appropriate environment variables. Use the .env.example as a guide.

---

## Cache

This project uses [Flask-Caching](https://pypi.org/project/Flask-Caching/) to provide response caching.

Requests are cached, and cached responses are returned until the cache expires. By default, the API uses in-memory caching and does not require external services like Redis. However, this can be changed by configuring the appropriate environment variables.

---

## Rate Limiting

This project uses [Flask-Limiter](https://flask-limiter.readthedocs.io/en/stable/index.html#installation) to provide Rate-Limits.

### Storage Backend Dependencies

By default, this API uses in-memory storage.
If you choose a different storage backend, you may need to install additional dependencies manually.

For production use, [Redis](https://pypi.org/project/redis) is recommended:

```sh
pip install Flask-Limiter[redis]
```

Other supported backends:

- Memcached → `pip install Flask-Limiter[memcached]`
- MongoDB → `pip install Flask-Limiter[mongodb]`
- Valkey → `pip install Flask-Limiter[valkey]`

For more information on supported backends, refer to the Flask-Limiter [documentation](https://flask-limiter.readthedocs.io/en/stable/index.html#installation) and the [storage](https://limits.readthedocs.io/en/stable/storage.html) options.
