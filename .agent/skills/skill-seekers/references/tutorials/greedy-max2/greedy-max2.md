# How To: Greedy Max2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test greedy max2

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
assert_equal_branchings(B, B_)
```

### Step 2: Assign B = branchings.greedy_branching(...)

```python
B = branchings.greedy_branching(G, default=6)
```

### Step 3: Assign edges = value

```python
edges = [(1, 0, 6), (1, 5, 13), (7, 6, 15), (2, 1, 17), (3, 4, 17), (8, 7, 18), (2, 3, 21), (6, 2, 21)]
```

### Step 4: Assign B_ = build_branching(...)

```python
B_ = build_branching(edges)
```

### Step 5: Call assert_equal_branchings()

```python
assert_equal_branchings(B, B_)
```


## Complete Example

```python
# Workflow
G = G1()
del G[1][0][0]['weight']
B = branchings.greedy_branching(G, default=6)
edges = [(1, 0, 6), (1, 5, 13), (7, 6, 15), (2, 1, 17), (3, 4, 17), (8, 7, 18), (2, 3, 21), (6, 2, 21)]
B_ = build_branching(edges)
assert_equal_branchings(B, B_)
```

## Next Steps


---

*Source: test_branchings.py:229 | Complexity: Intermediate | Last updated: 2026-06-02*