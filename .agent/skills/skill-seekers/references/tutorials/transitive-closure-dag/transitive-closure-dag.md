# How To: Transitive Closure Dag

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transitive closure dag

## Prerequisites

**Required Modules:**
- `collections`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (3, 4)])
```

**Verification:**
```python
assert edges_equal(transitive_closure(G).edges(), solution, directed=True)
```

### Step 2: Assign transitive_closure = value

```python
transitive_closure = nx.algorithms.dag.transitive_closure_dag
```

**Verification:**
```python
assert edges_equal(transitive_closure(G).edges(), solution, directed=True)
```

### Step 3: Assign solution = value

```python
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

**Verification:**
```python
assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
```

### Step 4: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (2, 4)])
```

**Verification:**
```python
assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
```

### Step 5: Assign solution = value

```python
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
```

**Verification:**
```python
assert edges_equal(transitive_closure(G).edges(), solution, directed=True)
```

### Step 6: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
```

### Step 7: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, transitive_closure, G)
```

### Step 8: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2, {'a': 3}), (2, 3, {'b': 0}), (3, 4)])
```

### Step 9: Assign H = transitive_closure(...)

```python
H = transitive_closure(G)
```

### Step 10: Assign k = 10

```python
k = 10
```

### Step 11: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(((i, i + 1, {'foo': 'bar', 'weight': i}) for i in range(k)))
```

### Step 12: Assign H = transitive_closure(...)

```python
H = transitive_closure(G)
```

**Verification:**
```python
assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph([(1, 2), (2, 3), (3, 4)])
transitive_closure = nx.algorithms.dag.transitive_closure_dag
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
assert edges_equal(transitive_closure(G).edges(), solution, directed=True)
G = nx.DiGraph([(1, 2), (2, 3), (2, 4)])
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
assert edges_equal(transitive_closure(G).edges(), solution, directed=True)
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
pytest.raises(nx.NetworkXNotImplemented, transitive_closure, G)
G = nx.DiGraph([(1, 2, {'a': 3}), (2, 3, {'b': 0}), (3, 4)])
H = transitive_closure(G)
for u, v in G.edges():
    assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
k = 10
G = nx.DiGraph(((i, i + 1, {'foo': 'bar', 'weight': i}) for i in range(k)))
H = transitive_closure(G)
for u, v in G.edges():
    assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
```

## Next Steps


---

*Source: test_dag.py:438 | Complexity: Advanced | Last updated: 2026-06-02*