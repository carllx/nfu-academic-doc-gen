# How To: Lexicographical Topological Sort2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Check the case of two or more nodes with same key value.
Want to avoid exception raised due to comparing nodes directly.
See Issue #3493

## Prerequisites

**Required Modules:**
- `collections`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: '\n        Check the case of two or more nodes with same key value.\n        Want to avoid exception raised due to comparing nodes directly.\n        See Issue #3493\n        '

```python
'\n        Check the case of two or more nodes with same key value.\n        Want to avoid exception raised due to comparing nodes directly.\n        See Issue #3493\n        '
```

**Verification:**
```python
assert sorting == test_nodes
```

### Step 2: Assign test_nodes = value

```python
test_nodes = [Test_Node(n) for n in range(4)]
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 4: Assign edges = value

```python
edges = [(0, 1), (0, 2), (0, 3), (2, 3)]
```

### Step 5: Call G.add_edges_from()

```python
G.add_edges_from(((test_nodes[a], test_nodes[b]) for a, b in edges))
```

### Step 6: Assign sorting = list(...)

```python
sorting = list(nx.lexicographical_topological_sort(G, key=sorting_key))
```

**Verification:**
```python
assert sorting == test_nodes
```

### Step 7: Assign self.label = n

```python
self.label = n
```

### Step 8: Assign self.priority = 1

```python
self.priority = 1
```


## Complete Example

```python
# Workflow
'\n        Check the case of two or more nodes with same key value.\n        Want to avoid exception raised due to comparing nodes directly.\n        See Issue #3493\n        '

class Test_Node:

    def __init__(self, n):
        self.label = n
        self.priority = 1

    def __repr__(self):
        return f'Node({self.label})'

def sorting_key(node):
    return node.priority
test_nodes = [Test_Node(n) for n in range(4)]
G = nx.DiGraph()
edges = [(0, 1), (0, 2), (0, 3), (2, 3)]
G.add_edges_from(((test_nodes[a], test_nodes[b]) for a, b in edges))
sorting = list(nx.lexicographical_topological_sort(G, key=sorting_key))
assert sorting == test_nodes
```

## Next Steps


---

*Source: test_dag.py:558 | Complexity: Advanced | Last updated: 2026-06-02*