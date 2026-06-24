# How To: Single Source All Shorpaths

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single source all shortest paths

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign cycle_ans = value

```python
cycle_ans = {0: [[0]], 1: [[0, 1]], 2: [[0, 1, 2], [0, 3, 2]], 3: [[0, 3]]}
```

**Verification:**
```python
assert sorted(ans[2]) == cycle_ans[2]
```

### Step 2: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(nx.cycle_graph(4), 0))
```

**Verification:**
```python
assert sorted(ans[11]) == grid_ans
```

### Step 3: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(self.grid, 1))
```

**Verification:**
```python
assert sorted(ans[2]) == cycle_ans[2]
```

### Step 4: Assign grid_ans = value

```python
grid_ans = [[1, 2, 3, 7, 11], [1, 2, 6, 7, 11], [1, 2, 6, 10, 11], [1, 5, 6, 7, 11], [1, 5, 6, 10, 11], [1, 5, 9, 10, 11]]
```

**Verification:**
```python
assert sorted(ans[2]) == cycle_ans[2]
```

### Step 5: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(nx.cycle_graph(4), 0, weight='weight'))
```

**Verification:**
```python
assert sorted(ans[11]) == grid_ans
```

### Step 6: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(nx.cycle_graph(4), 0, method='bellman-ford', weight='weight'))
```

**Verification:**
```python
assert sorted(ans[11]) == grid_ans
```

### Step 7: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(self.grid, 1, weight='weight'))
```

**Verification:**
```python
assert sorted(ans[2]) == [[0, 1, 2], [0, 3, 2]]
```

### Step 8: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(self.grid, 1, method='bellman-ford', weight='weight'))
```

**Verification:**
```python
assert sorted(ans[4]) == [[4]]
```

### Step 9: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4)
```

### Step 10: Call G.add_node()

```python
G.add_node(4)
```

### Step 11: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(G, 0))
```

**Verification:**
```python
assert sorted(ans[2]) == [[0, 1, 2], [0, 3, 2]]
```

### Step 12: Assign ans = dict(...)

```python
ans = dict(nx.single_source_all_shortest_paths(G, 4))
```

**Verification:**
```python
assert sorted(ans[4]) == [[4]]
```


## Complete Example

```python
# Workflow
cycle_ans = {0: [[0]], 1: [[0, 1]], 2: [[0, 1, 2], [0, 3, 2]], 3: [[0, 3]]}
ans = dict(nx.single_source_all_shortest_paths(nx.cycle_graph(4), 0))
assert sorted(ans[2]) == cycle_ans[2]
ans = dict(nx.single_source_all_shortest_paths(self.grid, 1))
grid_ans = [[1, 2, 3, 7, 11], [1, 2, 6, 7, 11], [1, 2, 6, 10, 11], [1, 5, 6, 7, 11], [1, 5, 6, 10, 11], [1, 5, 9, 10, 11]]
assert sorted(ans[11]) == grid_ans
ans = dict(nx.single_source_all_shortest_paths(nx.cycle_graph(4), 0, weight='weight'))
assert sorted(ans[2]) == cycle_ans[2]
ans = dict(nx.single_source_all_shortest_paths(nx.cycle_graph(4), 0, method='bellman-ford', weight='weight'))
assert sorted(ans[2]) == cycle_ans[2]
ans = dict(nx.single_source_all_shortest_paths(self.grid, 1, weight='weight'))
assert sorted(ans[11]) == grid_ans
ans = dict(nx.single_source_all_shortest_paths(self.grid, 1, method='bellman-ford', weight='weight'))
assert sorted(ans[11]) == grid_ans
G = nx.cycle_graph(4)
G.add_node(4)
ans = dict(nx.single_source_all_shortest_paths(G, 0))
assert sorted(ans[2]) == [[0, 1, 2], [0, 3, 2]]
ans = dict(nx.single_source_all_shortest_paths(G, 4))
assert sorted(ans[4]) == [[4]]
```

## Next Steps


---

*Source: test_generic.py:236 | Complexity: Advanced | Last updated: 2026-06-02*