# How To: Preflow Push Makes Enough Space

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test preflow push makes enough space

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

### Step 2: Call nx.add_path()

```python
nx.add_path(G, [0, 1, 3], capacity=1)
```

### Step 3: Call nx.add_path()

```python
nx.add_path(G, [1, 2, 3], capacity=1)
```

### Step 4: Assign R = preflow_push(...)

```python
R = preflow_push(G, 0, 3, value_only=False)
```

**Verification:**
```python
assert R.graph['flow_value'] == 1
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
nx.add_path(G, [0, 1, 3], capacity=1)
nx.add_path(G, [1, 2, 3], capacity=1)
R = preflow_push(G, 0, 3, value_only=False)
assert R.graph['flow_value'] == 1
```

## Next Steps


---

*Source: test_maxflow.py:517 | Complexity: Intermediate | Last updated: 2026-06-02*