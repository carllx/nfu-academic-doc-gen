# How To: Sample From P3

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Betweenness centrality: P3 sample

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Betweenness centrality: P3 sample'

```python
'Betweenness centrality: P3 sample'
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

**Verification:**
```python
assert b[n] in (b_approx1[n], b_approx2[n])
```

### Step 3: Assign b_answer = value

```python
b_answer = {0: 0.0, 1: 1.0, 2: 0.0}
```

### Step 4: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, k=3, weight=None, normalized=False, seed=1)
```

### Step 5: Assign b = nx.betweenness_centrality(...)

```python
b = nx.betweenness_centrality(G, k=2, weight=None, normalized=False, seed=1)
```

### Step 6: Assign b_approx1 = value

```python
b_approx1 = {0: 0.0, 1: 1.0, 2: 0.0}
```

### Step 7: Assign b_approx2 = value

```python
b_approx2 = {0: 0.0, 1: 0.5, 2: 0.0}
```

**Verification:**
```python
assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
```


## Complete Example

```python
# Workflow
'Betweenness centrality: P3 sample'
G = nx.path_graph(3)
b_answer = {0: 0.0, 1: 1.0, 2: 0.0}
b = nx.betweenness_centrality(G, k=3, weight=None, normalized=False, seed=1)
for n in sorted(G):
    assert b[n] == pytest.approx(b_answer[n], abs=1e-07)
b = nx.betweenness_centrality(G, k=2, weight=None, normalized=False, seed=1)
b_approx1 = {0: 0.0, 1: 1.0, 2: 0.0}
b_approx2 = {0: 0.0, 1: 0.5, 2: 0.0}
for n in sorted(G):
    assert b[n] in (b_approx1[n], b_approx2[n])
```

## Next Steps


---

*Source: test_betweenness_centrality.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*