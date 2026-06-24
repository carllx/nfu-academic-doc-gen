# How To: Transitive Closure

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transitive closure

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
assert edges_equal(nx.transitive_closure(G).edges(), solution, directed=True)
```

### Step 2: Assign solution = value

```python
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

**Verification:**
```python
assert edges_equal(nx.transitive_closure(G).edges(), solution, directed=True)
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (2, 4)])
```

**Verification:**
```python
assert edges_equal(sorted(nx.transitive_closure(G).edges()), soln, directed=True)
```

### Step 4: Assign solution = value

```python
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
```

**Verification:**
```python
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution)
```

### Step 5: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
```

**Verification:**
```python
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution)
```

### Step 6: Assign solution = value

```python
solution = [(1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)]
```

**Verification:**
```python
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution, directed=True)
```

### Step 7: Assign soln = sorted(...)

```python
soln = sorted(solution + [(n, n) for n in G])
```

**Verification:**
```python
assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
```

### Step 8: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
```

**Verification:**
```python
assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
```

### Step 9: Assign solution = value

```python
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

**Verification:**
```python
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution)
```

### Step 10: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph([(1, 2), (2, 3), (3, 4)])
```

### Step 11: Assign solution = value

```python
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

**Verification:**
```python
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution)
```

### Step 12: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph([(1, 2), (2, 3), (3, 4)])
```

### Step 13: Assign solution = value

```python
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

**Verification:**
```python
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution, directed=True)
```

### Step 14: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2, {'a': 3}), (2, 3, {'b': 0}), (3, 4)])
```

### Step 15: Assign H = nx.transitive_closure(...)

```python
H = nx.transitive_closure(G)
```

### Step 16: Assign k = 10

```python
k = 10
```

### Step 17: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(((i, i + 1, {'f': 'b', 'weight': i}) for i in range(k)))
```

### Step 18: Assign H = nx.transitive_closure(...)

```python
H = nx.transitive_closure(G)
```

### Step 19: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
```

### Step 20: Call nx.transitive_closure()

```python
nx.transitive_closure(G, reflexive='wrong input')
```


## Complete Example

```python
# Workflow
G = nx.DiGraph([(1, 2), (2, 3), (3, 4)])
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
assert edges_equal(nx.transitive_closure(G).edges(), solution, directed=True)
G = nx.DiGraph([(1, 2), (2, 3), (2, 4)])
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
assert edges_equal(nx.transitive_closure(G).edges(), solution, directed=True)
G = nx.DiGraph([(1, 2), (2, 3), (3, 1)])
solution = [(1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)]
soln = sorted(solution + [(n, n) for n in G])
assert edges_equal(sorted(nx.transitive_closure(G).edges()), soln, directed=True)
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution)
G = nx.MultiGraph([(1, 2), (2, 3), (3, 4)])
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution)
G = nx.MultiDiGraph([(1, 2), (2, 3), (3, 4)])
solution = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
assert edges_equal(sorted(nx.transitive_closure(G).edges()), solution, directed=True)
G = nx.DiGraph([(1, 2, {'a': 3}), (2, 3, {'b': 0}), (3, 4)])
H = nx.transitive_closure(G)
for u, v in G.edges():
    assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
k = 10
G = nx.DiGraph(((i, i + 1, {'f': 'b', 'weight': i}) for i in range(k)))
H = nx.transitive_closure(G)
for u, v in G.edges():
    assert G.get_edge_data(u, v) == H.get_edge_data(u, v)
G = nx.Graph()
with pytest.raises(nx.NetworkXError):
    nx.transitive_closure(G, reflexive='wrong input')
```

## Next Steps


---

*Source: test_dag.py:325 | Complexity: Advanced | Last updated: 2026-06-02*