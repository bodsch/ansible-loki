
# `loki_config_compactor`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#compactor_config)

## defaults

```yaml
loki_config_compactor:
  working_directory: "{{ loki_storage_dir }}/compactor"
  shared_store: filesystem
  compaction_interval: 5m
```
