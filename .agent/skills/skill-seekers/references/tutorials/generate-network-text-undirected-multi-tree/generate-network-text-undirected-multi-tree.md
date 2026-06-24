# How To: Generate Network Text Undirected Multi Tree

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generate network text undirected multi tree

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `textwrap`
- `pytest`
- `networkx`
- `random`
- `networkx.readwrite.text`


## Step-by-Step Guide

### Step 1: Assign tree1 = nx.balanced_tree(...)

```python
tree1 = nx.balanced_tree(r=2, h=2, create_using=nx.Graph)
```

**Verification:**
```python
assert ret == target
```

### Step 2: Assign tree2 = nx.balanced_tree(...)

```python
tree2 = nx.balanced_tree(r=2, h=2, create_using=nx.Graph)
```

**Verification:**
```python
assert ret == target
```

### Step 3: Assign tree2 = nx.relabel_nodes(...)

```python
tree2 = nx.relabel_nodes(tree2, {n: n + len(tree1) for n in tree2.nodes})
```

### Step 4: Assign forest = nx.union(...)

```python
forest = nx.union(tree1, tree2)
```

### Step 5: Assign ret = unknown.join(...)

```python
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 7]))
```

### Step 6: Assign target = dedent.strip(...)

```python
target = dedent('\n        ╟── 0\n        ╎   ├── 1\n        ╎   │   ├── 3\n        ╎   │   └── 4\n        ╎   └── 2\n        ╎       ├── 5\n        ╎       └── 6\n        ╙── 7\n            ├── 8\n            │   ├── 10\n            │   └── 11\n            └── 9\n                ├── 12\n                └── 13\n        ').strip()
```

**Verification:**
```python
assert ret == target
```

### Step 7: Assign ret = unknown.join(...)

```python
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 7], ascii_only=True))
```

### Step 8: Assign target = dedent.strip(...)

```python
target = dedent('\n        +-- 0\n        :   |-- 1\n        :   |   |-- 3\n        :   |   L-- 4\n        :   L-- 2\n        :       |-- 5\n        :       L-- 6\n        +-- 7\n            |-- 8\n            |   |-- 10\n            |   L-- 11\n            L-- 9\n                |-- 12\n                L-- 13\n        ').strip()
```

**Verification:**
```python
assert ret == target
```


## Complete Example

```python
# Workflow
tree1 = nx.balanced_tree(r=2, h=2, create_using=nx.Graph)
tree2 = nx.balanced_tree(r=2, h=2, create_using=nx.Graph)
tree2 = nx.relabel_nodes(tree2, {n: n + len(tree1) for n in tree2.nodes})
forest = nx.union(tree1, tree2)
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 7]))
target = dedent('\n        ╟── 0\n        ╎   ├── 1\n        ╎   │   ├── 3\n        ╎   │   └── 4\n        ╎   └── 2\n        ╎       ├── 5\n        ╎       └── 6\n        ╙── 7\n            ├── 8\n            │   ├── 10\n            │   └── 11\n            └── 9\n                ├── 12\n                └── 13\n        ').strip()
assert ret == target
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 7], ascii_only=True))
target = dedent('\n        +-- 0\n        :   |-- 1\n        :   |   |-- 3\n        :   |   L-- 4\n        :   L-- 2\n        :       |-- 5\n        :       L-- 6\n        +-- 7\n            |-- 8\n            |   |-- 10\n            |   L-- 11\n            L-- 9\n                |-- 12\n                L-- 13\n        ').strip()
assert ret == target
```

## Next Steps


---

*Source: test_text.py:174 | Complexity: Advanced | Last updated: 2026-06-02*