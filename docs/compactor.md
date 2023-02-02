
# `loki_config_compactor`

The compactor block configures the compactor component.  
This component periodically compacts index shards to more performant forms.

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#compactor_config)

## defaults

```yaml
loki_config_compactor:
  working_directory: "{{ loki_storage_dir }}/compactor"
  shared_store: filesystem
  compaction_interval: 5m
```
