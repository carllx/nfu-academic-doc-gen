# How To: Flow Func Parameters

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test flow func parameters

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

### Step 3: Assign errmsg = value

```python
errmsg = f'Assertion failed in function: {flow_func.__name__} in interface {interface_func.__name__}'
```

### Step 4: Assign result = interface_func(...)

```python
result = interface_func(G, 'x', 'y', flow_func=flow_func)
```

**Verification:**
```python
assert fv == result, errmsg
```

### Step 5: Assign result = value

```python
result = result[0]
```


## Complete Example

```python
# Workflow
G = self.G
fv = 3.0
for interface_func in interface_funcs:
    for flow_func in flow_funcs:
        errmsg = f'Assertion failed in function: {flow_func.__name__} in interface {interface_func.__name__}'
        result = interface_func(G, 'x', 'y', flow_func=flow_func)
        if interface_func in max_min_funcs:
            result = result[0]
        assert fv == result, errmsg
```

## Next Steps


---

*Source: test_maxflow.py:428 | Complexity: Intermediate | Last updated: 2026-06-02*