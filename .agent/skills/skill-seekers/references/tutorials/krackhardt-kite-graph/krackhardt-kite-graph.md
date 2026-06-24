# How To: Krackhardt Kite Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Weighted betweenness centrality: Krackhardt kite graph

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Weighted betweenness centrality: Krackhardt kite graph'

```python
'Weighted betweenness centrality: Krackhardt kite graph'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=0.001)
```

### Step 2: Assign G = nx.krackhardt_kite_graph(...)

```python
G = nx.krackhardt_kite_graph()
```

### Step 3: Assign b_answer = value

```python
b_answer = {0: 1.667, 1: 1.667, 2: 0.0, 3: 7.333, 4: 0.0, 5: 16.667, 6: 16.667, 7: 28.0, 8: 16.0, 9: 0.0}
```

### Step 4: Assign b = nx.betweenness_centrality(...)

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
'Weighted betweenness centrality: Krackhardt kite graph'
G = nx.krackhardt_kite_graph()
b_answer = {0: 1.667, 1: 1.667, 2: 0.0, 3: 7.333, 4: 0.0, 5: 16.667, 6: 16.667, 7: 28.0, 8: 16.0, 9: 0.0}
for b in b_answer:
    b_answer[b] /= 2
b = nx.betweenness_centrality(G, weight='weight', normalized=False)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=0.001)
```

## Next Steps


---

*Source: test_betweenness_centrality.py:440 | Complexity: Intermediate | Last updated: 2026-06-02*