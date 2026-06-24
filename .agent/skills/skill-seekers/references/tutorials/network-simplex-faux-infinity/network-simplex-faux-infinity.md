# How To: Network Simplex Faux Infinity

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: network_simplex should not raise an exception as a result of faux_infinity
for these cases. See gh-7562

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: faux_inf_example, large_capacity, large_demand, large_weight
```

## Step-by-Step Guide

### Step 1: 'network_simplex should not raise an exception as a result of faux_infinity\n    for these cases. See gh-7562'

```python
'network_simplex should not raise an exception as a result of faux_infinity\n    for these cases. See gh-7562'
```

### Step 2: Assign G = faux_inf_example

```python
G = faux_inf_example
```

### Step 3: Assign lv = 1000000000

```python
lv = 1000000000
```

### Step 4: Assign unknown = nx.network_simplex(...)

```python
fc, fd = nx.network_simplex(G)
```

### Step 5: Assign unknown = lv

```python
G['s0']['ns']['capacity'] = lv
```

### Step 6: Assign unknown = value

```python
G.nodes['s0']['demand'] = -lv
```

### Step 7: Assign unknown = lv

```python
G.nodes['c1']['demand'] = lv
```

### Step 8: Assign unknown = lv

```python
G['s1']['ns']['weight'] = lv
```


## Complete Example

```python
# Setup
# Fixtures: faux_inf_example, large_capacity, large_demand, large_weight

# Workflow
'network_simplex should not raise an exception as a result of faux_infinity\n    for these cases. See gh-7562'
G = faux_inf_example
lv = 1000000000
if large_capacity:
    G['s0']['ns']['capacity'] = lv
if large_demand:
    G.nodes['s0']['demand'] = -lv
    G.nodes['c1']['demand'] = lv
if large_weight:
    G['s1']['ns']['weight'] = lv
fc, fd = nx.network_simplex(G)
```

## Next Steps


---

*Source: test_networksimplex.py:445 | Complexity: Advanced | Last updated: 2026-06-02*