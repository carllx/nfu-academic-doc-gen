# How To: Greedy Modularity Communities Directed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test greedy modularity communities directed

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('d', 'e'), ('d', 'f'), ('d', 'g'), ('f', 'g'), ('d', 'e'), ('f', 'e')])
```

**Verification:**
```python
assert greedy_modularity_communities(G) == expected
```

### Step 2: Assign expected = value

```python
expected = [frozenset({'f', 'g', 'e', 'd'}), frozenset({'a', 'b', 'c'})]
```

**Verification:**
```python
assert greedy_modularity_communities(G) == expected
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 4: Call G.add_edges_from()

```python
G.add_edges_from([(1, 1), (1, 2), (1, 3), (2, 3), (1, 4), (4, 4), (5, 5), (4, 5), (4, 6), (5, 6)])
```

### Step 5: Assign expected = value

```python
expected = [frozenset({1, 2, 3}), frozenset({4, 5, 6})]
```

**Verification:**
```python
assert greedy_modularity_communities(G) == expected
```


## Complete Example

```python
# Workflow
G = nx.DiGraph([('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('d', 'e'), ('d', 'f'), ('d', 'g'), ('f', 'g'), ('d', 'e'), ('f', 'e')])
expected = [frozenset({'f', 'g', 'e', 'd'}), frozenset({'a', 'b', 'c'})]
assert greedy_modularity_communities(G) == expected
G = nx.DiGraph()
G.add_edges_from([(1, 1), (1, 2), (1, 3), (2, 3), (1, 4), (4, 4), (5, 5), (4, 5), (4, 6), (5, 6)])
expected = [frozenset({1, 2, 3}), frozenset({4, 5, 6})]
assert greedy_modularity_communities(G) == expected
```

## Next Steps


---

*Source: test_modularity_max.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*