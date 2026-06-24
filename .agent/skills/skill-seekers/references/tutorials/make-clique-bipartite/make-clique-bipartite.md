# How To: Make Clique Bipartite

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test make clique bipartite

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert sorted(B) == [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

### Step 2: Assign B = nx.make_clique_bipartite(...)

```python
B = nx.make_clique_bipartite(G)
```

**Verification:**
```python
assert H.adj == G.adj
```

### Step 3: Assign H = nx.projected_graph(...)

```python
H = nx.projected_graph(B, range(1, 12))
```

**Verification:**
```python
assert sorted(H1) == [1, 2, 3, 4, 5]
```

### Step 4: Assign H1 = nx.projected_graph(...)

```python
H1 = nx.projected_graph(B, range(-5, 0))
```

### Step 5: Assign H1 = nx.relabel_nodes(...)

```python
H1 = nx.relabel_nodes(H1, {-v: v for v in range(1, 6)})
```

**Verification:**
```python
assert sorted(H1) == [1, 2, 3, 4, 5]
```


## Complete Example

```python
# Workflow
G = self.G
B = nx.make_clique_bipartite(G)
assert sorted(B) == [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
H = nx.projected_graph(B, range(1, 12))
assert H.adj == G.adj
H1 = nx.projected_graph(B, range(-5, 0))
H1 = nx.relabel_nodes(H1, {-v: v for v in range(1, 6)})
assert sorted(H1) == [1, 2, 3, 4, 5]
```

## Next Steps


---

*Source: test_clique.py:176 | Complexity: Intermediate | Last updated: 2026-06-02*