# How To: Flow Func Not Callable

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test flow func not callable

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign elements = value

```python
elements = ['this_should_be_callable', 10, {1, 2, 3}]
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([(0, 1, 1), (1, 2, 1), (2, 3, 1)], weight='capacity')
```

### Step 4: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, flow_func, G, 0, 1, flow_func=element)
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, flow_func, G, 0, 1, flow_func=element)
```


## Complete Example

```python
# Workflow
elements = ['this_should_be_callable', 10, {1, 2, 3}]
G = nx.Graph()
G.add_weighted_edges_from([(0, 1, 1), (1, 2, 1), (2, 3, 1)], weight='capacity')
for flow_func in interface_funcs:
    for element in elements:
        pytest.raises(nx.NetworkXError, flow_func, G, 0, 1, flow_func=element)
        pytest.raises(nx.NetworkXError, flow_func, G, 0, 1, flow_func=element)
```

## Next Steps


---

*Source: test_maxflow.py:419 | Complexity: Intermediate | Last updated: 2026-06-02*