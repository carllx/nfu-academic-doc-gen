# How To: Gnmk Random Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gnmk random graph

## Prerequisites

**Required Modules:**
- `numbers`
- `pytest`
- `networkx`
- `generators`


## Step-by-Step Guide

### Step 1: Assign n = 10

```python
n = 10
```

**Verification:**
```python
assert len(G) == n + m
```

### Step 2: Assign m = 20

```python
m = 20
```

**Verification:**
```python
assert nx.is_bipartite(G)
```

### Step 3: Assign edges = 100

```python
edges = 100
```

**Verification:**
```python
assert set(range(n)) == X
```

### Step 4: Assign G = gnmk_random_graph(...)

```python
G = gnmk_random_graph(n, m, edges, seed=1234)
```

**Verification:**
```python
assert set(range(n, n + m)) == Y
```

### Step 5: Assign unknown = nx.algorithms.bipartite.sets(...)

```python
X, Y = nx.algorithms.bipartite.sets(G)
```

**Verification:**
```python
assert edges == len(list(G.edges()))
```


## Complete Example

```python
# Workflow
n = 10
m = 20
edges = 100
G = gnmk_random_graph(n, m, edges, seed=1234)
assert len(G) == n + m
assert nx.is_bipartite(G)
X, Y = nx.algorithms.bipartite.sets(G)
assert set(range(n)) == X
assert set(range(n, n + m)) == Y
assert edges == len(list(G.edges()))
```

## Next Steps


---

*Source: test_generators.py:374 | Complexity: Intermediate | Last updated: 2026-06-02*