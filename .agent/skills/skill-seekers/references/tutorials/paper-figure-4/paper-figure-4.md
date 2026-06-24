# How To: Paper Figure 4

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test paper figure 4

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert sorted(clique_sizes) == clique_sizes
```

### Step 2: Assign edges_fig_4 = value

```python
edges_fig_4 = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e'), ('d', 'e'), ('f', 'b'), ('f', 'c'), ('f', 'g'), ('g', 'f'), ('g', 'c'), ('g', 'd'), ('g', 'e')]
```

**Verification:**
```python
assert sorted(map(sorted, cliques)) == sorted(map(sorted, expected_cliques))
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(edges_fig_4)
```

### Step 4: Assign cliques = list(...)

```python
cliques = list(nx.enumerate_all_cliques(G))
```

### Step 5: Assign clique_sizes = list(...)

```python
clique_sizes = list(map(len, cliques))
```

**Verification:**
```python
assert sorted(clique_sizes) == clique_sizes
```

### Step 6: Assign expected_cliques = value

```python
expected_cliques = [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['a', 'b'], ['a', 'b', 'd'], ['a', 'b', 'd', 'e'], ['a', 'b', 'e'], ['a', 'c'], ['a', 'c', 'd'], ['a', 'c', 'd', 'e'], ['a', 'c', 'e'], ['a', 'd'], ['a', 'd', 'e'], ['a', 'e'], ['b', 'c'], ['b', 'c', 'd'], ['b', 'c', 'd', 'e'], ['b', 'c', 'e'], ['b', 'c', 'f'], ['b', 'd'], ['b', 'd', 'e'], ['b', 'e'], ['b', 'f'], ['c', 'd'], ['c', 'd', 'e'], ['c', 'd', 'e', 'g'], ['c', 'd', 'g'], ['c', 'e'], ['c', 'e', 'g'], ['c', 'f'], ['c', 'f', 'g'], ['c', 'g'], ['d', 'e'], ['d', 'e', 'g'], ['d', 'g'], ['e', 'g'], ['f', 'g'], ['a', 'b', 'c'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'e']]
```

**Verification:**
```python
assert sorted(map(sorted, cliques)) == sorted(map(sorted, expected_cliques))
```


## Complete Example

```python
# Workflow
G = nx.Graph()
edges_fig_4 = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'd'), ('c', 'e'), ('d', 'e'), ('f', 'b'), ('f', 'c'), ('f', 'g'), ('g', 'f'), ('g', 'c'), ('g', 'd'), ('g', 'e')]
G.add_edges_from(edges_fig_4)
cliques = list(nx.enumerate_all_cliques(G))
clique_sizes = list(map(len, cliques))
assert sorted(clique_sizes) == clique_sizes
expected_cliques = [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['a', 'b'], ['a', 'b', 'd'], ['a', 'b', 'd', 'e'], ['a', 'b', 'e'], ['a', 'c'], ['a', 'c', 'd'], ['a', 'c', 'd', 'e'], ['a', 'c', 'e'], ['a', 'd'], ['a', 'd', 'e'], ['a', 'e'], ['b', 'c'], ['b', 'c', 'd'], ['b', 'c', 'd', 'e'], ['b', 'c', 'e'], ['b', 'c', 'f'], ['b', 'd'], ['b', 'd', 'e'], ['b', 'e'], ['b', 'f'], ['c', 'd'], ['c', 'd', 'e'], ['c', 'd', 'e', 'g'], ['c', 'd', 'g'], ['c', 'e'], ['c', 'e', 'g'], ['c', 'f'], ['c', 'f', 'g'], ['c', 'g'], ['d', 'e'], ['d', 'e', 'g'], ['d', 'g'], ['e', 'g'], ['f', 'g'], ['a', 'b', 'c'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'c', 'e']]
assert sorted(map(sorted, cliques)) == sorted(map(sorted, expected_cliques))
```

## Next Steps


---

*Source: test_clique.py:222 | Complexity: Intermediate | Last updated: 2026-06-02*