# How To: Prominent Group Disconnected Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Prominent group of disconnected graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n        Prominent group of disconnected graph\n        '

```python
'\n        Prominent group of disconnected graph\n        '
```

**Verification:**
```python
assert b == b_answer and g == g_answer
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(6)
```

### Step 3: Call G.remove_edge()

```python
G.remove_edge(0, 1)
```

### Step 4: Assign k = 1

```python
k = 1
```

### Step 5: Assign unknown = nx.prominent_group(...)

```python
b, g = nx.prominent_group(G, k, weight=None, normalized=False)
```

### Step 6: Assign unknown = value

```python
b_answer, g_answer = (4.0, [3])
```

**Verification:**
```python
assert b == b_answer and g == g_answer
```


## Complete Example

```python
# Workflow
'\n        Prominent group of disconnected graph\n        '
G = nx.path_graph(6)
G.remove_edge(0, 1)
k = 1
b, g = nx.prominent_group(G, k, weight=None, normalized=False)
b_answer, g_answer = (4.0, [3])
assert b == b_answer and g == g_answer
```

## Next Steps


---

*Source: test_group.py:138 | Complexity: Intermediate | Last updated: 2026-06-02*