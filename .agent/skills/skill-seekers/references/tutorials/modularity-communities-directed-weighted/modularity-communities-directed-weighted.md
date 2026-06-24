# How To: Modularity Communities Directed Weighted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test modularity communities directed weighted

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```

### Step 2: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([(1, 2, 5), (1, 3, 3), (2, 3, 6), (2, 6, 1), (1, 4, 1), (4, 5, 3), (4, 6, 7), (5, 6, 2), (5, 7, 5), (5, 8, 4), (6, 8, 3)])
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```

### Step 3: Assign expected = value

```python
expected = [frozenset({4, 5, 6, 7, 8}), frozenset({1, 2, 3})]
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```

### Step 4: Assign unknown = 20

```python
G[2][6]['weight'] = 20
```

### Step 5: Assign expected = value

```python
expected = [frozenset({1, 2, 3, 6}), frozenset({4, 5, 7, 8})]
```

**Verification:**
```python
assert greedy_modularity_communities(G, weight='weight') == expected
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_weighted_edges_from([(1, 2, 5), (1, 3, 3), (2, 3, 6), (2, 6, 1), (1, 4, 1), (4, 5, 3), (4, 6, 7), (5, 6, 2), (5, 7, 5), (5, 8, 4), (6, 8, 3)])
expected = [frozenset({4, 5, 6, 7, 8}), frozenset({1, 2, 3})]
assert greedy_modularity_communities(G, weight='weight') == expected
G[2][6]['weight'] = 20
expected = [frozenset({1, 2, 3, 6}), frozenset({4, 5, 7, 8})]
assert greedy_modularity_communities(G, weight='weight') == expected
```

## Next Steps


---

*Source: test_modularity_max.py:127 | Complexity: Intermediate | Last updated: 2026-06-02*