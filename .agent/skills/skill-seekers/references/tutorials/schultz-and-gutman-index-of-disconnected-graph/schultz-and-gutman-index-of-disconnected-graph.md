# How To: Schultz And Gutman Index Of Disconnected Graph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test schultz and gutman index of disconnected graph

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign n = 4

```python
n = 4
```

**Verification:**
```python
assert expected == actual_1
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert expected == actual_2
```

### Step 3: Call G.add_nodes_from()

```python
G.add_nodes_from(list(range(1, n + 1)))
```

### Step 4: Assign expected = float(...)

```python
expected = float('inf')
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 2)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(3, 4)
```

### Step 7: Assign actual_1 = nx.schultz_index(...)

```python
actual_1 = nx.schultz_index(G)
```

### Step 8: Assign actual_2 = nx.gutman_index(...)

```python
actual_2 = nx.gutman_index(G)
```

**Verification:**
```python
assert expected == actual_1
```


## Complete Example

```python
# Workflow
n = 4
G = nx.Graph()
G.add_nodes_from(list(range(1, n + 1)))
expected = float('inf')
G.add_edge(1, 2)
G.add_edge(3, 4)
actual_1 = nx.schultz_index(G)
actual_2 = nx.gutman_index(G)
assert expected == actual_1
assert expected == actual_2
```

## Next Steps


---

*Source: test_wiener.py:50 | Complexity: Advanced | Last updated: 2026-06-02*