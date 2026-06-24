# How To: All Shorpaths

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all shortest paths

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3))
```

### Step 2: Call nx.add_path()

```python
nx.add_path(G, [0, 1, 2, 3])
```

**Verification:**
```python
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight'))
```

### Step 3: Call nx.add_path()

```python
nx.add_path(G, [0, 10, 20, 3])
```

**Verification:**
```python
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight', method='dijkstra'))
```

### Step 4: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight', method='bellman-ford'))
```

### Step 5: Call nx.add_path()

```python
nx.add_path(G, [0, 1, 2, 3])
```

### Step 6: Call nx.add_path()

```python
nx.add_path(G, [0, 10, 20, 3])
```

**Verification:**
```python
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight'))
```

### Step 7: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 8: Call nx.add_path()

```python
nx.add_path(G, [0, 1, 2, 3])
```

### Step 9: Call nx.add_path()

```python
nx.add_path(G, [0, 10, 20, 3])
```

**Verification:**
```python
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight', method='dijkstra'))
```

### Step 10: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 11: Call nx.add_path()

```python
nx.add_path(G, [0, 1, 2, 3])
```

### Step 12: Call nx.add_path()

```python
nx.add_path(G, [0, 10, 20, 3])
```

**Verification:**
```python
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight', method='bellman-ford'))
```


## Complete Example

```python
# Workflow
G = nx.Graph()
nx.add_path(G, [0, 1, 2, 3])
nx.add_path(G, [0, 10, 20, 3])
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3))
G = nx.Graph()
nx.add_path(G, [0, 1, 2, 3])
nx.add_path(G, [0, 10, 20, 3])
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight'))
G = nx.Graph()
nx.add_path(G, [0, 1, 2, 3])
nx.add_path(G, [0, 10, 20, 3])
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight', method='dijkstra'))
G = nx.Graph()
nx.add_path(G, [0, 1, 2, 3])
nx.add_path(G, [0, 10, 20, 3])
assert [[0, 1, 2, 3], [0, 10, 20, 3]] == sorted(nx.all_shortest_paths(G, 0, 3, weight='weight', method='bellman-ford'))
```

## Next Steps


---

*Source: test_generic.py:348 | Complexity: Advanced | Last updated: 2026-06-02*