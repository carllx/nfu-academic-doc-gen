# How To: Bipartite Density

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bipartite density

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(5)
```

**Verification:**
```python
assert bipartite.density(G, X) == density
```

### Step 2: Assign unknown = bipartite.sets(...)

```python
X, Y = bipartite.sets(G)
```

**Verification:**
```python
assert bipartite.density(D, X) == density / 2.0
```

### Step 3: Assign density = value

```python
density = len(list(G.edges())) / (len(X) * len(Y))
```

**Verification:**
```python
assert bipartite.density(nx.Graph(), {}) == 0.0
```

### Step 4: Assign D = nx.DiGraph(...)

```python
D = nx.DiGraph(G.edges())
```

**Verification:**
```python
assert bipartite.density(D, X) == density / 2.0
```


## Complete Example

```python
# Workflow
G = nx.path_graph(5)
X, Y = bipartite.sets(G)
density = len(list(G.edges())) / (len(X) * len(Y))
assert bipartite.density(G, X) == density
D = nx.DiGraph(G.edges())
assert bipartite.density(D, X) == density / 2.0
assert bipartite.density(nx.Graph(), {}) == 0.0
```

## Next Steps


---

*Source: test_basic.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*