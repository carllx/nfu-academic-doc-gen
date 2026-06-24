# How To: Pyramid

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pyramid

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign N = 10

```python
N = 10
```

**Verification:**
```python
assert flow_value == pytest.approx(1.0, abs=1e-07)
```

### Step 2: Assign G = gen_pyramid(...)

```python
G = gen_pyramid(N)
```

### Step 3: Assign R = build_residual_network(...)

```python
R = build_residual_network(G, 'capacity')
```

### Step 4: Assign kwargs = value

```python
kwargs = {'residual': R}
```

### Step 5: Assign unknown = flow_func

```python
kwargs['flow_func'] = flow_func
```

### Step 6: Assign errmsg = value

```python
errmsg = f'Assertion failed in function: {flow_func.__name__}'
```

### Step 7: Assign flow_value = nx.maximum_flow_value(...)

```python
flow_value = nx.maximum_flow_value(G, (0, 0), 't', **kwargs)
```

**Verification:**
```python
assert flow_value == pytest.approx(1.0, abs=1e-07)
```


## Complete Example

```python
# Workflow
N = 10
G = gen_pyramid(N)
R = build_residual_network(G, 'capacity')
kwargs = {'residual': R}
for flow_func in flow_funcs:
    kwargs['flow_func'] = flow_func
    errmsg = f'Assertion failed in function: {flow_func.__name__}'
    flow_value = nx.maximum_flow_value(G, (0, 0), 't', **kwargs)
    assert flow_value == pytest.approx(1.0, abs=1e-07)
```

## Next Steps


---

*Source: test_maxflow_large_graph.py:98 | Complexity: Intermediate | Last updated: 2026-06-02*