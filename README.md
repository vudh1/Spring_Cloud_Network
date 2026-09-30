# Spring Cloud Config Network

A small two-service Spring Boot project demonstrating centralized configuration with **Spring Cloud Config**.

## Architecture

```text
config-repo/application.properties
              |
              v
     Config Server :8800
              |
              v
       Config Client :8801
              |
              v
 GET /config/max-attempts  ->  5
```

- `springcloudServer/` runs a Config Server.
- `config-repo/` contains the configuration served by the server.
- `springcloudClient/` loads that remote configuration during startup and exposes it through a REST endpoint.

The project intentionally uses the original Spring Boot 2.1 / Spring Cloud Greenwich generation it was created with.

## Run

Use two terminals from the repository root.

### 1. Start the Config Server

```bash
cd springcloudServer
./mvnw spring-boot:run
```

Verify it:

```bash
curl http://localhost:8800/application/default
```

### 2. Start the client

```bash
cd springcloudClient
./mvnw spring-boot:run
```

Then:

```bash
curl http://localhost:8801/config/max-attempts
```

Expected output:

```text
5
```

The original `/getCronformat` route is kept as an alias for compatibility.

## Change configuration

Edit:

```text
config-repo/application.properties
```

For a running client, the project also exposes the Spring Actuator refresh endpoint. In production, actuator endpoints should be secured appropriately.

## Test

Both Maven projects are compiled in CI, then the workflow starts the server and client and performs an HTTP smoke test across the full configuration path.
