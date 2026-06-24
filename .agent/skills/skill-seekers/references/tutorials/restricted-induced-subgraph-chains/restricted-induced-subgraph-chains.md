# How To: Restricted Induced Subgraph Chains

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test subgraph chains that both restrict and show nodes/edges.

A restricted_view subgraph should allow induced subgraphs using
G.subgraph that automagically without a chain (meaning the result
is a subgraph view of the original graph not a subgraph-of-subgraph.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `pickle`
- `pickle`
- `pickle`
- `pickle`
- `pickle`


## Step-by-Step Guide

### Step 1: 'Test subgraph chains that both restrict and show nodes/edges.\n\n        A restricted_view subgraph should allow induced subgraphs using\n        G.subgraph that automagically without a chain (meaning the result\n        is a subgraph view of the original graph not a subgraph-of-subgraph.\n        '

```python
'Test subgraph chains that both restrict and show nodes/edges.\n\n        A restricted_view subgraph should allow induced subgraphs using\n        G.subgraph that automagically without a chain (meaning the result\n        is a subgraph view of the original graph not a subgraph-of-subgraph.\n        '
```

**Verification:**
```python
assert RG._graph is self.G
```

### Step 2: Assign hide_nodes = value

```python
hide_nodes = [3, 4, 5]
```

**Verification:**
```python
assert SSG._graph is self.G
```

### Step 3: Assign hide_edges = value

```python
hide_edges = [(6, 7)]
```

**Verification:**
```python
assert SG._graph is RG
```

### Step 4: Assign RG = nx.restricted_view(...)

```python
RG = nx.restricted_view(self.G, hide_nodes, hide_edges)
```

**Verification:**
```python
assert edges_equal(SG.edges, SSG.edges)
```

### Step 5: Assign nodes = value

```python
nodes = [4, 5, 6, 7, 8]
```

**Verification:**
```python
assert edges_equal(CG.edges(nodes), SSG.edges)
```

### Step 6: Assign SG = nx.induced_subgraph(...)

```python
SG = nx.induced_subgraph(RG, nodes)
```

**Verification:**
```python
assert edges_equal(CG.edges, SSG.edges)
```

### Step 7: Assign SSG = RG.subgraph(...)

```python
SSG = RG.subgraph(nodes)
```

**Verification:**
```python
assert RSG._graph is not self.G
```

### Step 8: Assign CG = self.G.copy(...)

```python
CG = self.G.copy()
```

**Verification:**
```python
assert edges_equal(RSG.edges, CG.edges)
```

### Step 9: Call CG.remove_nodes_from()

```python
CG.remove_nodes_from(hide_nodes)
```

### Step 10: Call CG.remove_edges_from()

```python
CG.remove_edges_from(hide_edges)
```

**Verification:**
```python
assert edges_equal(CG.edges(nodes), SSG.edges)
```

### Step 11: Call CG.remove_nodes_from()

```python
CG.remove_nodes_from([0, 1, 2, 3])
```

**Verification:**
```python
assert edges_equal(CG.edges, SSG.edges)
```

### Step 12: Assign SSSG = self.G.subgraph(...)

```python
SSSG = self.G.subgraph(nodes)
```

### Step 13: Assign RSG = nx.restricted_view(...)

```python
RSG = nx.restricted_view(SSSG, hide_nodes, hide_edges)
```

**Verification:**
```python
assert RSG._graph is not self.G
```


## Complete Example

```python
# Workflow
'Test subgraph chains that both restrict and show nodes/edges.\n\n        A restricted_view subgraph should allow induced subgraphs using\n        G.subgraph that automagically without a chain (meaning the result\n        is a subgraph view of the original graph not a subgraph-of-subgraph.\n        '
hide_nodes = [3, 4, 5]
hide_edges = [(6, 7)]
RG = nx.restricted_view(self.G, hide_nodes, hide_edges)
nodes = [4, 5, 6, 7, 8]
SG = nx.induced_subgraph(RG, nodes)
SSG = RG.subgraph(nodes)
assert RG._graph is self.G
assert SSG._graph is self.G
assert SG._graph is RG
assert edges_equal(SG.edges, SSG.edges)
CG = self.G.copy()
CG.remove_nodes_from(hide_nodes)
CG.remove_edges_from(hide_edges)
assert edges_equal(CG.edges(nodes), SSG.edges)
CG.remove_nodes_from([0, 1, 2, 3])
assert edges_equal(CG.edges, SSG.edges)
SSSG = self.G.subgraph(nodes)
RSG = nx.restricted_view(SSSG, hide_nodes, hide_edges)
assert RSG._graph is not self.G
assert edges_equal(RSG.edges, CG.edges)
```

## Next Steps


---

*Source: test_graphviews.py:223 | Complexity: Advanced | Last updated: 2026-06-02*