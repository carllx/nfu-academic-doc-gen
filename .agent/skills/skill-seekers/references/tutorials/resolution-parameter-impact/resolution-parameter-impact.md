# How To: Resolution Parameter Impact

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resolution parameter impact

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(5, 3)
```

**Verification:**
```python
assert greedy_modularity_communities(G, resolution=gamma) == expected
```

### Step 2: Assign gamma = 1

```python
gamma = 1
```

**Verification:**
```python
assert naive_greedy_modularity_communities(G, resolution=gamma) == expected
```

### Step 3: Assign expected = value

```python
expected = [frozenset(range(5)), frozenset(range(8, 13)), frozenset(range(5, 8))]
```

**Verification:**
```python
assert greedy_modularity_communities(G, resolution=gamma) == expected
```

### Step 4: Assign gamma = 2.5

```python
gamma = 2.5
```

**Verification:**
```python
assert naive_greedy_modularity_communities(G, resolution=gamma) == expected
```

### Step 5: Assign expected = value

```python
expected = [{0, 1, 2, 3}, {9, 10, 11, 12}, {5, 6, 7}, {4}, {8}]
```

**Verification:**
```python
assert greedy_modularity_communities(G, resolution=gamma) == expected
```

### Step 6: Assign gamma = 0.3

```python
gamma = 0.3
```

**Verification:**
```python
assert naive_greedy_modularity_communities(G, resolution=gamma) == expected
```

### Step 7: Assign expected = value

```python
expected = [frozenset(range(8)), frozenset(range(8, 13))]
```

**Verification:**
```python
assert greedy_modularity_communities(G, resolution=gamma) == expected
```


## Complete Example

```python
# Workflow
G = nx.barbell_graph(5, 3)
gamma = 1
expected = [frozenset(range(5)), frozenset(range(8, 13)), frozenset(range(5, 8))]
assert greedy_modularity_communities(G, resolution=gamma) == expected
assert naive_greedy_modularity_communities(G, resolution=gamma) == expected
gamma = 2.5
expected = [{0, 1, 2, 3}, {9, 10, 11, 12}, {5, 6, 7}, {4}, {8}]
assert greedy_modularity_communities(G, resolution=gamma) == expected
assert naive_greedy_modularity_communities(G, resolution=gamma) == expected
gamma = 0.3
expected = [frozenset(range(8)), frozenset(range(8, 13))]
assert greedy_modularity_communities(G, resolution=gamma) == expected
assert naive_greedy_modularity_communities(G, resolution=gamma) == expected
```

## Next Steps


---

*Source: test_modularity_max.py:282 | Complexity: Intermediate | Last updated: 2026-06-02*