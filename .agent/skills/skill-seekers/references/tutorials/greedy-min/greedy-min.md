# How To: Greedy Min

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test greedy min

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
B = branchings.greedy_branching(G, kind='min')
```

### Step 3: Assign edges = value

```python
edges = [(1, 0, 4), (0, 2, 12), (0, 4, 12), (2, 5, 12), (4, 7, 12), (5, 8, 12), (5, 6, 14), (7, 3, 19)]
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
B = branchings.greedy_branching(G, kind='min')
edges = [(1, 0, 4), (0, 2, 12), (0, 4, 12), (2, 5, 12), (4, 7, 12), (5, 8, 12), (5, 6, 14), (7, 3, 19)]
B_ = build_branching(edges)
assert_equal_branchings(B, B_)
```

## Next Steps


---

*Source: test_branchings.py:272 | Complexity: Intermediate | Last updated: 2026-06-02*