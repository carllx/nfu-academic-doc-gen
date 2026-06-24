# How To: Generate Network Text Directed Multi Tree

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generate network text directed multi tree

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
tree1 = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
```

**Verification:**
```python
assert ret == target
```

### Step 2: Assign tree2 = nx.balanced_tree(...)

```python
tree2 = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
```

**Verification:**
```python
assert ret == target
```

### Step 3: Assign forest = nx.disjoint_union_all(...)

```python
forest = nx.disjoint_union_all([tree1, tree2])
```

**Verification:**
```python
assert ret == target
```

### Step 4: Assign ret = unknown.join(...)

```python
ret = '\n'.join(nx.generate_network_text(forest))
```

### Step 5: Assign target = dedent.strip(...)

```python
target = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   │   ├─╼ 3\n        ╎   │   └─╼ 4\n        ╎   └─╼ 2\n        ╎       ├─╼ 5\n        ╎       └─╼ 6\n        ╙── 7\n            ├─╼ 8\n            │   ├─╼ 10\n            │   └─╼ 11\n            └─╼ 9\n                ├─╼ 12\n                └─╼ 13\n        ').strip()
```

**Verification:**
```python
assert ret == target
```

### Step 6: Assign tree3 = nx.balanced_tree(...)

```python
tree3 = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
```

### Step 7: Assign forest = nx.disjoint_union_all(...)

```python
forest = nx.disjoint_union_all([tree1, tree2, tree3])
```

### Step 8: Assign ret = unknown.join(...)

```python
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 14, 7]))
```

### Step 9: Assign target = dedent.strip(...)

```python
target = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   │   ├─╼ 3\n        ╎   │   └─╼ 4\n        ╎   └─╼ 2\n        ╎       ├─╼ 5\n        ╎       └─╼ 6\n        ╟── 14\n        ╎   ├─╼ 15\n        ╎   │   ├─╼ 17\n        ╎   │   └─╼ 18\n        ╎   └─╼ 16\n        ╎       ├─╼ 19\n        ╎       └─╼ 20\n        ╙── 7\n            ├─╼ 8\n            │   ├─╼ 10\n            │   └─╼ 11\n            └─╼ 9\n                ├─╼ 12\n                └─╼ 13\n        ').strip()
```

**Verification:**
```python
assert ret == target
```

### Step 10: Assign ret = unknown.join(...)

```python
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 14, 7], ascii_only=True))
```

### Step 11: Assign target = dedent.strip(...)

```python
target = dedent('\n        +-- 0\n        :   |-> 1\n        :   |   |-> 3\n        :   |   L-> 4\n        :   L-> 2\n        :       |-> 5\n        :       L-> 6\n        +-- 14\n        :   |-> 15\n        :   |   |-> 17\n        :   |   L-> 18\n        :   L-> 16\n        :       |-> 19\n        :       L-> 20\n        +-- 7\n            |-> 8\n            |   |-> 10\n            |   L-> 11\n            L-> 9\n                |-> 12\n                L-> 13\n        ').strip()
```

**Verification:**
```python
assert ret == target
```


## Complete Example

```python
# Workflow
tree1 = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
tree2 = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
forest = nx.disjoint_union_all([tree1, tree2])
ret = '\n'.join(nx.generate_network_text(forest))
target = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   │   ├─╼ 3\n        ╎   │   └─╼ 4\n        ╎   └─╼ 2\n        ╎       ├─╼ 5\n        ╎       └─╼ 6\n        ╙── 7\n            ├─╼ 8\n            │   ├─╼ 10\n            │   └─╼ 11\n            └─╼ 9\n                ├─╼ 12\n                └─╼ 13\n        ').strip()
assert ret == target
tree3 = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
forest = nx.disjoint_union_all([tree1, tree2, tree3])
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 14, 7]))
target = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   │   ├─╼ 3\n        ╎   │   └─╼ 4\n        ╎   └─╼ 2\n        ╎       ├─╼ 5\n        ╎       └─╼ 6\n        ╟── 14\n        ╎   ├─╼ 15\n        ╎   │   ├─╼ 17\n        ╎   │   └─╼ 18\n        ╎   └─╼ 16\n        ╎       ├─╼ 19\n        ╎       └─╼ 20\n        ╙── 7\n            ├─╼ 8\n            │   ├─╼ 10\n            │   └─╼ 11\n            └─╼ 9\n                ├─╼ 12\n                └─╼ 13\n        ').strip()
assert ret == target
ret = '\n'.join(nx.generate_network_text(forest, sources=[0, 14, 7], ascii_only=True))
target = dedent('\n        +-- 0\n        :   |-> 1\n        :   |   |-> 3\n        :   |   L-> 4\n        :   L-> 2\n        :       |-> 5\n        :       L-> 6\n        +-- 14\n        :   |-> 15\n        :   |   |-> 17\n        :   |   L-> 18\n        :   L-> 16\n        :       |-> 19\n        :       L-> 20\n        +-- 7\n            |-> 8\n            |   |-> 10\n            |   L-> 11\n            L-> 9\n                |-> 12\n                L-> 13\n        ').strip()
assert ret == target
```

## Next Steps


---

*Source: test_text.py:85 | Complexity: Advanced | Last updated: 2026-06-02*