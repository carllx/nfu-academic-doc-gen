# How To: All Pairs Shorpath Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs shortest path length

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.cycle))
```

**Verification:**
```python
assert ans[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
```

### Step 2: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.grid))
```

**Verification:**
```python
assert ans == dict(nx.all_pairs_shortest_path_length(self.cycle))
```

### Step 3: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.cycle, weight='weight'))
```

**Verification:**
```python
assert ans[1][16] == 6
```

### Step 4: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.grid, weight='weight'))
```

**Verification:**
```python
assert ans[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
```

### Step 5: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.cycle, weight='weight', method='dijkstra'))
```

**Verification:**
```python
assert ans == dict(nx.all_pairs_dijkstra_path_length(self.cycle))
```

### Step 6: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.cycle, weight='weight', method='bellman-ford'))
```

**Verification:**
```python
assert ans[1][16] == 6
```


## Complete Example

```python
# Workflow
ans = dict(nx.shortest_path_length(self.cycle))
assert ans[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == dict(nx.all_pairs_shortest_path_length(self.cycle))
ans = dict(nx.shortest_path_length(self.grid))
assert ans[1][16] == 6
ans = dict(nx.shortest_path_length(self.cycle, weight='weight'))
assert ans[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == dict(nx.all_pairs_dijkstra_path_length(self.cycle))
ans = dict(nx.shortest_path_length(self.grid, weight='weight'))
assert ans[1][16] == 6
ans = dict(nx.shortest_path_length(self.cycle, weight='weight', method='dijkstra'))
assert ans[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == dict(nx.all_pairs_dijkstra_path_length(self.cycle))
ans = dict(nx.shortest_path_length(self.cycle, weight='weight', method='bellman-ford'))
assert ans[0] == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == dict(nx.all_pairs_bellman_ford_path_length(self.cycle))
```

## Next Steps


---

*Source: test_generic.py:297 | Complexity: Intermediate | Last updated: 2026-06-02*