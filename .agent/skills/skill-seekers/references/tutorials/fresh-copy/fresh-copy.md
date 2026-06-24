# How To: Fresh Copy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fresh copy

## Prerequisites

**Required Modules:**
- `gc`
- `pickle`
- `platform`
- `weakref`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = self.Graph(...)

```python
G = self.Graph()
```

**Verification:**
```python
assert len(G.nodes[0]) == 1
```

### Step 2: Call G.add_node()

```python
G.add_node(0)
```

**Verification:**
```python
assert len(ddict) == 1
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 2)
```

**Verification:**
```python
assert len(H.nodes[0]) == 0
```

### Step 4: Call self.add_attributes()

```python
self.add_attributes(G)
```

**Verification:**
```python
assert len(ddict) == 0
```

### Step 5: Assign H = G.__class__(...)

```python
H = G.__class__()
```

### Step 6: Call H.add_nodes_from()

```python
H.add_nodes_from(G)
```

### Step 7: Call H.add_edges_from()

```python
H.add_edges_from(G.edges())
```

**Verification:**
```python
assert len(G.nodes[0]) == 1
```

### Step 8: Assign ddict = value

```python
ddict = G.adj[1][2][0] if G.is_multigraph() else G.adj[1][2]
```

**Verification:**
```python
assert len(ddict) == 1
```

### Step 9: Assign ddict = value

```python
ddict = H.adj[1][2][0] if H.is_multigraph() else H.adj[1][2]
```

**Verification:**
```python
assert len(ddict) == 0
```


## Complete Example

```python
# Workflow
G = self.Graph()
G.add_node(0)
G.add_edge(1, 2)
self.add_attributes(G)
H = G.__class__()
H.add_nodes_from(G)
H.add_edges_from(G.edges())
assert len(G.nodes[0]) == 1
ddict = G.adj[1][2][0] if G.is_multigraph() else G.adj[1][2]
assert len(ddict) == 1
assert len(H.nodes[0]) == 0
ddict = H.adj[1][2][0] if H.is_multigraph() else H.adj[1][2]
assert len(ddict) == 0
```

## Next Steps


---

*Source: test_graph.py:286 | Complexity: Advanced | Last updated: 2026-06-02*