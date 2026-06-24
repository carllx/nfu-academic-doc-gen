# How To: Non Neighbors

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non neighbors

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign graph = nx.complete_graph(...)

```python
graph = nx.complete_graph(100)
```

**Verification:**
```python
assert len(nbors) == 0
```

### Step 2: Assign pop = random.sample(...)

```python
pop = random.sample(list(graph), 1)
```

**Verification:**
```python
assert len(nbors) == 97
```

### Step 3: Assign nbors = nx.non_neighbors(...)

```python
nbors = nx.non_neighbors(graph, pop[0])
```

**Verification:**
```python
assert len(nbors) == 98
```

### Step 4: Assign graph = nx.path_graph(...)

```python
graph = nx.path_graph(100)
```

**Verification:**
```python
assert len(nbors) == 0
```

### Step 5: Assign node = value

```python
node = random.sample(list(graph), 1)[0]
```

**Verification:**
```python
assert len(nbors) == 9
```

### Step 6: Assign nbors = nx.non_neighbors(...)

```python
nbors = nx.non_neighbors(graph, node)
```

### Step 7: Assign graph = nx.star_graph(...)

```python
graph = nx.star_graph(99)
```

### Step 8: Assign nbors = nx.non_neighbors(...)

```python
nbors = nx.non_neighbors(graph, 0)
```

**Verification:**
```python
assert len(nbors) == 0
```

### Step 9: Assign graph = nx.Graph(...)

```python
graph = nx.Graph()
```

### Step 10: Call graph.add_nodes_from()

```python
graph.add_nodes_from(range(10))
```

### Step 11: Assign nbors = nx.non_neighbors(...)

```python
nbors = nx.non_neighbors(graph, 0)
```

**Verification:**
```python
assert len(nbors) == 9
```


## Complete Example

```python
# Workflow
graph = nx.complete_graph(100)
pop = random.sample(list(graph), 1)
nbors = nx.non_neighbors(graph, pop[0])
assert len(nbors) == 0
graph = nx.path_graph(100)
node = random.sample(list(graph), 1)[0]
nbors = nx.non_neighbors(graph, node)
if node != 0 and node != 99:
    assert len(nbors) == 97
else:
    assert len(nbors) == 98
graph = nx.star_graph(99)
nbors = nx.non_neighbors(graph, 0)
assert len(nbors) == 0
graph = nx.Graph()
graph.add_nodes_from(range(10))
nbors = nx.non_neighbors(graph, 0)
assert len(nbors) == 9
```

## Next Steps


---

*Source: test_function.py:312 | Complexity: Advanced | Last updated: 2026-06-02*