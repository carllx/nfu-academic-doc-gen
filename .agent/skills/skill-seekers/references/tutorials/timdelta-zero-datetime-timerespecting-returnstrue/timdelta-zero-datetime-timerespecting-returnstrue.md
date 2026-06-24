# How To: Timdelta Zero Datetime Timerespecting Returnstrue

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timdelta zero datetime timeRespecting returnsTrue

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

### Step 2: Assign temporal_name = 'date'

```python
temporal_name = 'date'
```

### Step 3: Assign G1 = put_same_datetime(...)

```python
G1 = put_same_datetime(G1, temporal_name)
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
temporal_name = 'date'
G1 = put_same_datetime(G1, temporal_name)
G2 = self.provide_g2_path_3edges()
d = timedelta()
gm = iso.TimeRespectingGraphMatcher(G1, G2, temporal_name, d)
assert gm.subgraph_is_isomorphic()
```

## Next Steps


---

*Source: test_temporalisomorphvf2.py:92 | Complexity: Intermediate | Last updated: 2026-06-02*