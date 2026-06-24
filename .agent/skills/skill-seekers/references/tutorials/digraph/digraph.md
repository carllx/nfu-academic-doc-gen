# How To: Digraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test digraph

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms`

**Setup Required:**
```python
# Fixtures: graph_constructor
```

## Step-by-Step Guide

### Step 1: Assign g1a = graph_constructor(...)

```python
g1a = graph_constructor(self.g1a_edges)
```

**Verification:**
```python
assert iso.ISMAGS(g1a, g2b).is_isomorphic()
```

### Step 2: Assign g1b = graph_constructor(...)

```python
g1b = graph_constructor(self.g1b_edges)
```

**Verification:**
```python
assert iso.ISMAGS(g1b, g2a).is_isomorphic()
```

### Step 3: Assign g2a = graph_constructor(...)

```python
g2a = graph_constructor(self.g2a_edges)
```

**Verification:**
```python
assert not iso.ISMAGS(g1a, g1b).is_isomorphic()
```

### Step 4: Assign g2b = graph_constructor(...)

```python
g2b = graph_constructor(self.g2b_edges)
```

**Verification:**
```python
assert not iso.ISMAGS(g2a, g2b).is_isomorphic()
```

### Step 5: Assign P2 = nx.path_graph(...)

```python
P2 = nx.path_graph(range(2), create_using=graph_constructor)
```

**Verification:**
```python
assert not iso.ISMAGS(g1a, g2a).is_isomorphic()
```

### Step 6: Assign P3 = nx.path_graph(...)

```python
P3 = nx.path_graph(range(3), create_using=graph_constructor)
```

**Verification:**
```python
assert not iso.ISMAGS(g1b, g2b).is_isomorphic()
```


## Complete Example

```python
# Setup
# Fixtures: graph_constructor

# Workflow
g1a = graph_constructor(self.g1a_edges)
g1b = graph_constructor(self.g1b_edges)
g2a = graph_constructor(self.g2a_edges)
g2b = graph_constructor(self.g2b_edges)
assert iso.ISMAGS(g1a, g2b).is_isomorphic()
assert iso.ISMAGS(g1b, g2a).is_isomorphic()
assert not iso.ISMAGS(g1a, g1b).is_isomorphic()
assert not iso.ISMAGS(g2a, g2b).is_isomorphic()
assert not iso.ISMAGS(g1a, g2a).is_isomorphic()
assert not iso.ISMAGS(g1b, g2b).is_isomorphic()
P2 = nx.path_graph(range(2), create_using=graph_constructor)
assert iso.ISMAGS(g1a, P2).subgraph_is_isomorphic()
P3 = nx.path_graph(range(3), create_using=graph_constructor)
assert not iso.ISMAGS(g1a, P3).subgraph_is_isomorphic()
```

## Next Steps


---

*Source: test_ismags.py:406 | Complexity: Intermediate | Last updated: 2026-06-02*