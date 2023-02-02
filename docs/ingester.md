
# `loki_config_ingester`

The ingester block configures the Loki Ingesters.

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#ingester_config)

## defaults

```yaml
loki_config_ingester:
  lifecycler:
    ring:
      kvstore:
        store: inmemory
      replication_factor: 1
    final_sleep: 0s
  # All chunks will be flushed when they hit this age, default is 1h
  max_chunk_age: 1h
  # Chunk transfers disabled
  max_transfer_retries: 0
  chunk_block_size: 262144
  # Any chunk not receiving new logs in this time will be flushed
  chunk_idle_period: 30m
  # Must be greater than index read cache TTL
  # if using an index cache (Default index read cache TTL is 5m)
  chunk_retain_period: 15m
  # Loki will attempt to build chunks up to 1.5MB,
  # flushing first if chunk_idle_period or max_chunk_age is reached first
  chunk_target_size: 1572864
  wal:
    dir: "{{ loki_storage_dir }}/wal"
    enabled: true
```
