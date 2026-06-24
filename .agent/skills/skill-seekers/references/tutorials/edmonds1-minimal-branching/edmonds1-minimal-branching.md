# How To: Edmonds1 Minimal Branching

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edmonds1 minimal branching

## Prerequisites

**Required Modules:**
- `math`
- `operator`
- `pytest`
- `networkx`
- `networkx.algorithms.tree`


## Step-by-Step Guide

### Step 1: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(G_big_array, create_using=nx.DiGraph)
```

**Verification:**
```python
assert_equal_branchings(B, B_)
```

### Step 2: Assign B = branchings.minimal_branching(...)

```python
B = branchings.minimal_branching(G)
```

### Step 3: Assign edges = value

```python
edges = [(3, 0, 5), (0, 2, 12), (0, 4, 12), (2, 5, 12), (4, 7, 12), (5, 8, 12), (5, 6, 14), (2, 1, 17)]
```

### Step 4: Assign B_ = build_branching(...)

```python
B_ = build_branching(edges, double=True)
```

### Step 5: Call assert_equal_branchings()

```python
assert_equal_branchings(B, B_)
```


## Complete Example

```python
# Workflow
G = nx.from_numpy_array(G_big_array, create_using=nx.DiGraph)
B = branchings.minimal_branching(G)
edges = [(3, 0, 5), (0, 2, 12), (0, 4, 12), (2, 5, 12), (4, 7, 12), (5, 8, 12), (5, 6, 14), (2, 1, 17)]
B_ = build_branching(edges, double=True)
assert_equal_branchings(B, B_)
```

## Next Steps


---

*Source: test_branchings.py:304 | Complexity: Intermediate | Last updated: 2026-06-02*