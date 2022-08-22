
# `loki_config_schema`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#schema_config)

## defaults

```yaml
loki_config_schema:
  configs:
    - from: "2020-10-24"
      store: boltdb
      object_store: filesystem
      schema: v11
      index:
        prefix: index_
        period: 168h
      chunks:
        prefix: index_
        period: 168h
      row_shards: 16
```
