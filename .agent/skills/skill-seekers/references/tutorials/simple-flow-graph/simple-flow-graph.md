# How To: Simple Flow Graph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: simple flow graph

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 2: Call G.add_node()

```python
G.add_node('a', demand=0)
```

### Step 3: Call G.add_node()

```python
G.add_node('b', demand=-5)
```

### Step 4: Call G.add_node()

```python
G.add_node('c', demand=50000000)
```

### Step 5: Call G.add_node()

```python
G.add_node('d', demand=-49999995)
```

### Step 6: Call G.add_edge()

```python
G.add_edge('a', 'b', weight=3, capacity=4)
```

### Step 7: Call G.add_edge()

```python
G.add_edge('a', 'c', weight=6, capacity=10)
```

### Step 8: Call G.add_edge()

```python
G.add_edge('b', 'd', weight=1, capacity=9)
```

### Step 9: Call G.add_edge()

```python
G.add_edge('c', 'd', weight=2, capacity=5)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_node('a', demand=0)
G.add_node('b', demand=-5)
G.add_node('c', demand=50000000)
G.add_node('d', demand=-49999995)
G.add_edge('a', 'b', weight=3, capacity=4)
G.add_edge('a', 'c', weight=6, capacity=10)
G.add_edge('b', 'd', weight=1, capacity=9)
G.add_edge('c', 'd', weight=2, capacity=5)
return G
```

## Next Steps


---

*Source: test_networksimplex.py:11 | Complexity: Advanced | Last updated: 2026-06-02*