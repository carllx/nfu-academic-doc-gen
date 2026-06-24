# How To: Timdelta One Config1 Returns Four Embedding

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timdelta one config1 returns four embedding

## Prerequisites

**Required Modules:**
- `datetime`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign G1 = self.provide_g1_topology(...)

```python
G1 = self.provide_g1_topology()
```

**Verification:**
```python
assert count_match == 4
```

### Step 2: Assign temporal_name = 'date'

```python
temporal_name = 'date'
```

### Step 3: Assign G1 = put_time_config_1(...)

```python
G1 = put_time_config_1(G1, temporal_name)
```

### Step 4: Assign G2 = self.provide_g2_path_3edges(...)

```python
G2 = self.provide_g2_path_3edges()
```

### Step 5: Assign d = timedelta(...)

```python
d = timedelta(days=1)
```

### Step 6: Assign gm = iso.TimeRespectingGraphMatcher(...)

```python
gm = iso.TimeRespectingGraphMatcher(G1, G2, temporal_name, d)
```

### Step 7: Assign count_match = len(...)

```python
count_match = len(list(gm.subgraph_isomorphisms_iter()))
```

**Verification:**
```python
assert count_match == 4
```


## Complete Example

```python
# Workflow
G1 = self.provide_g1_topology()
temporal_name = 'date'
G1 = put_time_config_1(G1, temporal_name)
G2 = self.provide_g2_path_3edges()
d = timedelta(days=1)
gm = iso.TimeRespectingGraphMatcher(G1, G2, temporal_name, d)
count_match = len(list(gm.subgraph_isomorphisms_iter()))
assert count_match == 4
```

## Next Steps


---

*Source: test_temporalisomorphvf2.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*