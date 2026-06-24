# How To: Edmonds1 Minbranch

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edmonds1 minbranch

## Prerequisites

**Required Modules:**
- `math`
- `operator`
- `pytest`
- `networkx`
- `networkx.algorithms.tree`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(u, v, -w) for u, v, w in optimal_arborescence_1]
```

**Verification:**
```python
assert_equal_branchings(x, x_)
```

### Step 2: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(-G_array, create_using=nx.DiGraph)
```

**Verification:**
```python
assert_equal_branchings(x, x_)
```

### Step 3: Assign x = branchings.maximum_branching(...)

```python
x = branchings.maximum_branching(G)
```

### Step 4: Assign x_ = build_branching(...)

```python
x_ = build_branching([])
```

### Step 5: Call assert_equal_branchings()

```python
assert_equal_branchings(x, x_)
```

### Step 6: Assign x = branchings.minimum_branching(...)

```python
x = branchings.minimum_branching(G)
```

### Step 7: Assign x_ = build_branching(...)

```python
x_ = build_branching(edges)
```

### Step 8: Call assert_equal_branchings()

```python
assert_equal_branchings(x, x_)
```


## Complete Example

```python
# Workflow
edges = [(u, v, -w) for u, v, w in optimal_arborescence_1]
G = nx.from_numpy_array(-G_array, create_using=nx.DiGraph)
x = branchings.maximum_branching(G)
x_ = build_branching([])
assert_equal_branchings(x, x_)
x = branchings.minimum_branching(G)
x_ = build_branching(edges)
assert_equal_branchings(x, x_)
```

## Next Steps


---

*Source: test_branchings.py:419 | Complexity: Advanced | Last updated: 2026-06-02*