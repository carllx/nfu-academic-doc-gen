# How To: Ego

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ego

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.star_graph(...)

```python
G = nx.star_graph(3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, H)
```

### Step 2: Assign H = nx.ego_graph(...)

```python
H = nx.ego_graph(G, 0)
```

**Verification:**
```python
assert nx.is_isomorphic(nx.star_graph(3), H)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 11)
```

**Verification:**
```python
assert edges_equal(H.edges(), [(0, 1)])
```

### Step 4: Call G.add_edge()

```python
G.add_edge(2, 22)
```

**Verification:**
```python
assert edges_equal(H.edges(), [(0, 1)])
```

### Step 5: Call G.add_edge()

```python
G.add_edge(3, 33)
```

**Verification:**
```python
assert edges_equal(H.edges(), [])
```

### Step 6: Assign H = nx.ego_graph(...)

```python
H = nx.ego_graph(G, 0)
```

**Verification:**
```python
assert nx.is_isomorphic(nx.star_graph(3), H)
```

### Step 7: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

### Step 8: Assign H = nx.ego_graph(...)

```python
H = nx.ego_graph(G, 0)
```

**Verification:**
```python
assert edges_equal(H.edges(), [(0, 1)])
```

### Step 9: Assign H = nx.ego_graph(...)

```python
H = nx.ego_graph(G, 0, undirected=True)
```

**Verification:**
```python
assert edges_equal(H.edges(), [(0, 1)])
```

### Step 10: Assign H = nx.ego_graph(...)

```python
H = nx.ego_graph(G, 0, center=False)
```

**Verification:**
```python
assert edges_equal(H.edges(), [])
```


## Complete Example

```python
# Workflow
G = nx.star_graph(3)
H = nx.ego_graph(G, 0)
assert nx.is_isomorphic(G, H)
G.add_edge(1, 11)
G.add_edge(2, 22)
G.add_edge(3, 33)
H = nx.ego_graph(G, 0)
assert nx.is_isomorphic(nx.star_graph(3), H)
G = nx.path_graph(3)
H = nx.ego_graph(G, 0)
assert edges_equal(H.edges(), [(0, 1)])
H = nx.ego_graph(G, 0, undirected=True)
assert edges_equal(H.edges(), [(0, 1)])
H = nx.ego_graph(G, 0, center=False)
assert edges_equal(H.edges(), [])
```

## Next Steps


---

*Source: test_ego.py:11 | Complexity: Advanced | Last updated: 2026-06-02*