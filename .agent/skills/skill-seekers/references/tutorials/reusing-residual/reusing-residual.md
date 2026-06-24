# How To: Reusing Residual

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reusing residual

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert fv == result, errmsg
```

### Step 2: Assign fv = 3.0

```python
fv = 3.0
```

### Step 3: Assign unknown = value

```python
s, t = ('x', 'y')
```

### Step 4: Assign R = build_residual_network(...)

```python
R = build_residual_network(G, 'capacity')
```

### Step 5: Assign errmsg = value

```python
errmsg = f'Assertion failed in function: {flow_func.__name__} in interface {interface_func.__name__}'
```

### Step 6: Assign result = interface_func(...)

```python
result = interface_func(G, 'x', 'y', flow_func=flow_func, residual=R)
```

**Verification:**
```python
assert fv == result, errmsg
```

### Step 7: Assign result = value

```python
result = result[0]
```


## Complete Example

```python
# Workflow
G = self.G
fv = 3.0
s, t = ('x', 'y')
R = build_residual_network(G, 'capacity')
for interface_func in interface_funcs:
    for flow_func in flow_funcs:
        errmsg = f'Assertion failed in function: {flow_func.__name__} in interface {interface_func.__name__}'
        for i in range(3):
            result = interface_func(G, 'x', 'y', flow_func=flow_func, residual=R)
            if interface_func in max_min_funcs:
                result = result[0]
            assert fv == result, errmsg
```

## Next Steps


---

*Source: test_maxflow.py:488 | Complexity: Intermediate | Last updated: 2026-06-02*