
# Ansible Role:  `loki`

Ansible role to setup [Loki](https://github.com/grafana/loki).


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-loki/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-loki)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-loki)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-loki/actions
[issues]: https://github.com/bodsch/ansible-loki/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-loki/releases
[quality]: https://galaxy.ansible.com/bodsch/loki


If `latest` is set for `loki_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/loki/${loki_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The Loki archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/loki`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `loki_direct_download` to `true`.



## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)
- [bodsch.scm](https://github.com/bodsch/ansible-collection-scm)

```bash
ansible-galaxy collection install bodsch.core
ansible-galaxy collection install bodsch.scm
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

### Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11 / 12
    - Ubuntu 20.04 / 22.04

> **RedHat-based systems are no longer officially supported! May work, but does not have to.**


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

loki_config_common: {}

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
The value `read` is an alias to run only read-path related components such as the `querier` and `query-frontend`, but all in the same process.
The value `write` is an alias to run only write-path related components such as the `distributor` and `compactor`, but all in the same process.

Supported values: 
  `all`, `compactor`, `distributor`, `ingester`, `querier`, `query-scheduler`,
 `ingester-querier`, `query-frontend`, `index-gateway`, `ruler`, `table-manager`, `read`, `write`.

### `loki_auth_enabled`

#### defaults

```yaml
loki_auth_enabled: false
```

### `loki_config_service`

Values to configure the service directly.  
Only values that are not listed in the configuration file are defined here.

```yaml
loki_config_service:
  validation:
    create_grace_period: ""
    enforce_metric_name: ""
    increment_duplicate_timestamps: ""
    max_entries_limit: ""
    max_label_names_per_series: ""
    max_length_label_name: ""
    reject_old_samples: ""
    reject_old_samples_max_age: ""
```

for more, [see](docs).

---

## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-loki/tags)!

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**
