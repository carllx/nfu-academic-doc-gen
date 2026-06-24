# How To: Box

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Edge betweenness subset centrality: box

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Edge betweenness subset centrality: box'

```python
'Edge betweenness subset centrality: box'
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
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
```

### Step 4: Assign b_answer = dict.fromkeys(...)

```python
b_answer = dict.fromkeys(G.edges(), 0)
```

### Step 5: Assign unknown, unknown = 0.25

```python
b_answer[0, 1] = b_answer[0, 2] = 0.25
```

### Step 6: Assign unknown, unknown = 0.25

```python
b_answer[1, 3] = b_answer[2, 3] = 0.25
```

### Step 7: Assign b = nx.edge_betweenness_centrality_subset(...)

```python
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3], weight=None)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Edge betweenness subset centrality: box'
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
b_answer = dict.fromkeys(G.edges(), 0)
b_answer[0, 1] = b_answer[0, 2] = 0.25
b_answer[1, 3] = b_answer[2, 3] = 0.25
b = nx.edge_betweenness_centrality_subset(G, sources=[0], targets=[3], weight=None)
for n in sorted(G.edges()):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality_subset.py:214 | Complexity: Intermediate | Last updated: 2026-06-02*