# How To: Generate Network Text Forest Directed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generate network text forest directed

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
graph = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
```

**Verification:**
```python
assert '\n'.join(ret) == node_target
```

### Step 2: Assign node_target = dedent.strip(...)

```python
node_target = dedent('\n        ╙── 0\n            ├─╼ 1\n            │   ├─╼ 3\n            │   └─╼ 4\n            └─╼ 2\n                ├─╼ 5\n                └─╼ 6\n        ').strip()
```

**Verification:**
```python
assert '\n'.join(ret) == label_target
```

### Step 3: Assign label_target = dedent.strip(...)

```python
label_target = dedent('\n        ╙── node_a\n            ├─╼ node_b\n            │   ├─╼ node_d\n            │   └─╼ node_e\n            └─╼ node_c\n                ├─╼ node_f\n                └─╼ node_g\n        ').strip()
```

### Step 4: Assign ret = nx.generate_network_text(...)

```python
ret = nx.generate_network_text(graph, with_labels=False)
```

**Verification:**
```python
assert '\n'.join(ret) == node_target
```

### Step 5: Assign ret = nx.generate_network_text(...)

```python
ret = nx.generate_network_text(graph, with_labels=True)
```

**Verification:**
```python
assert '\n'.join(ret) == label_target
```

### Step 6: Assign unknown = value

```python
graph.nodes[node]['label'] = 'node_' + chr(ord('a') + node)
```


## Complete Example

```python
# Workflow
graph = nx.balanced_tree(r=2, h=2, create_using=nx.DiGraph)
for node in graph.nodes:
    graph.nodes[node]['label'] = 'node_' + chr(ord('a') + node)
node_target = dedent('\n        ╙── 0\n            ├─╼ 1\n            │   ├─╼ 3\n            │   └─╼ 4\n            └─╼ 2\n                ├─╼ 5\n                └─╼ 6\n        ').strip()
label_target = dedent('\n        ╙── node_a\n            ├─╼ node_b\n            │   ├─╼ node_d\n            │   └─╼ node_e\n            └─╼ node_c\n                ├─╼ node_f\n                └─╼ node_g\n        ').strip()
ret = nx.generate_network_text(graph, with_labels=False)
assert '\n'.join(ret) == node_target
ret = nx.generate_network_text(graph, with_labels=True)
assert '\n'.join(ret) == label_target
```

## Next Steps


---

*Source: test_text.py:10 | Complexity: Intermediate | Last updated: 2026-06-02*