# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2026-04-26

### Added

- Added [VSCode] launch configurations.
- Implemented request rate limiting using [Flask-Limiter].
- The API is now configurable via environment variables.
- Added an example environment file: [.env.example](.env.example).
- Added support for [Redis], [Memcached], and other storage backends for caching and rate limiting.
- Added [CHANGELOG.md](CHANGELOG.md) to document the changes to this project.
- The project is now licensed under the [MIT License].
- Better logging is displayed during initialization.

### Changed

- Requirements: Uses `>=` instead of `==` for better dependency handling.
- Configs are now lazy loaded.
- Root page content has been reduced a bit.

## [1.2.0] - 2026-04-02

### Added

- Latency endpoint for Java, Legacy Java and Bedrock.

## [1.1.1] - 2026-04-02

### Changed

- Source code refactored, maintaining the same functionality.

## [1.1.0] - 2026-03-26

### Added

- Add support to legacy Minecraft servers.
- Add support for deploying on [Render] using the [Render.sh](Render.sh) file.

## [1.0.4] - 2026-03-26

### Changed

- Bump [waitress] from 3.0.1 to 3.0.2.

## [1.0.3] - 2026-03-24

### Security

- Bump [Flask] from 2.2.5 to 3.1.3 [CVE-2026-27205].
- Bump [Flask-Caching] from 2.0.1 to 2.3.1.
- Bump [Flask-RESTful] from 0.3.9 to 0.3.10.

## [1.0.2] - 2024-10-29

### Security

- Bump [Flask] from 2.2.2 to 2.2.5. [CVE-2023-30861].

## [1.0.1] - 2024-10-29

### Security

- Bump [waitress] from 2.1.2 to 3.0.1. [CVE-2024-49768].

## [1.0.0] - 2022-08-29

### Added

- Initial release of this RESTful API powered by [Flask].
- Full server info endpoints for Java, Bedrock.
- Player amount endpoints for Java, Bedrock.
- Using [waitress] as prod wsgi.
- Caching responses with [Flask-Caching]
- Procfile ready for deploying on [Heroku].

[unreleased]: https://github.com/RenanMsV/minecraft-query-api/compare/main...dev
[1.3.0]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.3.0
[1.2.0]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.2.0
[1.1.1]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.1.1
[1.1.0]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.1.0
[1.0.4]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.0.4
[1.0.3]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.0.3
[1.0.2]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.0.2
[1.0.1]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.0.1
[1.0.0]: https://github.com/RenanMsV/minecraft-query-api/releases/tag/1.0.0
[Heroku]: https://heroku.com
[Render]: https://render.com
[waitress]: https://pypi.org/project/waitress/
[Flask]: https://pypi.org/project/Flask/
[Flask-RESTful]: https://pypi.org/project/Flask-RESTful/
[Flask-Caching]: https://pypi.org/project/Flask-Caching/
[Flask-Limiter]: https://pypi.org/project/Flask-Limiter/
[Redis]: https://pypi.org/project/redis/
[Memcached]: https://pypi.org/project/pymemcache/
[VSCode]: https://code.visualstudio.com/
[MIT License]: https://opensource.org/license/mit
[CVE-2026-27205]: https://nvd.nist.gov/vuln/detail/CVE-2026-27205
[CVE-2023-30861]: https://nvd.nist.gov/vuln/detail/cve-2023-30861
[CVE-2024-49768]: https://nvd.nist.gov/vuln/detail/CVE-2024-49768