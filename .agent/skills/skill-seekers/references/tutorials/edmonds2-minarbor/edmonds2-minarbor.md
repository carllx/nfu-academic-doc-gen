# How To: Edmonds2 Minarbor

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edmonds2 minarbor

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
assert_equal_branchings(x, x_)
```

### Step 2: Assign x = branchings.minimum_spanning_arborescence(...)

```python
x = branchings.minimum_spanning_arborescence(G)
```

### Step 3: Assign edges = value

```python
edges = [(3, 0, 5), (0, 2, 12), (0, 4, 12), (2, 5, 12), (4, 7, 12), (5, 8, 12), (5, 6, 14), (2, 1, 17)]
```

### Step 4: Assign x_ = build_branching(...)

```python
x_ = build_branching(edges)
```

### Step 5: Call assert_equal_branchings()

```python
assert_equal_branchings(x, x_)
```


## Complete Example

```python
# Workflow
G = G1()
x = branchings.minimum_spanning_arborescence(G)
edges = [(3, 0, 5), (0, 2, 12), (0, 4, 12), (2, 5, 12), (4, 7, 12), (5, 8, 12), (5, 6, 14), (2, 1, 17)]
x_ = build_branching(edges)
assert_equal_branchings(x, x_)
```

## Next Steps


---

*Source: test_branchings.py:336 | Complexity: Intermediate | Last updated: 2026-06-02*