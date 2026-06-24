# How To: Greedy Modularity Communities Relabeled

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test greedy modularity communities relabeled

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.balanced_tree(...)

```python
G = nx.balanced_tree(2, 2)
```

**Verification:**
```python
assert greedy_modularity_communities(G) == expected
```

### Step 2: Assign mapping = value

```python
mapping = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
```

### Step 3: Assign G = nx.relabel_nodes(...)

```python
G = nx.relabel_nodes(G, mapping)
```

### Step 4: Assign expected = value

```python
expected = [frozenset({'e', 'd', 'a', 'b'}), frozenset({'c', 'f', 'g'})]
```

**Verification:**
```python
assert greedy_modularity_communities(G) == expected
```


## Complete Example

```python
# Workflow
G = nx.balanced_tree(2, 2)
mapping = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
G = nx.relabel_nodes(G, mapping)
expected = [frozenset({'e', 'd', 'a', 'b'}), frozenset({'c', 'f', 'g'})]
assert greedy_modularity_communities(G) == expected
```

## Next Steps


---

*Source: test_modularity_max.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*