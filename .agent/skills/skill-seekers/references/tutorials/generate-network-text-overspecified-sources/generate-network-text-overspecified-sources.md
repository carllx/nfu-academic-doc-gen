# How To: Generate Network Text Overspecified Sources

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: When sources are directly specified, we won't be able to determine when we
are in the last component, so there will always be a trailing, leftmost
pipe.

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

### Step 1: "\n    When sources are directly specified, we won't be able to determine when we\n    are in the last component, so there will always be a trailing, leftmost\n    pipe.\n    "

```python
"\n    When sources are directly specified, we won't be able to determine when we\n    are in the last component, so there will always be a trailing, leftmost\n    pipe.\n    "
```

**Verification:**
```python
assert got1 == target1
```

### Step 2: Assign graph = nx.disjoint_union_all(...)

```python
graph = nx.disjoint_union_all([nx.balanced_tree(r=2, h=1, create_using=nx.DiGraph), nx.balanced_tree(r=1, h=2, create_using=nx.DiGraph), nx.balanced_tree(r=2, h=1, create_using=nx.DiGraph)])
```

**Verification:**
```python
assert got2 == target2
```

### Step 3: Assign target1 = dedent.strip(...)

```python
target1 = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   └─╼ 2\n        ╟── 3\n        ╎   └─╼ 4\n        ╎       └─╼ 5\n        ╟── 6\n        ╎   ├─╼ 7\n        ╎   └─╼ 8\n        ').strip()
```

### Step 4: Assign target2 = dedent.strip(...)

```python
target2 = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   └─╼ 2\n        ╟── 3\n        ╎   └─╼ 4\n        ╎       └─╼ 5\n        ╙── 6\n            ├─╼ 7\n            └─╼ 8\n        ').strip()
```

### Step 5: Assign got1 = unknown.join(...)

```python
got1 = '\n'.join(nx.generate_network_text(graph, sources=graph.nodes))
```

### Step 6: Assign got2 = unknown.join(...)

```python
got2 = '\n'.join(nx.generate_network_text(graph))
```

**Verification:**
```python
assert got1 == target1
```


## Complete Example

```python
# Workflow
"\n    When sources are directly specified, we won't be able to determine when we\n    are in the last component, so there will always be a trailing, leftmost\n    pipe.\n    "
graph = nx.disjoint_union_all([nx.balanced_tree(r=2, h=1, create_using=nx.DiGraph), nx.balanced_tree(r=1, h=2, create_using=nx.DiGraph), nx.balanced_tree(r=2, h=1, create_using=nx.DiGraph)])
target1 = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   └─╼ 2\n        ╟── 3\n        ╎   └─╼ 4\n        ╎       └─╼ 5\n        ╟── 6\n        ╎   ├─╼ 7\n        ╎   └─╼ 8\n        ').strip()
target2 = dedent('\n        ╟── 0\n        ╎   ├─╼ 1\n        ╎   └─╼ 2\n        ╟── 3\n        ╎   └─╼ 4\n        ╎       └─╼ 5\n        ╙── 6\n            ├─╼ 7\n            └─╼ 8\n        ').strip()
got1 = '\n'.join(nx.generate_network_text(graph, sources=graph.nodes))
got2 = '\n'.join(nx.generate_network_text(graph))
assert got1 == target1
assert got2 == target2
```

## Next Steps


---

*Source: test_text.py:260 | Complexity: Intermediate | Last updated: 2026-06-02*