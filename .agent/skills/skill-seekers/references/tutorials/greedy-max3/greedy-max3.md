# How To: Greedy Max3

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test greedy max3

## Prerequisites

**Required Modules:**
- `math`
- `operator`
- `pytest`
- `networkx`
- `networkx.algorithms.tree`


## Step-by-Step Guide

### Step 1: Assign G = G1(...)

```python
G = G1()
```

**Verification:**
```python
assert_equal_branchings(B, B_, default=1)
```

### Step 2: Assign B = branchings.greedy_branching(...)

```python
B = branchings.greedy_branching(G, attr=None)
```

### Step 3: Assign edges = value

```python
edges = [(2, 1, 1), (3, 0, 1), (3, 4, 1), (5, 8, 1), (6, 2, 1), (7, 3, 1), (7, 6, 1), (8, 7, 1)]
```

### Step 4: Assign B_ = build_branching(...)

```python
B_ = build_branching(edges)
```

### Step 5: Call assert_equal_branchings()

```python
assert_equal_branchings(B, B_, default=1)
```


## Complete Example

```python
# Workflow
G = G1()
B = branchings.greedy_branching(G, attr=None)
edges = [(2, 1, 1), (3, 0, 1), (3, 4, 1), (5, 8, 1), (6, 2, 1), (7, 3, 1), (7, 6, 1), (8, 7, 1)]
B_ = build_branching(edges)
assert_equal_branchings(B, B_, default=1)
```

## Next Steps


---

*Source: test_branchings.py:251 | Complexity: Intermediate | Last updated: 2026-06-02*