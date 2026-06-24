# How To: Directed Projection

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed projection

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
```

### Step 2: Call G.add_edge()

```python
G.add_edge('A', 1)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 'B')
```

**Verification:**
```python
assert P['A']['B']['weight'] == 1
```

### Step 4: Call G.add_edge()

```python
G.add_edge('A', 2)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
```

### Step 5: Call G.add_edge()

```python
G.add_edge('B', 2)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
```

### Step 6: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, 'AB')
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
```

### Step 7: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, 'AB')
```

**Verification:**
```python
assert P['A']['B']['weight'] == 2
```

### Step 8: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, 'AB', multigraph=True)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B'), ('A', 'B')], directed=True)
```

### Step 9: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 10: Call G.add_edge()

```python
G.add_edge('A', 1)
```

### Step 11: Call G.add_edge()

```python
G.add_edge(1, 'B')
```

### Step 12: Call G.add_edge()

```python
G.add_edge('A', 2)
```

### Step 13: Call G.add_edge()

```python
G.add_edge(2, 'B')
```

### Step 14: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, 'AB')
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
```

### Step 15: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(G, 'AB')
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
```

### Step 16: Assign P = bipartite.projected_graph(...)

```python
P = bipartite.projected_graph(G, 'AB', multigraph=True)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), [('A', 'B'), ('A', 'B')], directed=True)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge('A', 1)
G.add_edge(1, 'B')
G.add_edge('A', 2)
G.add_edge('B', 2)
P = bipartite.projected_graph(G, 'AB')
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
P = bipartite.weighted_projected_graph(G, 'AB')
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
assert P['A']['B']['weight'] == 1
P = bipartite.projected_graph(G, 'AB', multigraph=True)
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
G = nx.DiGraph()
G.add_edge('A', 1)
G.add_edge(1, 'B')
G.add_edge('A', 2)
G.add_edge(2, 'B')
P = bipartite.projected_graph(G, 'AB')
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
P = bipartite.weighted_projected_graph(G, 'AB')
assert edges_equal(list(P.edges()), [('A', 'B')], directed=True)
assert P['A']['B']['weight'] == 2
P = bipartite.projected_graph(G, 'AB', multigraph=True)
assert edges_equal(list(P.edges()), [('A', 'B'), ('A', 'B')], directed=True)
```

## Next Steps


---

*Source: test_project.py:129 | Complexity: Advanced | Last updated: 2026-06-02*