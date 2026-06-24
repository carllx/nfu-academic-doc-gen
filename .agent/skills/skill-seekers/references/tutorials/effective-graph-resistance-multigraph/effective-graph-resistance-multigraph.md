# How To: Effective Graph Resistance Multigraph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test effective graph resistance multigraph

## Prerequisites

**Required Modules:**
- `itertools`
- `math`
- `random`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.distance_measures`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert np.isclose(RG, rd12 + rd13 + rd23)
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2, weight=2)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 3, weight=1)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(2, 3, weight=1)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(2, 3, weight=3)
```

### Step 6: Assign RG = nx.effective_graph_resistance(...)

```python
RG = nx.effective_graph_resistance(G, 'weight', True)
```

### Step 7: Assign edge23 = value

```python
edge23 = 1 / (1 / 1 + 1 / 3)
```

### Step 8: Assign rd12 = value

```python
rd12 = 1 / (1 / (1 + edge23) + 1 / 2)
```

### Step 9: Assign rd13 = value

```python
rd13 = 1 / (1 / (1 + 2) + 1 / edge23)
```

### Step 10: Assign rd23 = value

```python
rd23 = 1 / (1 / (2 + edge23) + 1 / 1)
```

**Verification:**
```python
assert np.isclose(RG, rd12 + rd13 + rd23)
```


## Complete Example

```python
# Workflow
G = nx.MultiGraph()
G.add_edge(1, 2, weight=2)
G.add_edge(1, 3, weight=1)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 3, weight=3)
RG = nx.effective_graph_resistance(G, 'weight', True)
edge23 = 1 / (1 / 1 + 1 / 3)
rd12 = 1 / (1 / (1 + edge23) + 1 / 2)
rd13 = 1 / (1 / (1 + 2) + 1 / edge23)
rd23 = 1 / (1 / (2 + edge23) + 1 / 1)
assert np.isclose(RG, rd12 + rd13 + rd23)
```

## Next Steps


---

*Source: test_distance_measures.py:557 | Complexity: Advanced | Last updated: 2026-06-02*