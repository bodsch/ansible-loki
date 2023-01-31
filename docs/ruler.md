
# `loki_config_ruler`

The ruler block configures the Loki ruler.

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
      # Backend storage to use for the ring. 
      #   Supported values are: consul, etcd, inmemory, memberlist, multi.
      store: inmemory
  enable_api: true
```
