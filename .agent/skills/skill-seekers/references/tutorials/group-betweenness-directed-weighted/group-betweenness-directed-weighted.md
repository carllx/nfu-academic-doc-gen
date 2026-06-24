# How To: Group Betweenness Directed Weighted

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Group betweenness centrality in a directed and weighted graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n        Group betweenness centrality in a directed and weighted graph\n        '

```python
'\n        Group betweenness centrality in a directed and weighted graph\n        '
```

**Verification:**
```python
assert b == b_answer and g == g_answer
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 0, weight=1)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(0, 2, weight=2)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 2, weight=3)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(3, 1, weight=4)
```

### Step 7: Call G.add_edge()

```python
G.add_edge(2, 3, weight=1)
```

### Step 8: Call G.add_edge()

```python
G.add_edge(4, 3, weight=6)
```

### Step 9: Call G.add_edge()

```python
G.add_edge(2, 4, weight=7)
```

### Step 10: Assign k = 2

```python
k = 2
```

### Step 11: Assign unknown = nx.prominent_group(...)

```python
b, g = nx.prominent_group(G, k, weight='weight', normalized=False)
```

### Step 12: Assign unknown = value

```python
b_answer, g_answer = (5.0, [1, 2])
```

**Verification:**
```python
assert b == b_answer and g == g_answer
```


## Complete Example

```python
# Workflow
'\n        Group betweenness centrality in a directed and weighted graph\n        '
G = nx.DiGraph()
G.add_edge(1, 0, weight=1)
G.add_edge(0, 2, weight=2)
G.add_edge(1, 2, weight=3)
G.add_edge(3, 1, weight=4)
G.add_edge(2, 3, weight=1)
G.add_edge(4, 3, weight=6)
G.add_edge(2, 4, weight=7)
k = 2
b, g = nx.prominent_group(G, k, weight='weight', normalized=False)
b_answer, g_answer = (5.0, [1, 2])
assert b == b_answer and g == g_answer
```

## Next Steps


---

*Source: test_group.py:156 | Complexity: Advanced | Last updated: 2026-06-02*