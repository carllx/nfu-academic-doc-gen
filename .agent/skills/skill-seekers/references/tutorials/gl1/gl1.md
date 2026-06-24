# How To: Gl1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gl1

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
G = read_graph('gl1')
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

### Step 6: Assign flow_func = value

```python
flow_func = flow_funcs[0]
```

### Step 7: Call validate_flows()

```python
validate_flows(G, s, t, 156545, flow_func(G, s, t, **kwargs), flow_func)
```


## Complete Example

```python
# Workflow
G = read_graph('gl1')
s = 1
t = len(G)
R = build_residual_network(G, 'capacity')
kwargs = {'residual': R}
flow_func = flow_funcs[0]
validate_flows(G, s, t, 156545, flow_func(G, s, t, **kwargs), flow_func)
```

## Next Steps


---

*Source: test_maxflow_large_graph.py:111 | Complexity: Intermediate | Last updated: 2026-06-02*