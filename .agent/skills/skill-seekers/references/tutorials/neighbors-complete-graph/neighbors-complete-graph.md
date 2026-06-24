# How To: Neighbors Complete Graph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test neighbors complete graph

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
assert len(nbors) == len(graph) - 1
```

### Step 2: Assign pop = random.sample(...)

```python
pop = random.sample(list(graph), 1)
```

**Verification:**
```python
assert len(nbors) == 2
```

### Step 3: Assign nbors = list(...)

```python
nbors = list(nx.neighbors(graph, pop[0]))
```

**Verification:**
```python
assert len(nbors) == 1
```

### Step 4: Assign graph = nx.path_graph(...)

```python
graph = nx.path_graph(100)
```

**Verification:**
```python
assert len(nbors) == 99
```

### Step 5: Assign node = value

```python
node = random.sample(list(graph), 1)[0]
```

### Step 6: Assign nbors = list(...)

```python
nbors = list(nx.neighbors(graph, node))
```

### Step 7: Assign graph = nx.star_graph(...)

```python
graph = nx.star_graph(99)
```

### Step 8: Assign nbors = list(...)

```python
nbors = list(nx.neighbors(graph, 0))
```

**Verification:**
```python
assert len(nbors) == 99
```


## Complete Example

```python
# Workflow
graph = nx.complete_graph(100)
pop = random.sample(list(graph), 1)
nbors = list(nx.neighbors(graph, pop[0]))
assert len(nbors) == len(graph) - 1
graph = nx.path_graph(100)
node = random.sample(list(graph), 1)[0]
nbors = list(nx.neighbors(graph, node))
if node != 0 and node != 99:
    assert len(nbors) == 2
else:
    assert len(nbors) == 1
graph = nx.star_graph(99)
nbors = list(nx.neighbors(graph, 0))
assert len(nbors) == 99
```

## Next Steps


---

*Source: test_function.py:291 | Complexity: Advanced | Last updated: 2026-06-02*