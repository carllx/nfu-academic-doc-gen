# How To: Random Unlabeled Rooted Forest

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test random unlabeled rooted forest

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign t = nx.random_unlabeled_rooted_forest(...)

```python
t = nx.random_unlabeled_rooted_forest(15, number_of_forests=10, seed=43)
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
assert nx.is_tree(t1.subgraph(c))
```

### Step 3: Assign s = nx.random_unlabeled_rooted_forest(...)

```python
s = nx.random_unlabeled_rooted_forest(15, number_of_forests=10, seed=random)
```

**Verification:**
```python
assert len(c) <= q
```

### Step 4: Call nx.random_unlabeled_rooted_forest()

```python
nx.random_unlabeled_rooted_forest(10, q=0, seed=42)
```

**Verification:**
```python
assert 'root' not in t1.graph
```

### Step 5: Assign t1 = nx.random_unlabeled_rooted_forest(...)

```python
t1 = nx.random_unlabeled_rooted_forest(i, q=q, seed=42)
```

**Verification:**
```python
assert 'roots' in t1.graph
```

### Step 6: Assign t2 = nx.random_unlabeled_rooted_forest(...)

```python
t2 = nx.random_unlabeled_rooted_forest(i, q=q, seed=42)
```

**Verification:**
```python
assert nx.utils.misc.graphs_equal(t[i], s[i])
```


## Complete Example

```python
# Workflow
with pytest.raises(ValueError):
    nx.random_unlabeled_rooted_forest(10, q=0, seed=42)
for i in range(1, 10):
    for q in range(1, i + 1):
        t1 = nx.random_unlabeled_rooted_forest(i, q=q, seed=42)
        t2 = nx.random_unlabeled_rooted_forest(i, q=q, seed=42)
        assert nx.utils.misc.graphs_equal(t1, t2)
        for c in nx.connected_components(t1):
            assert nx.is_tree(t1.subgraph(c))
            assert len(c) <= q
        assert 'root' not in t1.graph
        assert 'roots' in t1.graph
t = nx.random_unlabeled_rooted_forest(15, number_of_forests=10, seed=43)
random.seed(43)
s = nx.random_unlabeled_rooted_forest(15, number_of_forests=10, seed=random)
for i in range(10):
    assert nx.utils.misc.graphs_equal(t[i], s[i])
    for c in nx.connected_components(t[i]):
        assert nx.is_tree(t[i].subgraph(c))
    assert 'root' not in t[i].graph
    assert 'roots' in t[i].graph
```

## Next Steps


---

*Source: test_trees.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*