# How To: Edgelists

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test edgelists

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.convert`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign P = nx.path_graph(...)

```python
P = nx.path_graph(4)
```

**Verification:**
```python
assert nodes_equal(sorted(G.nodes()), sorted(P.nodes()))
```

### Step 2: Assign e = value

```python
e = [(0, 1), (1, 2), (2, 3)]
```

**Verification:**
```python
assert edges_equal(sorted(G.edges()), sorted(P.edges()))
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph(e)
```

**Verification:**
```python
assert edges_equal(sorted(G.edges(data=True)), sorted(P.edges(data=True)))
```

### Step 4: Assign e = value

```python
e = [(0, 1, {}), (1, 2, {}), (2, 3, {})]
```

**Verification:**
```python
assert nodes_equal(sorted(G.nodes()), sorted(P.nodes()))
```

### Step 5: Assign G = nx.Graph(...)

```python
G = nx.Graph(e)
```

**Verification:**
```python
assert edges_equal(sorted(G.edges()), sorted(P.edges()))
```

### Step 6: Assign e = value

```python
e = ((n, n + 1) for n in range(3))
```

**Verification:**
```python
assert edges_equal(sorted(G.edges(data=True)), sorted(P.edges(data=True)))
```

### Step 7: Assign G = nx.Graph(...)

```python
G = nx.Graph(e)
```

**Verification:**
```python
assert nodes_equal(sorted(G.nodes()), sorted(P.nodes()))
```


## Complete Example

```python
# Workflow
P = nx.path_graph(4)
e = [(0, 1), (1, 2), (2, 3)]
G = nx.Graph(e)
assert nodes_equal(sorted(G.nodes()), sorted(P.nodes()))
assert edges_equal(sorted(G.edges()), sorted(P.edges()))
assert edges_equal(sorted(G.edges(data=True)), sorted(P.edges(data=True)))
e = [(0, 1, {}), (1, 2, {}), (2, 3, {})]
G = nx.Graph(e)
assert nodes_equal(sorted(G.nodes()), sorted(P.nodes()))
assert edges_equal(sorted(G.edges()), sorted(P.edges()))
assert edges_equal(sorted(G.edges(data=True)), sorted(P.edges(data=True)))
e = ((n, n + 1) for n in range(3))
G = nx.Graph(e)
assert nodes_equal(sorted(G.nodes()), sorted(P.nodes()))
assert edges_equal(sorted(G.edges()), sorted(P.edges()))
assert edges_equal(sorted(G.edges(data=True)), sorted(P.edges(data=True)))
```

## Next Steps


---

*Source: test_convert.py:212 | Complexity: Intermediate | Last updated: 2026-06-02*