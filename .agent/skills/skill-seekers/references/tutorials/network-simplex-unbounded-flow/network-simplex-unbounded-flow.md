# How To: Network Simplex Unbounded Flow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test network simplex unbounded flow

## Prerequisites

**Required Modules:**
- `bz2`
- `importlib.resources`
- `pickle`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 2: Call G.add_node()

```python
G.add_node('A')
```

### Step 3: Call G.add_node()

```python
G.add_node('B')
```

### Step 4: Call G.add_node()

```python
G.add_node('C')
```

### Step 5: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([('A', 'B', -5), ('B', 'C', -5), ('C', 'A', -5)])
```

### Step 6: Call nx.network_simplex()

```python
nx.network_simplex(G)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_weighted_edges_from([('A', 'B', -5), ('B', 'C', -5), ('C', 'A', -5)])
with pytest.raises(nx.NetworkXUnbounded, match='negative cycle with infinite capacity found'):
    nx.network_simplex(G)
```

## Next Steps


---

*Source: test_networksimplex.py:467 | Complexity: Intermediate | Last updated: 2026-06-02*