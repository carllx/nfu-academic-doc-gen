# How To: Preflow Push Global Relabel

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test preflow push global relabel

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

**Verification:**
```python
assert R.graph['flow_value'] == 1202018
```

### Step 2: Assign R = preflow_push(...)

```python
R = preflow_push(G, 1, len(G), global_relabel_freq=50)
```

**Verification:**
```python
assert R.graph['flow_value'] == 1202018
```


## Complete Example

```python
# Workflow
G = read_graph('gw1')
R = preflow_push(G, 1, len(G), global_relabel_freq=50)
assert R.graph['flow_value'] == 1202018
```

## Next Steps


---

*Source: test_maxflow_large_graph.py:152 | Complexity: Beginner | Last updated: 2026-06-02*