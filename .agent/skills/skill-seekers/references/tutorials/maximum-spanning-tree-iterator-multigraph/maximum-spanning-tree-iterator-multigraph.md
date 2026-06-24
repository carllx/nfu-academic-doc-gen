# How To: Maximum Spanning Tree Iterator Multigraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the spanning trees are correctly returned in decreasing order

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

### Step 1: '\n        Tests that the spanning trees are correctly returned in decreasing order\n        '

```python
'\n        Tests that the spanning trees are correctly returned in decreasing order\n        '
```

**Verification:**
```python
assert actual in self.spanning_trees
```

### Step 2: Assign tree_index = 127

```python
tree_index = 127
```

**Verification:**
```python
assert weight <= last_weight
```

### Step 3: Assign last_weight = 50

```python
last_weight = 50
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
'\n        Tests that the spanning trees are correctly returned in decreasing order\n        '
tree_index = 127
last_weight = 50
for tree in nx.SpanningTreeIterator(self.G, minimum=False):
    actual = sorted(tree.edges(keys=True, data=True))
    weight = sum([e[3]['weight'] for e in actual])
    assert actual in self.spanning_trees
    assert weight <= last_weight
    tree_index -= 1
```

## Next Steps


---

*Source: test_mst.py:521 | Complexity: Intermediate | Last updated: 2026-06-02*