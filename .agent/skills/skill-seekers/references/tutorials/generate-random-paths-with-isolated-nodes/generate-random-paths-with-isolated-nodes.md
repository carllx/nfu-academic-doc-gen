# How To: Generate Random Paths With Isolated Nodes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test generate random paths with isolated nodes

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.similarity`
- `networkx.generators.classic`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numpy')
```

**Verification:**
```python
assert len(paths) == 2
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert all((len(path) == 3 for path in paths))
```

### Step 3: Call G.add_nodes_from()

```python
G.add_nodes_from([0, 1, 2])
```

**Verification:**
```python
assert all((path[0] == 0 for path in paths))
```

### Step 4: Call G.add_edge()

```python
G.add_edge(0, 1)
```

### Step 5: Assign paths = list(...)

```python
paths = list(nx.generate_random_paths(G, 2, path_length=2, source=0, seed=42))
```

**Verification:**
```python
assert len(paths) == 2
```

### Step 6: Assign path_gen = nx.generate_random_paths(...)

```python
path_gen = nx.generate_random_paths(G, 2, path_length=2, source=2, seed=42)
```

### Step 7: Assign path_gen = nx.generate_random_paths(...)

```python
path_gen = nx.generate_random_paths(G, 2, path_length=2, seed=42)
```

### Step 8: Call list()

```python
list(path_gen)
```

### Step 9: Call list()

```python
list(path_gen)
```


## Complete Example

```python
# Workflow
pytest.importorskip('numpy')
G = nx.Graph()
G.add_nodes_from([0, 1, 2])
G.add_edge(0, 1)
paths = list(nx.generate_random_paths(G, 2, path_length=2, source=0, seed=42))
assert len(paths) == 2
assert all((len(path) == 3 for path in paths))
assert all((path[0] == 0 for path in paths))
path_gen = nx.generate_random_paths(G, 2, path_length=2, source=2, seed=42)
with pytest.raises(ValueError, match='probabilities contain NaN'):
    list(path_gen)
path_gen = nx.generate_random_paths(G, 2, path_length=2, seed=42)
with pytest.raises(ValueError, match='probabilities contain NaN'):
    list(path_gen)
```

## Next Steps


---

*Source: test_similarity.py:28 | Complexity: Advanced | Last updated: 2026-06-02*