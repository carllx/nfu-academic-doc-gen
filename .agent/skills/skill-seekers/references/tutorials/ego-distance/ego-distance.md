# How To: Ego Distance

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ego distance

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert nodes_equal(nx.ego_graph(G, 0, radius=3).nodes(), [0, 1, 2, 3])
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 1, weight=2, distance=1)
```

**Verification:**
```python
assert nodes_equal(eg.nodes(), [0, 1])
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 2, weight=2, distance=2)
```

**Verification:**
```python
assert nodes_equal(eg.nodes(), [0, 1])
```

### Step 4: Call G.add_edge()

```python
G.add_edge(2, 3, weight=2, distance=1)
```

**Verification:**
```python
assert nodes_equal(eg.nodes(), [0, 1, 2])
```

### Step 5: Assign eg = nx.ego_graph(...)

```python
eg = nx.ego_graph(G, 0, radius=3, distance='weight')
```

**Verification:**
```python
assert nodes_equal(eg.nodes(), [0, 1])
```

### Step 6: Assign eg = nx.ego_graph(...)

```python
eg = nx.ego_graph(G, 0, radius=3, distance='weight', undirected=True)
```

**Verification:**
```python
assert nodes_equal(eg.nodes(), [0, 1])
```

### Step 7: Assign eg = nx.ego_graph(...)

```python
eg = nx.ego_graph(G, 0, radius=3, distance='distance')
```

**Verification:**
```python
assert nodes_equal(eg.nodes(), [0, 1, 2])
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edge(0, 1, weight=2, distance=1)
G.add_edge(1, 2, weight=2, distance=2)
G.add_edge(2, 3, weight=2, distance=1)
assert nodes_equal(nx.ego_graph(G, 0, radius=3).nodes(), [0, 1, 2, 3])
eg = nx.ego_graph(G, 0, radius=3, distance='weight')
assert nodes_equal(eg.nodes(), [0, 1])
eg = nx.ego_graph(G, 0, radius=3, distance='weight', undirected=True)
assert nodes_equal(eg.nodes(), [0, 1])
eg = nx.ego_graph(G, 0, radius=3, distance='distance')
assert nodes_equal(eg.nodes(), [0, 1, 2])
```

## Next Steps


---

*Source: test_ego.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*