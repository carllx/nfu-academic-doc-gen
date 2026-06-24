# How To: Wrong Graph Type

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wrong graph type

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 2: Assign G_edges = value

```python
G_edges = [[0, 1], [0, 2], [0, 3]]
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(G_edges)
```

### Step 4: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, nx.inverse_line_graph, G)
```

### Step 5: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

### Step 6: Assign G_edges = value

```python
G_edges = [[0, 1], [0, 2], [0, 3]]
```

### Step 7: Call G.add_edges_from()

```python
G.add_edges_from(G_edges)
```

### Step 8: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, nx.inverse_line_graph, G)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G_edges = [[0, 1], [0, 2], [0, 3]]
G.add_edges_from(G_edges)
pytest.raises(nx.NetworkXNotImplemented, nx.inverse_line_graph, G)
G = nx.MultiGraph()
G_edges = [[0, 1], [0, 2], [0, 3]]
G.add_edges_from(G_edges)
pytest.raises(nx.NetworkXNotImplemented, nx.inverse_line_graph, G)
```

## Next Steps


---

*Source: test_line.py:234 | Complexity: Advanced | Last updated: 2026-06-02*