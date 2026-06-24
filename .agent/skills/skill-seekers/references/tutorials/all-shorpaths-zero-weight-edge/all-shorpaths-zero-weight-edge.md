# How To: All Shorpaths Zero Weight Edge

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all shortest paths zero weight edge

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign g = nx.Graph(...)

```python
g = nx.Graph()
```

**Verification:**
```python
assert sorted(paths03d) == sorted((p[::-1] for p in paths30d))
```

### Step 2: Call nx.add_path()

```python
nx.add_path(g, [0, 1, 3])
```

**Verification:**
```python
assert sorted(paths03d) == sorted((p[::-1] for p in paths30b))
```

### Step 3: Call nx.add_path()

```python
nx.add_path(g, [0, 1, 2, 3])
```

**Verification:**
```python
assert sorted(paths03b) == sorted((p[::-1] for p in paths30b))
```

### Step 4: Assign unknown = 0

```python
g.edges[1, 2]['weight'] = 0
```

### Step 5: Assign paths30d = list(...)

```python
paths30d = list(nx.all_shortest_paths(g, 3, 0, weight='weight', method='dijkstra'))
```

### Step 6: Assign paths03d = list(...)

```python
paths03d = list(nx.all_shortest_paths(g, 0, 3, weight='weight', method='dijkstra'))
```

### Step 7: Assign paths30b = list(...)

```python
paths30b = list(nx.all_shortest_paths(g, 3, 0, weight='weight', method='bellman-ford'))
```

### Step 8: Assign paths03b = list(...)

```python
paths03b = list(nx.all_shortest_paths(g, 0, 3, weight='weight', method='bellman-ford'))
```

**Verification:**
```python
assert sorted(paths03d) == sorted((p[::-1] for p in paths30d))
```


## Complete Example

```python
# Workflow
g = nx.Graph()
nx.add_path(g, [0, 1, 3])
nx.add_path(g, [0, 1, 2, 3])
g.edges[1, 2]['weight'] = 0
paths30d = list(nx.all_shortest_paths(g, 3, 0, weight='weight', method='dijkstra'))
paths03d = list(nx.all_shortest_paths(g, 0, 3, weight='weight', method='dijkstra'))
paths30b = list(nx.all_shortest_paths(g, 3, 0, weight='weight', method='bellman-ford'))
paths03b = list(nx.all_shortest_paths(g, 0, 3, weight='weight', method='bellman-ford'))
assert sorted(paths03d) == sorted((p[::-1] for p in paths30d))
assert sorted(paths03d) == sorted((p[::-1] for p in paths30b))
assert sorted(paths03b) == sorted((p[::-1] for p in paths30b))
```

## Next Steps


---

*Source: test_generic.py:394 | Complexity: Advanced | Last updated: 2026-06-02*