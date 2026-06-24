# How To: Shorpath Length Target

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shortest path length target

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign answer = value

```python
answer = {0: 1, 1: 0, 2: 1}
```

**Verification:**
```python
assert sp == answer
```

### Step 2: Assign sp = nx.shortest_path_length(...)

```python
sp = nx.shortest_path_length(nx.path_graph(3), target=1)
```

**Verification:**
```python
assert sp == answer
```

### Step 3: Assign sp = nx.shortest_path_length(...)

```python
sp = nx.shortest_path_length(nx.path_graph(3), target=1, weight='weight')
```

**Verification:**
```python
assert sp == answer
```

### Step 4: Assign sp = nx.shortest_path_length(...)

```python
sp = nx.shortest_path_length(nx.path_graph(3), target=1, weight='weight', method='dijkstra')
```

**Verification:**
```python
assert sp == answer
```

### Step 5: Assign sp = nx.shortest_path_length(...)

```python
sp = nx.shortest_path_length(nx.path_graph(3), target=1, weight='weight', method='bellman-ford')
```

**Verification:**
```python
assert sp == answer
```


## Complete Example

```python
# Workflow
answer = {0: 1, 1: 0, 2: 1}
sp = nx.shortest_path_length(nx.path_graph(3), target=1)
assert sp == answer
sp = nx.shortest_path_length(nx.path_graph(3), target=1, weight='weight')
assert sp == answer
sp = nx.shortest_path_length(nx.path_graph(3), target=1, weight='weight', method='dijkstra')
assert sp == answer
sp = nx.shortest_path_length(nx.path_graph(3), target=1, weight='weight', method='bellman-ford')
assert sp == answer
```

## Next Steps


---

*Source: test_generic.py:173 | Complexity: Intermediate | Last updated: 2026-06-02*