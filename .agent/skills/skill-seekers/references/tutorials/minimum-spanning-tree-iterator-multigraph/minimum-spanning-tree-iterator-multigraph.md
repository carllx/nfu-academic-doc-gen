# How To: Minimum Spanning Tree Iterator Multigraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the spanning trees are correctly returned in increasing order

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `math`
- `math`
- `random`
- `random`
- `itertools`


## Step-by-Step Guide

### Step 1: '\n        Tests that the spanning trees are correctly returned in increasing order\n        '

```python
'\n        Tests that the spanning trees are correctly returned in increasing order\n        '
```

**Verification:**
```python
assert actual in self.spanning_trees
```

### Step 2: Assign tree_index = 0

```python
tree_index = 0
```

**Verification:**
```python
assert weight >= last_weight
```

### Step 3: Assign last_weight = 0

```python
last_weight = 0
```

### Step 4: Assign actual = sorted(...)

```python
actual = sorted(tree.edges(keys=True, data=True))
```

### Step 5: Assign weight = sum(...)

```python
weight = sum([e[3]['weight'] for e in actual])
```

**Verification:**
```python
assert actual in self.spanning_trees
```


## Complete Example

```python
# Workflow
'\n        Tests that the spanning trees are correctly returned in increasing order\n        '
tree_index = 0
last_weight = 0
for tree in nx.SpanningTreeIterator(self.G):
    actual = sorted(tree.edges(keys=True, data=True))
    weight = sum([e[3]['weight'] for e in actual])
    assert actual in self.spanning_trees
    assert weight >= last_weight
    tree_index += 1
```

## Next Steps


---

*Source: test_mst.py:508 | Complexity: Intermediate | Last updated: 2026-06-02*