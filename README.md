# Minecraft Query API

A lightweight RESTful API for querying Minecraft server status (Java, legacy, and Bedrock) using the [mcstatus] library.
Perfect for dashboards, bots, and monitoring tools.

## Features
- Supports Java (1.7+), legacy Java (Beta 1.8-1.6), and Bedrock.
- Simple **RESTful** endpoints.
- Lightweight Flask backend.
- [**Cached**](#cache) responses.
- [**Rate-limited**](#rate-limiting) endpoints.
- Ready for [Heroku] and [Render] deployment.

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

[VSCode] launch configurations are included.

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

By default, the project runs entirely in memory and does not require external services like [Redis]. However, this can be changed by setting the appropriate environment variables. Use the [.env.example](.env.example) as a guide.

---

## Cache

This project uses [Flask-Caching] to provide response caching.

Requests are cached, and cached responses are returned until the cache expires.

### Cache storage backend dependencies

By default, this API uses in-memory storage. If you choose a different storage backend, you may need to install additional dependencies manually.

For production use, [Redis] is recommended:

```sh
pip install redis
```

---

## Rate Limiting

This project uses [Flask-Limiter] to provide Rate-Limits.

### Storage backend dependencies

By default, this API uses in-memory storage.
If you choose a different storage backend, you may need to install additional dependencies manually.

For production use, [Redis] is recommended:

```sh
pip install Flask-Limiter[redis]
```

Other supported backends:

- Memcached → `pip install Flask-Limiter[memcached]`
- MongoDB → `pip install Flask-Limiter[mongodb]`
- Valkey → `pip install Flask-Limiter[valkey]`

For more information on supported backends, refer to the Flask-Limiter [documentation](https://flask-limiter.readthedocs.io/en/stable/index.html#installation) and the [storage](https://limits.readthedocs.io/en/stable/storage.html) options.

## License

This project is licensed under the [MIT License].

## Third-Party Dependencies

This project relies on several open-source libraries, including:

- [Flask]
- [Flask-RESTful]
- [Flask-Caching]
- [Flask-Limiter]
- [mcstatus]
- [waitress]
- [python-dotenv]

And a few optional ones like:

- [Redis]
- [Pymemcache]

All third-party libraries retain their respective licenses.

[Heroku]: https://heroku.com
[Render]: https://render.com
[VSCode]: https://code.visualstudio.com/
[waitress]: https://pypi.org/project/waitress/
[Flask]: https://pypi.org/project/Flask/
[Flask-RESTful]: https://pypi.org/project/Flask-RESTful/
[Flask-Caching]: https://pypi.org/project/Flask-Caching/
[Flask-Limiter]: https://pypi.org/project/Flask-Limiter/
[Redis]: https://pypi.org/project/redis/
[Pymemcache]: https://pypi.org/project/pymemcache/
[mcstatus]: https://pypi.org/project/mcstatus/
[python-dotenv]: https://pypi.org/project/python-dotenv/
[MIT License]: https://opensource.org/license/mit
