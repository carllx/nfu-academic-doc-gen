# How To: Boost Example

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boost example

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(0, 1), (1, 2), (1, 3), (2, 7), (3, 4), (4, 5), (4, 6), (5, 7), (6, 4)]
```

**Verification:**
```python
assert nx.dominance_frontiers(G, 0) == {0: set(), 1: set(), 2: {7}, 3: {7}, 4: {4, 7}, 5: {7}, 6: {4}, 7: set()}
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(edges)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = nx.dominance_frontiers(...)

```python
result = nx.dominance_frontiers(G.reverse(copy=False), 7)
```

### Step 4: Assign expected = value

```python
expected = {0: set(), 1: set(), 2: {1}, 3: {1}, 4: {1, 4}, 5: {1}, 6: {4}, 7: set()}
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
edges = [(0, 1), (1, 2), (1, 3), (2, 7), (3, 4), (4, 5), (4, 6), (5, 7), (6, 4)]
G = nx.DiGraph(edges)
assert nx.dominance_frontiers(G, 0) == {0: set(), 1: set(), 2: {7}, 3: {7}, 4: {4, 7}, 5: {7}, 6: {4}, 7: set()}
result = nx.dominance_frontiers(G.reverse(copy=False), 7)
expected = {0: set(), 1: set(), 2: {1}, 3: {1}, 4: {1, 4}, 5: {1}, 6: {4}, 7: set()}
assert result == expected
```

## Next Steps


---

*Source: test_dominance.py:176 | Complexity: Intermediate | Last updated: 2026-06-02*