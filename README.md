
# Ansible Role:  `loki`

Ansible role to setup [Loki](https://github.com/grafana/loki).


[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-loki)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-loki)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-loki)][releases]

[ci]: https://github.com/bodsch/ansible-loki/actions
[issues]: https://github.com/bodsch/ansible-loki/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-loki/releases


If `latest` is set for `loki_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/loki/${loki_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The Prometheus archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/loki`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `loki_direct_download` to `true`.



## Requirements & Dependencies

- None

### Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10
* RedHat based
    - Alma Linux 8
    - Rocky Linux 8
    - Oracle Linux 8

## usage

Upstream configuration examples can be found in the [Configuration Examples](https://grafana.com/docs/loki/latest/configuration/examples/) document.

For config upgrades [read](https://grafana.com/docs/loki/latest/upgrading)!


### default configuration

```yaml
loki_version: "2.6.1"
loki_release_download_url: https://github.com/grafana/loki/releases

loki_system_user: loki
loki_system_group: loki
loki_config_dir: /etc/loki
loki_storage_dir: /var/lib/loki

loki_direct_download: false

loki_targets:
  - all
loki_auth_enabled: false

loki_config_server: {}

loki_config_distributor: {}

loki_config_querier: {}

loki_config_ingester: {}

loki_config_ingester_client: {}

loki_config_storage: {}

loki_config_chunk_store: {}

loki_config_schema: {}

loki_config_limits: {}

loki_config_frontend_worker: {}

loki_config_runtime: {}

loki_config_table_manager: {}

loki_config_memberlist: {}

loki_config_compactor: {}

loki_config_ruler: {}
```

### `loki_targets`

A list of components to run.  
The default value `all` runs Loki in single binary mode.  
The value `read` is an alias to run only read-path related components such as the querier and query-frontend, but all in the same process.
The value `write` is an alias to run only write-path related components such as the distributor and compactor, but all in the same process.

Supported values: 
  `all`, `compactor`, `distributor`, `ingester`, `querier`, `query-scheduler`,
 `ingester-querier`, `query-frontend`, `index-gateway`, `ruler`, `table-manager`, `read`, `write`.

### `loki_auth_enabled`

#### defaults

```yaml
loki_auth_enabled: false
```

### `loki_config_server`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#server_config)

#### defaults

```yaml
loki_config_server:
  http_listen_address: "127.0.0.1"
  http_listen_port: 3100
  # [debug, info, warn, error] (default info)
  log_level: info
```

### `loki_config_distributor`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#distributor_config)

#### defaults

```yaml
loki_config_distributor:
  ring:
    kvstore:
      store: inmemory
```
### `loki_config_querier`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#querier_config)

#### defaults

```yaml
loki_config_querier: {}
```

### `loki_config_ingester`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#ingester_config)

#### defaults

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

### `loki_config_ingester_client`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#ingester_client_config)

#### defaults

```yaml
loki_config_ingester_client: {}
```

### `loki_config_storage`


[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#local_storage_config)

see also:

- [azure storage](https://grafana.com/docs/loki/latest/configuration/#azure_storage_config)
- [gcs storage](https://grafana.com/docs/loki/latest/configuration/#gcs_storage_config)
- [s3 storage](https://grafana.com/docs/loki/latest/configuration/#s3_storage_config)
- [swift storage](https://grafana.com/docs/loki/latest/configuration/#swift_storage_config)

#### defaults

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

### `loki_config_chunk_store`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#chunk_store_config)

#### defaults

```yaml
loki_config_chunk_store: {}
```

### `loki_config_schema`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#schema_config)

#### defaults

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

### `loki_config_limits`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#limits_config)

#### defaults

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

### `loki_config_frontend_worker`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#frontend_worker_config)

#### defaults

```yaml
loki_config_frontend_worker: {}
```

### `loki_config_runtime`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#runtime-configuration-file)

#### defaults

```yaml
loki_config_runtime: {}
```

### `loki_config_table_manager`

only for version <= 2.3!

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#table_manager_config)

#### defaults

```yaml
loki_config_table_manager: {}
```

### `loki_config_memberlist`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#memberlist_config)

#### defaults

```yaml
loki_config_memberlist: {}
```

### `loki_config_compactor`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#compactor_config)

#### defaults

```yaml
loki_config_compactor:
  working_directory: "{{ loki_storage_dir }}/compactor"
  shared_store: filesystem
  compaction_interval: 5m
```

### `loki_config_ruler`

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#ruler_config)

#### defaults

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

## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-loki/-/tags)!

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
