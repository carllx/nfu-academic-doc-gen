# How To: Ladder Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Weighted betweenness centrality: Ladder graph

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Weighted betweenness centrality: Ladder graph'

```python
'Weighted betweenness centrality: Ladder graph'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=0.001)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (4, 5), (3, 5)])
```

### Step 4: Assign b_answer = value

```python
b_answer = {0: 1.667, 1: 1.667, 2: 6.667, 3: 6.667, 4: 1.667, 5: 1.667}
```

### Step 5: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, weight='weight', normalized=False)
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=0.001)
```


## Complete Example

```python
# Workflow
'Weighted betweenness centrality: Ladder graph'
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (4, 5), (3, 5)])
b_answer = {0: 1.667, 1: 1.667, 2: 6.667, 3: 6.667, 4: 1.667, 5: 1.667}
for b in b_answer:
    b_answer[b] /= 2
b = nx.betweenness_centrality(G, weight='weight', normalized=False)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=0.001)
```

## Next Steps


---

*Source: test_betweenness_centrality.py:598 | Complexity: Intermediate | Last updated: 2026-06-02*