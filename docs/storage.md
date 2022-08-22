
# `loki_config_storage`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#local_storage_config)

see also:

- [azure storage](https://grafana.com/docs/loki/latest/configuration/#azure_storage_config)
- [gcs storage](https://grafana.com/docs/loki/latest/configuration/#gcs_storage_config)
- [s3 storage](https://grafana.com/docs/loki/latest/configuration/#s3_storage_config)
- [swift storage](https://grafana.com/docs/loki/latest/configuration/#swift_storage_config)

## defaults

```yaml
loki_config_storage:
  boltdb_shipper:
    active_index_directory: "{{ loki_storage_dir }}/boltdb-shipper-active"
    cache_location: "{{ loki_storage_dir }}/boltdb-shipper-cache"
    # Can be increased for faster performance over longer query periods, uses more disk space
    cache_ttl: 24h
    shared_store: filesystem
  boltdb:
    directory: "{{ loki_storage_dir }}/index"
  filesystem:
    directory: "{{ loki_storage_dir }}/chunks"
```
