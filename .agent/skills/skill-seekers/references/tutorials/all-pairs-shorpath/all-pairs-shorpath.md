# How To: All Pairs Shorpath

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs shortest path

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign p = dict(...)

```python
p = dict(nx.shortest_path(self.cycle))
```

**Verification:**
```python
assert p[0][3] == [0, 1, 2, 3]
```

### Step 2: Assign p = dict(...)

```python
p = dict(nx.shortest_path(self.grid))
```

**Verification:**
```python
assert p == dict(nx.all_pairs_shortest_path(self.cycle))
```

### Step 3: Call validate_grid_path()

```python
validate_grid_path(4, 4, 1, 12, p[1][12])
```

**Verification:**
```python
assert p[0][3] == [0, 1, 2, 3]
```

### Step 4: Assign p = dict(...)

```python
p = dict(nx.shortest_path(self.cycle, weight='weight'))
```

**Verification:**
```python
assert p == dict(nx.all_pairs_dijkstra_path(self.cycle))
```

### Step 5: Assign p = dict(...)

```python
p = dict(nx.shortest_path(self.grid, weight='weight'))
```

**Verification:**
```python
assert p[0][3] == [0, 1, 2, 3]
```

### Step 6: Call validate_grid_path()

```python
validate_grid_path(4, 4, 1, 12, p[1][12])
```

**Verification:**
```python
assert p == dict(nx.all_pairs_dijkstra_path(self.cycle))
```

### Step 7: Assign p = dict(...)

```python
p = dict(nx.shortest_path(self.cycle, weight='weight', method='dijkstra'))
```

**Verification:**
```python
assert p[0][3] == [0, 1, 2, 3]
```

### Step 8: Assign p = dict(...)

```python
p = dict(nx.shortest_path(self.cycle, weight='weight', method='bellman-ford'))
```

**Verification:**
```python
assert p == dict(nx.all_pairs_bellman_ford_path(self.cycle))
```


## Complete Example

```python
# Workflow
p = dict(nx.shortest_path(self.cycle))
assert p[0][3] == [0, 1, 2, 3]
assert p == dict(nx.all_pairs_shortest_path(self.cycle))
p = dict(nx.shortest_path(self.grid))
validate_grid_path(4, 4, 1, 12, p[1][12])
p = dict(nx.shortest_path(self.cycle, weight='weight'))
assert p[0][3] == [0, 1, 2, 3]
assert p == dict(nx.all_pairs_dijkstra_path(self.cycle))
p = dict(nx.shortest_path(self.grid, weight='weight'))
validate_grid_path(4, 4, 1, 12, p[1][12])
p = dict(nx.shortest_path(self.cycle, weight='weight', method='dijkstra'))
assert p[0][3] == [0, 1, 2, 3]
assert p == dict(nx.all_pairs_dijkstra_path(self.cycle))
p = dict(nx.shortest_path(self.cycle, weight='weight', method='bellman-ford'))
assert p[0][3] == [0, 1, 2, 3]
assert p == dict(nx.all_pairs_bellman_ford_path(self.cycle))
```

## Next Steps


---

*Source: test_generic.py:275 | Complexity: Advanced | Last updated: 2026-06-02*