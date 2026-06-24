# How To: Attnamestrange Timdelta Zero Timerespecting Returnstrue

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test attNameStrange timdelta zero timeRespecting returnsTrue

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
assert gm.subgraph_is_isomorphic()
```

### Step 2: Assign temporal_name = 'strange_name'

```python
temporal_name = 'strange_name'
```

### Step 3: Assign G1 = put_same_time(...)

```python
G1 = put_same_time(G1, temporal_name)
```

### Step 4: Assign G2 = self.provide_g2_path_3edges(...)

```python
G2 = self.provide_g2_path_3edges()
```

### Step 5: Assign d = timedelta(...)

```python
d = timedelta()
```

### Step 6: Assign gm = iso.TimeRespectingGraphMatcher(...)

```python
gm = iso.TimeRespectingGraphMatcher(G1, G2, temporal_name, d)
```

**Verification:**
```python
assert gm.subgraph_is_isomorphic()
```


## Complete Example

```python
# Workflow
G1 = self.provide_g1_topology()
temporal_name = 'strange_name'
G1 = put_same_time(G1, temporal_name)
G2 = self.provide_g2_path_3edges()
d = timedelta()
gm = iso.TimeRespectingGraphMatcher(G1, G2, temporal_name, d)
assert gm.subgraph_is_isomorphic()
```

## Next Steps


---

*Source: test_temporalisomorphvf2.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*