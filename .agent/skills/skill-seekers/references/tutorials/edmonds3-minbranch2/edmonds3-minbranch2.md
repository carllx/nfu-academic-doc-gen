# How To: Edmonds3 Minbranch2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edmonds3 minbranch2

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

### Step 2: Call G.add_edge()

```python
G.add_edge(8, 9, weight=-10)
```

### Step 3: Assign x = branchings.minimum_branching(...)

```python
x = branchings.minimum_branching(G)
```

### Step 4: Assign edges = value

```python
edges = [(8, 9, -10)]
```

### Step 5: Assign x_ = build_branching(...)

```python
x_ = build_branching(edges)
```

### Step 6: Call assert_equal_branchings()

```python
assert_equal_branchings(x, x_)
```


## Complete Example

```python
# Workflow
G = G1()
G.add_edge(8, 9, weight=-10)
x = branchings.minimum_branching(G)
edges = [(8, 9, -10)]
x_ = build_branching(edges)
assert_equal_branchings(x, x_)
```

## Next Steps


---

*Source: test_branchings.py:363 | Complexity: Intermediate | Last updated: 2026-06-02*