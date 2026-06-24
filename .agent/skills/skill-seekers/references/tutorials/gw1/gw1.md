# How To: Gw1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test gw1

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign G = read_graph(...)

```python
G = read_graph('gw1')
```

### Step 2: Assign s = 1

```python
s = 1
```

### Step 3: Assign t = len(...)

```python
t = len(G)
```

### Step 4: Assign R = build_residual_network(...)

```python
R = build_residual_network(G, 'capacity')
```

### Step 5: Assign kwargs = value

```python
kwargs = {'residual': R}
```

### Step 6: Call validate_flows()

```python
validate_flows(G, s, t, 1202018, flow_func(G, s, t, **kwargs), flow_func)
```


## Complete Example

```python
# Workflow
G = read_graph('gw1')
s = 1
t = len(G)
R = build_residual_network(G, 'capacity')
kwargs = {'residual': R}
for flow_func in flow_funcs:
    validate_flows(G, s, t, 1202018, flow_func(G, s, t, **kwargs), flow_func)
```

## Next Steps


---

*Source: test_maxflow_large_graph.py:127 | Complexity: Intermediate | Last updated: 2026-06-02*