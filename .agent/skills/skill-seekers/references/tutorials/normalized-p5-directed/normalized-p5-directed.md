# How To: Normalized P5 Directed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Edge betweenness subset centrality: Normalized Directed P5

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Edge betweenness subset centrality: Normalized Directed P5'

```python
'Edge betweenness subset centrality: Normalized Directed P5'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call nx.add_path()

```python
nx.add_path(G, range(5))
```

### Step 4: Assign b_answer = dict.fromkeys(...)

```python
b_answer = dict.fromkeys(G.edges(), 0)
```

### Step 5: Assign unknown, unknown, unknown = 0.05

```python
b_answer[0, 1] = b_answer[1, 2] = b_answer[2, 3] = 0.05
```

### Step 6: Assign b = nx.edge_betweenness_centrality_subset(...)

```python
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3], normalized=True, weight=None)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Edge betweenness subset centrality: Normalized Directed P5'
G = nx.DiGraph()
nx.add_path(G, range(5))
b_answer = dict.fromkeys(G.edges(), 0)
b_answer[0, 1] = b_answer[1, 2] = b_answer[2, 3] = 0.05
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3], normalized=True, weight=None)
for n in G.edges():
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality_subset.py:308 | Complexity: Intermediate | Last updated: 2026-06-02*