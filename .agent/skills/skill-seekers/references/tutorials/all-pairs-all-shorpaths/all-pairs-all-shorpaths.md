# How To: All Pairs All Shorpaths

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs all shortest paths

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign ans = dict(...)

```python
ans = dict(nx.all_pairs_all_shortest_paths(nx.cycle_graph(4)))
```

**Verification:**
```python
assert sorted(ans[1][3]) == [[1, 0, 3], [1, 2, 3]]
```

### Step 2: Assign ans = dict(...)

```python
ans = dict(nx.all_pairs_all_shortest_paths(nx.cycle_graph(4)), weight='weight')
```

**Verification:**
```python
assert sorted(ans[1][3]) == [[1, 0, 3], [1, 2, 3]]
```

### Step 3: Assign ans = dict(...)

```python
ans = dict(nx.all_pairs_all_shortest_paths(nx.cycle_graph(4)), method='bellman-ford', weight='weight')
```

**Verification:**
```python
assert sorted(ans[1][3]) == [[1, 0, 3], [1, 2, 3]]
```

### Step 4: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4)
```

**Verification:**
```python
assert sorted(ans[4][4]) == [[4]]
```

### Step 5: Call G.add_node()

```python
G.add_node(4)
```

### Step 6: Assign ans = dict(...)

```python
ans = dict(nx.all_pairs_all_shortest_paths(G))
```

**Verification:**
```python
assert sorted(ans[4][4]) == [[4]]
```


## Complete Example

```python
# Workflow
ans = dict(nx.all_pairs_all_shortest_paths(nx.cycle_graph(4)))
assert sorted(ans[1][3]) == [[1, 0, 3], [1, 2, 3]]
ans = dict(nx.all_pairs_all_shortest_paths(nx.cycle_graph(4)), weight='weight')
assert sorted(ans[1][3]) == [[1, 0, 3], [1, 2, 3]]
ans = dict(nx.all_pairs_all_shortest_paths(nx.cycle_graph(4)), method='bellman-ford', weight='weight')
assert sorted(ans[1][3]) == [[1, 0, 3], [1, 2, 3]]
G = nx.cycle_graph(4)
G.add_node(4)
ans = dict(nx.all_pairs_all_shortest_paths(G))
assert sorted(ans[4][4]) == [[4]]
```

## Next Steps


---

*Source: test_generic.py:321 | Complexity: Intermediate | Last updated: 2026-06-02*