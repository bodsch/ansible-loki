
# `loki_config_ruler`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#ruler_config)

## defaults

```yaml
loki_config_ruler:
  storage:
    type: local
    local:
      directory: "{{ loki_storage_dir }}/rules"
  rule_path: "{{ loki_storage_dir }}/rules-scratch"
  # alertmanager_url: http://localhost
  ring:
    kvstore:
      store: inmemory
  enable_api: true
```
