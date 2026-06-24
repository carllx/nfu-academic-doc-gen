# How To: Weighted Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Edge betweenness centrality: weighted

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Edge betweenness centrality: weighted'

```python
'Edge betweenness centrality: weighted'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign eList = value

```python
eList = [(0, 1, 5), (0, 2, 4), (0, 3, 3), (0, 4, 2), (1, 2, 4), (1, 3, 1), (1, 4, 3), (2, 4, 5), (3, 4, 4)]
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 4: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from(eList)
```

### Step 5: Assign b = nx.edge_betweenness_centrality(...)

```python
b = nx.edge_betweenness_centrality(G, weight='weight', normalized=False)
```

### Step 6: Assign b_answer = value

```python
b_answer = {(0, 1): 0.0, (0, 2): 1.0, (0, 3): 2.0, (0, 4): 1.0, (1, 2): 2.0, (1, 3): 3.5, (1, 4): 1.5, (2, 4): 1.0, (3, 4): 0.5}
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Edge betweenness centrality: weighted'
eList = [(0, 1, 5), (0, 2, 4), (0, 3, 3), (0, 4, 2), (1, 2, 4), (1, 3, 1), (1, 4, 3), (2, 4, 5), (3, 4, 4)]
G = nx.Graph()
G.add_weighted_edges_from(eList)
b = nx.edge_betweenness_centrality(G, weight='weight', normalized=False)
b_answer = {(0, 1): 0.0, (0, 2): 1.0, (0, 3): 2.0, (0, 4): 1.0, (1, 2): 2.0, (1, 3): 3.5, (1, 4): 1.5, (2, 4): 1.0, (3, 4): 0.5}
for n in sorted(G.edges()):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

## Next Steps


---

*Source: test_betweenness_centrality.py:783 | Complexity: Intermediate | Last updated: 2026-06-02*