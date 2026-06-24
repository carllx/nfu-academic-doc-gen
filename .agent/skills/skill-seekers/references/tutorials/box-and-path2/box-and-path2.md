# How To: Box And Path2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Edge betweenness subset centrality: box and path multiple target

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Edge betweenness subset centrality: box and path multiple target'

```python
'Edge betweenness subset centrality: box and path multiple target'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (1, 2), (2, 3), (1, 20), (20, 3), (3, 4)])
```

### Step 4: Assign b_answer = dict.fromkeys(...)

```python
b_answer = dict.fromkeys(G.edges(), 0)
```

### Step 5: Assign unknown = 1.0

```python
b_answer[0, 1] = 1.0
```

### Step 6: Assign unknown, unknown = 0.5

```python
b_answer[1, 20] = b_answer[3, 20] = 0.5
```

### Step 7: Assign unknown, unknown = 0.5

```python
b_answer[1, 2] = b_answer[2, 3] = 0.5
```

### Step 8: Assign unknown = 0.5

```python
b_answer[3, 4] = 0.5
```

### Step 9: Assign b = nx.edge_betweenness_centrality_subset(...)

```python
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3, 4], weight=None)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Edge betweenness subset centrality: box and path multiple target'
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (1, 20), (20, 3), (3, 4)])
b_answer = dict.fromkeys(G.edges(), 0)
b_answer[0, 1] = 1.0
b_answer[1, 20] = b_answer[3, 20] = 0.5
b_answer[1, 2] = b_answer[2, 3] = 0.5
b_answer[3, 4] = 0.5
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3, 4], weight=None)
for n in sorted(G.edges()):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality_subset.py:241 | Complexity: Advanced | Last updated: 2026-06-02*