
# `loki_config_memberlist`

The memberlist_config block configures the gossip ring to discover and connect between distributors, 
ingesters and queriers. The configuration is unique for all three components to ensure a single shared ring.

When a memberlist_config with least 1 join_members is defined, a kvstore of type memberlist is 
automatically configured for the distributor, ingester, and ruler rings unless otherwise specified in 
those components specific configuration sections.

[upstream configuration](https://grafana.com/docs/loki/latest/configuration/#memberlist_config)

## defaults

```yaml
loki_config_memberlist: {}
```
