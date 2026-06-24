# How To: Best N

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test best n

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
assert greedy_modularity_communities(G, best_n=best_n) == expected
```

### Step 2: Assign best_n = 3

```python
best_n = 3
```

**Verification:**
```python
assert greedy_modularity_communities(G, best_n=best_n) == expected
```

### Step 3: Assign expected = value

```python
expected = [frozenset(range(5)), frozenset(range(8, 13)), frozenset(range(5, 8))]
```

**Verification:**
```python
assert greedy_modularity_communities(G, best_n=best_n) == expected
```

### Step 4: Assign best_n = 2

```python
best_n = 2
```

### Step 5: Assign expected = value

```python
expected = [frozenset(range(8)), frozenset(range(8, 13))]
```

**Verification:**
```python
assert greedy_modularity_communities(G, best_n=best_n) == expected
```

### Step 6: Assign best_n = 1

```python
best_n = 1
```

### Step 7: Assign expected = value

```python
expected = [frozenset(range(13))]
```

**Verification:**
```python
assert greedy_modularity_communities(G, best_n=best_n) == expected
```


## Complete Example

```python
# Workflow
G = nx.barbell_graph(5, 3)
best_n = 3
expected = [frozenset(range(5)), frozenset(range(8, 13)), frozenset(range(5, 8))]
assert greedy_modularity_communities(G, best_n=best_n) == expected
best_n = 2
expected = [frozenset(range(8)), frozenset(range(8, 13))]
assert greedy_modularity_communities(G, best_n=best_n) == expected
best_n = 1
expected = [frozenset(range(13))]
assert greedy_modularity_communities(G, best_n=best_n) == expected
```

## Next Steps


---

*Source: test_modularity_max.py:317 | Complexity: Intermediate | Last updated: 2026-06-02*