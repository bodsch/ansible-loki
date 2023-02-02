
# `loki_config_limits`

The limits_config block configures global and per-tenant limits in Loki.

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#limits_config)

## defaults

```yaml
loki_config_limits:
  enforce_metric_name: false
  ingestion_burst_size_mb: 32
  ingestion_rate_mb: 16
  max_query_parallelism: 64
  max_streams_per_user: 0
  reject_old_samples: true
  reject_old_samples_max_age: 168h
```
