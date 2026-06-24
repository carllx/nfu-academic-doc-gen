# How To: Generate Network Text Forest Undirected

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generate network text forest undirected

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

### Step 1: Assign graph = nx.balanced_tree(...)

```python
graph = nx.balanced_tree(r=2, h=2, create_using=nx.Graph)
```

**Verification:**
```python
assert ret == node_target0
```

### Step 2: Assign node_target0 = dedent.strip(...)

```python
node_target0 = dedent('\n        ╙── 0\n            ├── 1\n            │   ├── 3\n            │   └── 4\n            └── 2\n                ├── 5\n                └── 6\n        ').strip()
```

**Verification:**
```python
assert ret == node_target2
```

### Step 3: Assign ret = unknown.join(...)

```python
ret = '\n'.join(nx.generate_network_text(graph, sources=[0]))
```

**Verification:**
```python
assert ret == node_target0
```

### Step 4: Assign node_target2 = dedent.strip(...)

```python
node_target2 = dedent('\n        ╙── 2\n            ├── 0\n            │   └── 1\n            │       ├── 3\n            │       └── 4\n            ├── 5\n            └── 6\n        ').strip()
```

### Step 5: Assign ret = unknown.join(...)

```python
ret = '\n'.join(nx.generate_network_text(graph, sources=[2]))
```

**Verification:**
```python
assert ret == node_target2
```


## Complete Example

```python
# Workflow
graph = nx.balanced_tree(r=2, h=2, create_using=nx.Graph)
node_target0 = dedent('\n        ╙── 0\n            ├── 1\n            │   ├── 3\n            │   └── 4\n            └── 2\n                ├── 5\n                └── 6\n        ').strip()
ret = '\n'.join(nx.generate_network_text(graph, sources=[0]))
assert ret == node_target0
node_target2 = dedent('\n        ╙── 2\n            ├── 0\n            │   └── 1\n            │       ├── 3\n            │       └── 4\n            ├── 5\n            └── 6\n        ').strip()
ret = '\n'.join(nx.generate_network_text(graph, sources=[2]))
assert ret == node_target2
```

## Next Steps


---

*Source: test_text.py:224 | Complexity: Intermediate | Last updated: 2026-06-02*