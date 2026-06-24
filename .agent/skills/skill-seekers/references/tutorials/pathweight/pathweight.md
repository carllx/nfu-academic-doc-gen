# How To: Pathweight

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pathweight

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign valid_path = value

```python
valid_path = [1, 2, 3]
```

**Verification:**
```python
assert nx.path_weight(graph, valid_path, 'cost') == 4
```

### Step 2: Assign invalid_path = value

```python
invalid_path = [1, 3, 2]
```

**Verification:**
```python
assert nx.path_weight(graph, valid_path, 'dist') == 6
```

### Step 3: Assign graphs = value

```python
graphs = [nx.Graph(), nx.DiGraph(), nx.MultiGraph(), nx.MultiDiGraph()]
```

### Step 4: Assign edges = value

```python
edges = [(1, 2, {'cost': 5, 'dist': 6}), (2, 3, {'cost': 3, 'dist': 4}), (1, 2, {'cost': 1, 'dist': 2})]
```

### Step 5: Call graph.add_edges_from()

```python
graph.add_edges_from(edges)
```

**Verification:**
```python
assert nx.path_weight(graph, valid_path, 'cost') == 4
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNoPath, nx.path_weight, graph, invalid_path, 'cost')
```


## Complete Example

```python
# Workflow
valid_path = [1, 2, 3]
invalid_path = [1, 3, 2]
graphs = [nx.Graph(), nx.DiGraph(), nx.MultiGraph(), nx.MultiDiGraph()]
edges = [(1, 2, {'cost': 5, 'dist': 6}), (2, 3, {'cost': 3, 'dist': 4}), (1, 2, {'cost': 1, 'dist': 2})]
for graph in graphs:
    graph.add_edges_from(edges)
    assert nx.path_weight(graph, valid_path, 'cost') == 4
    assert nx.path_weight(graph, valid_path, 'dist') == 6
    pytest.raises(nx.NetworkXNoPath, nx.path_weight, graph, invalid_path, 'cost')
```

## Next Steps


---

*Source: test_function.py:999 | Complexity: Intermediate | Last updated: 2026-06-02*