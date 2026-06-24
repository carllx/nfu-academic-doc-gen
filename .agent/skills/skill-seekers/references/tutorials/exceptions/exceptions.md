# How To: Exceptions

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test exceptions

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, nx.network_simplex, G)
```

### Step 3: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, nx.capacity_scaling, G)
```

### Step 4: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, nx.network_simplex, G)
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, nx.capacity_scaling, G)
```

### Step 7: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 8: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
```

### Step 9: Call G.add_node()

```python
G.add_node(0, demand=float('inf'))
```

### Step 10: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
```

### Step 11: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnfeasible, nx.capacity_scaling, G)
```

### Step 12: Assign unknown = 0

```python
G.nodes[0]['demand'] = 0
```

### Step 13: Call G.add_node()

```python
G.add_node(1, demand=0)
```

### Step 14: Call G.add_edge()

```python
G.add_edge(0, 1, weight=-float('inf'))
```

### Step 15: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
```

### Step 16: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnfeasible, nx.capacity_scaling, G)
```

### Step 17: Assign unknown = 0

```python
G[0][1]['weight'] = 0
```

### Step 18: Call G.add_edge()

```python
G.add_edge(0, 0, weight=float('inf'))
```

### Step 19: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
```

### Step 20: Assign unknown = 0

```python
G[0][0]['weight'] = 0
```

### Step 21: Assign unknown = value

```python
G[0][1]['capacity'] = -1
```

### Step 22: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnfeasible, nx.network_simplex, G)
```

### Step 23: Assign unknown = 0

```python
G[0][1]['capacity'] = 0
```

### Step 24: Assign unknown = value

```python
G[0][0]['capacity'] = -1
```

### Step 25: Call pytest.raises()

```python
pytest.raises(nx.NetworkXUnfeasible, nx.network_simplex, G)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
pytest.raises(nx.NetworkXNotImplemented, nx.network_simplex, G)
pytest.raises(nx.NetworkXNotImplemented, nx.capacity_scaling, G)
G = nx.MultiGraph()
pytest.raises(nx.NetworkXNotImplemented, nx.network_simplex, G)
pytest.raises(nx.NetworkXNotImplemented, nx.capacity_scaling, G)
G = nx.DiGraph()
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
G.add_node(0, demand=float('inf'))
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
pytest.raises(nx.NetworkXUnfeasible, nx.capacity_scaling, G)
G.nodes[0]['demand'] = 0
G.add_node(1, demand=0)
G.add_edge(0, 1, weight=-float('inf'))
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
pytest.raises(nx.NetworkXUnfeasible, nx.capacity_scaling, G)
G[0][1]['weight'] = 0
G.add_edge(0, 0, weight=float('inf'))
pytest.raises(nx.NetworkXError, nx.network_simplex, G)
G[0][0]['weight'] = 0
G[0][1]['capacity'] = -1
pytest.raises(nx.NetworkXUnfeasible, nx.network_simplex, G)
G[0][1]['capacity'] = 0
G[0][0]['capacity'] = -1
pytest.raises(nx.NetworkXUnfeasible, nx.network_simplex, G)
```

## Next Steps


---

*Source: test_mincost.py:432 | Complexity: Advanced | Last updated: 2026-06-02*