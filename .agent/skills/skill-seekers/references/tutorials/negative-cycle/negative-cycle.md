# How To: Negative Cycle

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test negative cycle

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `random`


## Step-by-Step Guide

### Step 1: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(5, create_using=nx.DiGraph())
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2, weight=-7)
```

### Step 3: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(5)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(1, 2, weight=-3)
```

### Step 5: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 1, {'weight': -1})])
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, 1)
```

### Step 7: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, 1)
```

### Step 8: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, 1)
```

### Step 9: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, 1)
```

### Step 10: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, 1)
```

### Step 11: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph([(1, 1, {'weight': -1})])
```

### Step 12: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, 1)
```

### Step 13: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, 1)
```

### Step 14: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, 1)
```

### Step 15: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, 1)
```

### Step 16: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, 1)
```

### Step 17: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, i)
```

### Step 18: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, i)
```

### Step 19: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, i)
```

### Step 20: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, i)
```

### Step 21: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, i)
```

### Step 22: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, i)
```

### Step 23: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, i)
```

### Step 24: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, i)
```

### Step 25: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, i)
```

### Step 26: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, i)
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(5, create_using=nx.DiGraph())
G.add_edge(1, 2, weight=-7)
for i in range(5):
    pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, i)
G = nx.cycle_graph(5)
G.add_edge(1, 2, weight=-3)
for i in range(5):
    pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, i)
    pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, i)
G = nx.DiGraph([(1, 1, {'weight': -1})])
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, 1)
G = nx.MultiDiGraph([(1, 1, {'weight': -1})])
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford_path_length, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.single_source_bellman_ford, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.bellman_ford_predecessor_and_distance, G, 1)
pytest.raises(nx.NetworkXUnbounded, nx.goldberg_radzik, G, 1)
```

## Next Steps


---

*Source: test_weighted.py:562 | Complexity: Advanced | Last updated: 2026-06-02*