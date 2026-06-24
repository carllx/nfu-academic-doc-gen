# How To: Greedy Modularity Communities Multigraph Weighted

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test greedy modularity communities multigraph weighted

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```

### Step 2: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([(1, 2, 5), (1, 2, 3), (1, 3, 6), (1, 3, 6), (2, 3, 4), (1, 4, 1), (1, 4, 1), (2, 4, 3), (2, 4, 3), (4, 5, 1), (5, 6, 3), (5, 6, 7), (5, 6, 4), (5, 7, 9), (5, 7, 9), (6, 7, 8), (7, 8, 2), (7, 8, 2), (5, 8, 6), (5, 8, 6)])
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```

### Step 3: Assign expected = value

```python
expected = [frozenset({1, 2, 3, 4}), frozenset({5, 6, 7, 8})]
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```

### Step 4: Call G.add_edge()

```python
G.add_edge(4, 5, weight=16)
```

### Step 5: Assign expected = value

```python
expected = [frozenset({4, 5, 6, 7, 8}), frozenset({1, 2, 3})]
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```

### Step 6: Assign unknown = 3

```python
G[1][4][1]['weight'] = 3
```

### Step 7: Assign expected = value

```python
expected = [frozenset({1, 2, 3, 4}), frozenset({5, 6, 7, 8})]
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```


## Complete Example

```python
# Workflow
G = nx.MultiGraph()
G.add_weighted_edges_from([(1, 2, 5), (1, 2, 3), (1, 3, 6), (1, 3, 6), (2, 3, 4), (1, 4, 1), (1, 4, 1), (2, 4, 3), (2, 4, 3), (4, 5, 1), (5, 6, 3), (5, 6, 7), (5, 6, 4), (5, 7, 9), (5, 7, 9), (6, 7, 8), (7, 8, 2), (7, 8, 2), (5, 8, 6), (5, 8, 6)])
expected = [frozenset({1, 2, 3, 4}), frozenset({5, 6, 7, 8})]
assert greedy_modularity_communities(G, weight='weight') == expected
G.add_edge(4, 5, weight=16)
expected = [frozenset({4, 5, 6, 7, 8}), frozenset({1, 2, 3})]
assert greedy_modularity_communities(G, weight='weight') == expected
G[1][4][1]['weight'] = 3
expected = [frozenset({1, 2, 3, 4}), frozenset({5, 6, 7, 8})]
assert greedy_modularity_communities(G, weight='weight') == expected
```

## Next Steps


---

*Source: test_modularity_max.py:182 | Complexity: Intermediate | Last updated: 2026-06-02*