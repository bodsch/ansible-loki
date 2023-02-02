
# `loki_config_server`

The server block configures the HTTP and gRPC server communication of the launched service(s).

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#server_config)

## defaults

```yaml
loki_config_server:
  http_listen_address: "127.0.0.1"
  http_listen_port: 3100
  # [debug, info, warn, error] (default info)
  log_level: info
```
