# How To: Single Source Shorpath Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single source shortest path length

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign ans = nx.shortest_path_length(...)

```python
ans = nx.shortest_path_length(self.cycle, 0)
```

**Verification:**
```python
assert ans == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
```

### Step 2: Assign ans = nx.shortest_path_length(...)

```python
ans = nx.shortest_path_length(self.grid, 1)
```

**Verification:**
```python
assert ans == nx.single_source_shortest_path_length(self.cycle, 0)
```

### Step 3: Assign ans = nx.shortest_path_length(...)

```python
ans = nx.shortest_path_length(self.cycle, 0, weight='weight')
```

**Verification:**
```python
assert ans[16] == 6
```

### Step 4: Assign ans = nx.shortest_path_length(...)

```python
ans = nx.shortest_path_length(self.grid, 1, weight='weight')
```

**Verification:**
```python
assert ans == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
```

### Step 5: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.cycle, 0, weight='weight', method='dijkstra'))
```

**Verification:**
```python
assert ans == nx.single_source_dijkstra_path_length(self.cycle, 0)
```

### Step 6: Assign ans = dict(...)

```python
ans = dict(nx.shortest_path_length(self.cycle, 0, weight='weight', method='bellman-ford'))
```

**Verification:**
```python
assert ans[16] == 6
```


## Complete Example

```python
# Workflow
ans = nx.shortest_path_length(self.cycle, 0)
assert ans == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == nx.single_source_shortest_path_length(self.cycle, 0)
ans = nx.shortest_path_length(self.grid, 1)
assert ans[16] == 6
ans = nx.shortest_path_length(self.cycle, 0, weight='weight')
assert ans == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == nx.single_source_dijkstra_path_length(self.cycle, 0)
ans = nx.shortest_path_length(self.grid, 1, weight='weight')
assert ans[16] == 6
ans = dict(nx.shortest_path_length(self.cycle, 0, weight='weight', method='dijkstra'))
assert ans == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == nx.single_source_dijkstra_path_length(self.cycle, 0)
ans = dict(nx.shortest_path_length(self.cycle, 0, weight='weight', method='bellman-ford'))
assert ans == {0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 2, 6: 1}
assert ans == nx.single_source_bellman_ford_path_length(self.cycle, 0)
```

## Next Steps


---

*Source: test_generic.py:210 | Complexity: Intermediate | Last updated: 2026-06-02*