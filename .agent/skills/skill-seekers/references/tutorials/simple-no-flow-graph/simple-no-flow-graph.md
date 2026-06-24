# How To: Simple No Flow Graph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: simple no flow graph

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
G.add_node('s', demand=-5)
```

### Step 3: Call G.add_node()

```python
G.add_node('t', demand=5)
```

### Step 4: Call G.add_edge()

```python
G.add_edge('s', 'a', weight=1, capacity=3)
```

### Step 5: Call G.add_edge()

```python
G.add_edge('a', 'b', weight=3)
```

### Step 6: Call G.add_edge()

```python
G.add_edge('a', 'c', weight=-6)
```

### Step 7: Call G.add_edge()

```python
G.add_edge('b', 'd', weight=1)
```

### Step 8: Call G.add_edge()

```python
G.add_edge('c', 'd', weight=-2)
```

### Step 9: Call G.add_edge()

```python
G.add_edge('d', 't', weight=1, capacity=3)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_node('s', demand=-5)
G.add_node('t', demand=5)
G.add_edge('s', 'a', weight=1, capacity=3)
G.add_edge('a', 'b', weight=3)
G.add_edge('a', 'c', weight=-6)
G.add_edge('b', 'd', weight=1)
G.add_edge('c', 'd', weight=-2)
G.add_edge('d', 't', weight=1, capacity=3)
return G
```

## Next Steps


---

*Source: test_networksimplex.py:25 | Complexity: Advanced | Last updated: 2026-06-02*