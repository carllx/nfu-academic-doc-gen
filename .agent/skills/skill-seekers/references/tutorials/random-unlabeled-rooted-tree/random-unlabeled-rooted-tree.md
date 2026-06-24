# How To: Random Unlabeled Rooted Tree

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random unlabeled rooted tree

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign t = nx.random_unlabeled_rooted_tree(...)

```python
t = nx.random_unlabeled_rooted_tree(15, number_of_trees=10, seed=43)
```

**Verification:**
```python
assert nx.utils.misc.graphs_equal(t1, t2)
```

### Step 2: Call random.seed()

```python
random.seed(43)
```

**Verification:**
```python
assert nx.is_tree(t1)
```

### Step 3: Assign s = nx.random_unlabeled_rooted_tree(...)

```python
s = nx.random_unlabeled_rooted_tree(15, number_of_trees=10, seed=random)
```

**Verification:**
```python
assert 'root' in t1.graph
```

### Step 4: Assign t1 = nx.random_unlabeled_rooted_tree(...)

```python
t1 = nx.random_unlabeled_rooted_tree(i, seed=42)
```

**Verification:**
```python
assert 'roots' not in t1.graph
```

### Step 5: Assign t2 = nx.random_unlabeled_rooted_tree(...)

```python
t2 = nx.random_unlabeled_rooted_tree(i, seed=42)
```

**Verification:**
```python
assert nx.utils.misc.graphs_equal(t[i], s[i])
```


## Complete Example

```python
# Workflow
for i in range(1, 10):
    t1 = nx.random_unlabeled_rooted_tree(i, seed=42)
    t2 = nx.random_unlabeled_rooted_tree(i, seed=42)
    assert nx.utils.misc.graphs_equal(t1, t2)
    assert nx.is_tree(t1)
    assert 'root' in t1.graph
    assert 'roots' not in t1.graph
t = nx.random_unlabeled_rooted_tree(15, number_of_trees=10, seed=43)
random.seed(43)
s = nx.random_unlabeled_rooted_tree(15, number_of_trees=10, seed=random)
for i in range(10):
    assert nx.utils.misc.graphs_equal(t[i], s[i])
    assert nx.is_tree(t[i])
    assert 'root' in t[i].graph
    assert 'roots' not in t[i].graph
```

## Next Steps


---

*Source: test_trees.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*