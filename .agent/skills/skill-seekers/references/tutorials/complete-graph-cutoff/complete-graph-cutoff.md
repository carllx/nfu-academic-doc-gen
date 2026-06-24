# How To: Complete Graph Cutoff

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete graph cutoff

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert cutoff == result, f'cutoff error in {flow_func.__name__}'
```

### Step 2: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(u, v): 1 for u, v in G.edges()}, 'capacity')
```

### Step 3: Assign result = nx.maximum_flow_value(...)

```python
result = nx.maximum_flow_value(G, 0, 4, flow_func=flow_func, cutoff=cutoff)
```

**Verification:**
```python
assert cutoff == result, f'cutoff error in {flow_func.__name__}'
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(5)
nx.set_edge_attributes(G, {(u, v): 1 for u, v in G.edges()}, 'capacity')
for flow_func in [shortest_augmenting_path, edmonds_karp, dinitz, boykov_kolmogorov]:
    for cutoff in [3, 2, 1]:
        result = nx.maximum_flow_value(G, 0, 4, flow_func=flow_func, cutoff=cutoff)
        assert cutoff == result, f'cutoff error in {flow_func.__name__}'
```

## Next Steps


---

*Source: test_maxflow.py:560 | Complexity: Beginner | Last updated: 2026-06-02*