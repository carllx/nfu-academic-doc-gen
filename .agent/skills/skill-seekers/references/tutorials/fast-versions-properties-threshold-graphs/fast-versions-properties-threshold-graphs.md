# How To: Fast Versions Properties Threshold Graphs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fast versions properties threshold graphs

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Assign cs = 'ddiiddid'

```python
cs = 'ddiiddid'
```

**Verification:**
```python
assert nxt.density('ddiiddid') == nx.density(G)
```

### Step 2: Assign G = nxt.threshold_graph(...)

```python
G = nxt.threshold_graph(cs)
```

**Verification:**
```python
assert sorted(nxt.degree_sequence(cs)) == sorted((d for n, d in G.degree()))
```

### Step 3: Assign ts = nxt.triangle_sequence(...)

```python
ts = nxt.triangle_sequence(cs)
```

**Verification:**
```python
assert ts == list(nx.triangles(G).values())
```

### Step 4: Assign c1 = nxt.cluster_sequence(...)

```python
c1 = nxt.cluster_sequence(cs)
```

**Verification:**
```python
assert sum(ts) // 3 == nxt.triangles(cs)
```

### Step 5: Assign c2 = list(...)

```python
c2 = list(nx.clustering(G).values())
```

**Verification:**
```python
assert sum((abs(c - d) for c, d in zip(c1, c2))) == pytest.approx(0, abs=1e-07)
```

### Step 6: Assign b1 = nx.betweenness_centrality.values(...)

```python
b1 = nx.betweenness_centrality(G).values()
```

**Verification:**
```python
assert sum((abs(c - d) for c, d in zip(b1, b2))) < 1e-07
```

### Step 7: Assign b2 = nxt.betweenness_sequence(...)

```python
b2 = nxt.betweenness_sequence(cs)
```

**Verification:**
```python
assert nxt.eigenvalues(cs) == [0, 1, 3, 3, 5, 7, 7, 8]
```


## Complete Example

```python
# Workflow
cs = 'ddiiddid'
G = nxt.threshold_graph(cs)
assert nxt.density('ddiiddid') == nx.density(G)
assert sorted(nxt.degree_sequence(cs)) == sorted((d for n, d in G.degree()))
ts = nxt.triangle_sequence(cs)
assert ts == list(nx.triangles(G).values())
assert sum(ts) // 3 == nxt.triangles(cs)
c1 = nxt.cluster_sequence(cs)
c2 = list(nx.clustering(G).values())
assert sum((abs(c - d) for c, d in zip(c1, c2))) == pytest.approx(0, abs=1e-07)
b1 = nx.betweenness_centrality(G).values()
b2 = nxt.betweenness_sequence(cs)
assert sum((abs(c - d) for c, d in zip(b1, b2))) < 1e-07
assert nxt.eigenvalues(cs) == [0, 1, 3, 3, 5, 7, 7, 8]
assert abs(nxt.degree_correlation(cs) + 0.593038821954) < 1e-12
assert nxt.degree_correlation('diiiddi') == -0.8
assert nxt.degree_correlation('did') == -1.0
assert nxt.degree_correlation('ddd') == 1.0
assert nxt.eigenvalues('dddiii') == [0, 0, 0, 0, 3, 3]
assert nxt.eigenvalues('dddiiid') == [0, 1, 1, 1, 4, 4, 7]
```

## Next Steps


---

*Source: test_threshold.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*