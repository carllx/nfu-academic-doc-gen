# How To: First Label

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test the functionality of the first_label argument.

## Prerequisites

**Required Modules:**
- `itertools`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Test the functionality of the first_label argument.'

```python
'Test the functionality of the first_label argument.'
```

**Verification:**
```python
assert set(actual.nodes()) == expected_nodes
```

### Step 2: Assign T1 = nx.path_graph(...)

```python
T1 = nx.path_graph(3)
```

**Verification:**
```python
assert set(actual.neighbors(10)) == {11, 14}
```

### Step 3: Assign T2 = nx.path_graph(...)

```python
T2 = nx.path_graph(2)
```

### Step 4: Assign actual = nx.join_trees(...)

```python
actual = nx.join_trees([(T1, 0), (T2, 0)], first_label=10)
```

### Step 5: Assign expected_nodes = set(...)

```python
expected_nodes = set(range(10, 16))
```

**Verification:**
```python
assert set(actual.nodes()) == expected_nodes
```


## Complete Example

```python
# Workflow
'Test the functionality of the first_label argument.'
T1 = nx.path_graph(3)
T2 = nx.path_graph(2)
actual = nx.join_trees([(T1, 0), (T2, 0)], first_label=10)
expected_nodes = set(range(10, 16))
assert set(actual.nodes()) == expected_nodes
assert set(actual.neighbors(10)) == {11, 14}
```

## Next Steps


---

*Source: test_operations.py:46 | Complexity: Intermediate | Last updated: 2026-06-02*