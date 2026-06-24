# How To: Diamond Multi Path

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Edge betweenness subset centrality: Diamond Multi Path

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Edge betweenness subset centrality: Diamond Multi Path'

```python
'Edge betweenness subset centrality: Diamond Multi Path'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[sort_n], abs=1e-07)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 10), (10, 11), (11, 12), (12, 9), (2, 6), (3, 6), (4, 6), (5, 7), (7, 8), (6, 8), (8, 9)])
```

### Step 4: Assign b_answer = dict.fromkeys(...)

```python
b_answer = dict.fromkeys(G.edges(), 0)
```

### Step 5: Assign unknown = 0.4

```python
b_answer[8, 9] = 0.4
```

### Step 6: Assign unknown, unknown = 0.2

```python
b_answer[6, 8] = b_answer[7, 8] = 0.2
```

### Step 7: Assign unknown, unknown, unknown = value

```python
b_answer[2, 6] = b_answer[3, 6] = b_answer[4, 6] = 0.2 / 3.0
```

### Step 8: Assign unknown, unknown, unknown = value

```python
b_answer[1, 2] = b_answer[1, 3] = b_answer[1, 4] = 0.2 / 3.0
```

### Step 9: Assign unknown = 0.2

```python
b_answer[5, 7] = 0.2
```

### Step 10: Assign unknown = 0.2

```python
b_answer[1, 5] = 0.2
```

### Step 11: Assign unknown = 0.1

```python
b_answer[9, 12] = 0.1
```

### Step 12: Assign unknown, unknown, unknown = 0.1

```python
b_answer[11, 12] = b_answer[10, 11] = b_answer[1, 10] = 0.1
```

### Step 13: Assign b = nx.edge_betweenness_centrality_subset(...)

```python
b = nx.edge_betweenness_centrality_subset(G, sources=[1], targets=[9], weight=None)
```

### Step 14: Assign sort_n = tuple(...)

```python
sort_n = tuple(sorted(n))
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[sort_n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Edge betweenness subset centrality: Diamond Multi Path'
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 10), (10, 11), (11, 12), (12, 9), (2, 6), (3, 6), (4, 6), (5, 7), (7, 8), (6, 8), (8, 9)])
b_answer = dict.fromkeys(G.edges(), 0)
b_answer[8, 9] = 0.4
b_answer[6, 8] = b_answer[7, 8] = 0.2
b_answer[2, 6] = b_answer[3, 6] = b_answer[4, 6] = 0.2 / 3.0
b_answer[1, 2] = b_answer[1, 3] = b_answer[1, 4] = 0.2 / 3.0
b_answer[5, 7] = 0.2
b_answer[1, 5] = 0.2
b_answer[9, 12] = 0.1
b_answer[11, 12] = b_answer[10, 11] = b_answer[1, 10] = 0.1
b = nx.edge_betweenness_centrality_subset(G, sources=[1], targets=[9], weight=None)
for n in G.edges():
    sort_n = tuple(sorted(n))
    assert b[n] == pytest.approx(b_answer[sort_n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality_subset.py:256 | Complexity: Advanced | Last updated: 2026-06-02*