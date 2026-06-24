# How To: Preflow Push Global Relabel Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test preflow push global relabel freq

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert R.graph['flow_value'] == 1
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2, capacity=1)
```

### Step 3: Assign R = preflow_push(...)

```python
R = preflow_push(G, 1, 2, global_relabel_freq=None)
```

**Verification:**
```python
assert R.graph['flow_value'] == 1
```

### Step 4: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, preflow_push, G, 1, 2, global_relabel_freq=-1)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge(1, 2, capacity=1)
R = preflow_push(G, 1, 2, global_relabel_freq=None)
assert R.graph['flow_value'] == 1
pytest.raises(nx.NetworkXError, preflow_push, G, 1, 2, global_relabel_freq=-1)
```

## Next Steps


---

*Source: test_maxflow.py:509 | Complexity: Intermediate | Last updated: 2026-06-02*