# How To: Project Weighted Shared

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test project weighted shared

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [('A', 'B', 2), ('A', 'C', 1), ('B', 'C', 1), ('B', 'D', 1), ('B', 'E', 2), ('E', 'F', 1)]
```

**Verification:**
```python
assert edges_equal(list(P.edges()), Panswer.edges())
```

### Step 2: Assign Panswer = nx.Graph(...)

```python
Panswer = nx.Graph()
```

**Verification:**
```python
assert P[u][v]['weight'] == Panswer[u][v]['weight']
```

### Step 3: Call Panswer.add_weighted_edges_from()

```python
Panswer.add_weighted_edges_from(edges)
```

**Verification:**
```python
assert edges_equal(list(P.edges()), Panswer.edges())
```

### Step 4: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(self.G, 'ABCDEF')
```

**Verification:**
```python
assert P[u][v]['weight'] == Panswer[u][v]['weight']
```

### Step 5: Assign edges = value

```python
edges = [('A', 'B', 3), ('A', 'E', 1), ('A', 'C', 1), ('A', 'D', 1), ('B', 'E', 1), ('B', 'C', 1), ('B', 'D', 1), ('C', 'D', 1)]
```

### Step 6: Assign Panswer = nx.Graph(...)

```python
Panswer = nx.Graph()
```

### Step 7: Call Panswer.add_weighted_edges_from()

```python
Panswer.add_weighted_edges_from(edges)
```

### Step 8: Assign P = bipartite.weighted_projected_graph(...)

```python
P = bipartite.weighted_projected_graph(self.N, 'ABCDE')
```

**Verification:**
```python
assert edges_equal(list(P.edges()), Panswer.edges())
```


## Complete Example

```python
# Workflow
edges = [('A', 'B', 2), ('A', 'C', 1), ('B', 'C', 1), ('B', 'D', 1), ('B', 'E', 2), ('E', 'F', 1)]
Panswer = nx.Graph()
Panswer.add_weighted_edges_from(edges)
P = bipartite.weighted_projected_graph(self.G, 'ABCDEF')
assert edges_equal(list(P.edges()), Panswer.edges())
for u, v in list(P.edges()):
    assert P[u][v]['weight'] == Panswer[u][v]['weight']
edges = [('A', 'B', 3), ('A', 'E', 1), ('A', 'C', 1), ('A', 'D', 1), ('B', 'E', 1), ('B', 'C', 1), ('B', 'D', 1), ('C', 'D', 1)]
Panswer = nx.Graph()
Panswer.add_weighted_edges_from(edges)
P = bipartite.weighted_projected_graph(self.N, 'ABCDE')
assert edges_equal(list(P.edges()), Panswer.edges())
for u, v in list(P.edges()):
    assert P[u][v]['weight'] == Panswer[u][v]['weight']
```

## Next Steps


---

*Source: test_project.py:190 | Complexity: Advanced | Last updated: 2026-06-02*