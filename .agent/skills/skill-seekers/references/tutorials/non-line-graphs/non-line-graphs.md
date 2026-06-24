# How To: Non Line Graphs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non line graphs

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign claw = nx.star_graph(...)

```python
claw = nx.star_graph(3)
```

### Step 2: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, claw)
```

### Step 3: Assign wheel = nx.wheel_graph(...)

```python
wheel = nx.wheel_graph(6)
```

### Step 4: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, wheel)
```

### Step 5: Assign K5m = nx.complete_graph(...)

```python
K5m = nx.complete_graph(5)
```

### Step 6: Call K5m.remove_edge()

```python
K5m.remove_edge(0, 1)
```

### Step 7: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, K5m)
```

### Step 8: Assign G = nx.compose(...)

```python
G = nx.compose(nx.path_graph(2), nx.complete_bipartite_graph(2, 3))
```

### Step 9: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```

### Step 10: Assign G = nx.diamond_graph(...)

```python
G = nx.diamond_graph()
```

### Step 11: Call G.add_edges_from()

```python
G.add_edges_from([(4, 0), (5, 3)])
```

### Step 12: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```

### Step 13: Call G.add_edge()

```python
G.add_edge(4, 5)
```

### Step 14: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```

### Step 15: Assign G = nx.diamond_graph(...)

```python
G = nx.diamond_graph()
```

### Step 16: Call G.add_edges_from()

```python
G.add_edges_from([(4, 0), (4, 3)])
```

### Step 17: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```

### Step 18: Assign G = nx.diamond_graph(...)

```python
G = nx.diamond_graph()
```

### Step 19: Call G.add_edges_from()

```python
G.add_edges_from([(4, 0), (4, 1), (4, 2), (5, 3)])
```

### Step 20: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```

### Step 21: Call G.add_edges_from()

```python
G.add_edges_from([(5, 1), (5, 2)])
```

### Step 22: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```

### Step 23: Assign G = nx.diamond_graph(...)

```python
G = nx.diamond_graph()
```

### Step 24: Call G.add_edges_from()

```python
G.add_edges_from([(4, 0), (4, 1), (5, 2), (5, 3)])
```

### Step 25: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```


## Complete Example

```python
# Workflow
claw = nx.star_graph(3)
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, claw)
wheel = nx.wheel_graph(6)
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, wheel)
K5m = nx.complete_graph(5)
K5m.remove_edge(0, 1)
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, K5m)
G = nx.compose(nx.path_graph(2), nx.complete_bipartite_graph(2, 3))
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
G = nx.diamond_graph()
G.add_edges_from([(4, 0), (5, 3)])
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
G.add_edge(4, 5)
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
G = nx.diamond_graph()
G.add_edges_from([(4, 0), (4, 3)])
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
G = nx.diamond_graph()
G.add_edges_from([(4, 0), (4, 1), (4, 2), (5, 3)])
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
G.add_edges_from([(5, 1), (5, 2)])
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
G = nx.diamond_graph()
G.add_edges_from([(4, 0), (4, 1), (5, 2), (5, 3)])
pytest.raises(nx.NetworkXError, nx.inverse_line_graph, G)
```

## Next Steps


---

*Source: test_line.py:187 | Complexity: Advanced | Last updated: 2026-06-02*