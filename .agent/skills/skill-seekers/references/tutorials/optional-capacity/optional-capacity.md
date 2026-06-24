# How To: Optional Capacity

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test optional capacity

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 2: Call G.add_edge()

```python
G.add_edge('x', 'a', spam=3.0)
```

### Step 3: Call G.add_edge()

```python
G.add_edge('x', 'b', spam=1.0)
```

### Step 4: Call G.add_edge()

```python
G.add_edge('a', 'c', spam=3.0)
```

### Step 5: Call G.add_edge()

```python
G.add_edge('b', 'c', spam=5.0)
```

### Step 6: Call G.add_edge()

```python
G.add_edge('b', 'd', spam=4.0)
```

### Step 7: Call G.add_edge()

```python
G.add_edge('d', 'e', spam=2.0)
```

### Step 8: Call G.add_edge()

```python
G.add_edge('c', 'y', spam=2.0)
```

### Step 9: Call G.add_edge()

```python
G.add_edge('e', 'y', spam=3.0)
```

### Step 10: Assign solnValue = 3.0

```python
solnValue = 3.0
```

### Step 11: Assign s = 'x'

```python
s = 'x'
```

### Step 12: Assign t = 'y'

```python
t = 'y'
```

### Step 13: Call compare_flows_and_cuts()

```python
compare_flows_and_cuts(G, s, t, solnValue, capacity='spam')
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge('x', 'a', spam=3.0)
G.add_edge('x', 'b', spam=1.0)
G.add_edge('a', 'c', spam=3.0)
G.add_edge('b', 'c', spam=5.0)
G.add_edge('b', 'd', spam=4.0)
G.add_edge('d', 'e', spam=2.0)
G.add_edge('c', 'y', spam=2.0)
G.add_edge('e', 'y', spam=3.0)
solnValue = 3.0
s = 'x'
t = 'y'
compare_flows_and_cuts(G, s, t, solnValue, capacity='spam')
```

## Next Steps


---

*Source: test_maxflow.py:246 | Complexity: Advanced | Last updated: 2026-06-02*