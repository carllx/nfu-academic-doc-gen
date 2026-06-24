# How To: Kemeny Constant Negative Weight

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test kemeny constant negative weight

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

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Assign w12 = 2

```python
w12 = 2
```

### Step 3: Assign w13 = 3

```python
w13 = 3
```

### Step 4: Assign w23 = value

```python
w23 = -10
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 2, weight=w12)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(1, 3, weight=w13)
```

### Step 7: Call G.add_edge()

```python
G.add_edge(2, 3, weight=w23)
```

### Step 8: Call nx.kemeny_constant()

```python
nx.kemeny_constant(G, weight='weight')
```


## Complete Example

```python
# Workflow
G = nx.Graph()
w12 = 2
w13 = 3
w23 = -10
G.add_edge(1, 2, weight=w12)
G.add_edge(1, 3, weight=w13)
G.add_edge(2, 3, weight=w23)
with pytest.raises(nx.NetworkXError):
    nx.kemeny_constant(G, weight='weight')
```

## Next Steps


---

*Source: test_distance_measures.py:710 | Complexity: Advanced | Last updated: 2026-06-02*