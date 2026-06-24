# How To: Heuristic First Steps

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test first steps of min_fill_in heuristic

## Prerequisites

**Required Modules:**
- `itertools`
- `networkx`
- `networkx.algorithms.approximation`
- `networkx.algorithms.approximation.treewidth`


## Step-by-Step Guide

### Step 1: 'Test first steps of min_fill_in heuristic'

```python
'Test first steps of min_fill_in heuristic'
```

**Verification:**
```python
assert steps[:2] == [6, 5]
```

### Step 2: Assign graph = value

```python
graph = {n: set(self.deterministic_graph[n]) - {n} for n in self.deterministic_graph}
```

### Step 3: Assign elim_node = min_fill_in_heuristic(...)

```python
elim_node = min_fill_in_heuristic(graph)
```

### Step 4: Assign steps = value

```python
steps = []
```

**Verification:**
```python
assert steps[:2] == [6, 5]
```

### Step 5: Call steps.append()

```python
steps.append(elim_node)
```

### Step 6: Assign nbrs = value

```python
nbrs = graph[elim_node]
```

### Step 7: Assign elim_node = min_fill_in_heuristic(...)

```python
elim_node = min_fill_in_heuristic(graph)
```

### Step 8: Call unknown.add()

```python
graph[u].add(v)
```

### Step 9: Call unknown.remove()

```python
graph[u].remove(elim_node)
```


## Complete Example

```python
# Workflow
'Test first steps of min_fill_in heuristic'
graph = {n: set(self.deterministic_graph[n]) - {n} for n in self.deterministic_graph}
elim_node = min_fill_in_heuristic(graph)
steps = []
while elim_node is not None:
    steps.append(elim_node)
    nbrs = graph[elim_node]
    for u, v in itertools.permutations(nbrs, 2):
        if v not in graph[u]:
            graph[u].add(v)
    for u in graph:
        if elim_node in graph[u]:
            graph[u].remove(elim_node)
    del graph[elim_node]
    elim_node = min_fill_in_heuristic(graph)
assert steps[:2] == [6, 5]
```

## Next Steps


---

*Source: test_treewidth.py:250 | Complexity: Advanced | Last updated: 2026-06-02*