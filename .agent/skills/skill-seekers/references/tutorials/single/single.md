# How To: Single

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Joining just one tree yields a tree with one more node.

## Prerequisites

**Required Modules:**
- `itertools`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Joining just one tree yields a tree with one more node.'

```python
'Joining just one tree yields a tree with one more node.'
```

**Verification:**
```python
assert nodes_equal(list(expected), list(actual_with_label))
```

### Step 2: Assign T = nx.empty_graph(...)

```python
T = nx.empty_graph(1)
```

**Verification:**
```python
assert edges_equal(list(expected.edges()), list(actual_with_label.edges()))
```

### Step 3: Assign trees = value

```python
trees = [(T, 0)]
```

### Step 4: Assign actual_with_label = nx.join_trees(...)

```python
actual_with_label = nx.join_trees(trees, label_attribute='custom_label')
```

### Step 5: Assign expected = nx.path_graph(...)

```python
expected = nx.path_graph(2)
```

**Verification:**
```python
assert nodes_equal(list(expected), list(actual_with_label))
```


## Complete Example

```python
# Workflow
'Joining just one tree yields a tree with one more node.'
T = nx.empty_graph(1)
trees = [(T, 0)]
actual_with_label = nx.join_trees(trees, label_attribute='custom_label')
expected = nx.path_graph(2)
assert nodes_equal(list(expected), list(actual_with_label))
assert edges_equal(list(expected.edges()), list(actual_with_label.edges()))
```

## Next Steps


---

*Source: test_operations.py:22 | Complexity: Intermediate | Last updated: 2026-06-02*