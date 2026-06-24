# How To: Random Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random graph

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
assert len(G) == 30
```

### Step 2: Assign m = 20

```python
m = 20
```

**Verification:**
```python
assert nx.is_bipartite(G)
```

### Step 3: Assign G = random_graph(...)

```python
G = random_graph(n, m, 0.9)
```

**Verification:**
```python
assert set(range(n)) == X
```

### Step 4: Assign unknown = nx.algorithms.bipartite.sets(...)

```python
X, Y = nx.algorithms.bipartite.sets(G)
```

**Verification:**
```python
assert set(range(n, n + m)) == Y
```


## Complete Example

```python
# Workflow
n = 10
m = 20
G = random_graph(n, m, 0.9)
assert len(G) == 30
assert nx.is_bipartite(G)
X, Y = nx.algorithms.bipartite.sets(G)
assert set(range(n)) == X
assert set(range(n, n + m)) == Y
```

## Next Steps


---

*Source: test_generators.py:354 | Complexity: Intermediate | Last updated: 2026-06-02*