# How To: Project Multigraph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test project multigraph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('a', 'b')])
```

### Step 2: Call G.add_edge()

```python
G.add_edge('a', 1)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('a', 'b')])
```

### Step 3: Call G.add_edge()

```python
G.add_edge('b', 1)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('a', 'b'), ('a', 'b')])
```

### Step 4: Call G.add_edge()

```python
G.add_edge('a', 2)
```

### Step 5: Call G.add_edge()

```python
G.add_edge('b', 2)
```

### Step 6: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, 'ab')
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('a', 'b')])
```

### Step 7: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, 'ab')
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('a', 'b')])
```

### Step 8: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, 'ab', multigraph=True)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('a', 'b'), ('a', 'b')])
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edge('a', 1)
G.add_edge('b', 1)
G.add_edge('a', 2)
G.add_edge('b', 2)
P = bipartite.projected_graph(G, 'ab')
assert edges_equal(list(P.edges()), [('a', 'b')])
P = bipartite.weighted_projected_graph(G, 'ab')
assert edges_equal(list(P.edges()), [('a', 'b')])
P = bipartite.projected_graph(G, 'ab', multigraph=True)
assert edges_equal(list(P.edges()), [('a', 'b'), ('a', 'b')])
```

## Next Steps


---

*Source: test_project.py:103 | Complexity: Advanced | Last updated: 2026-06-02*