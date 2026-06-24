# How To: Hard Prob

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hard prob

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
num_colors, s = (5, 5)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(0, 10), (0, 11), (0, 12), (0, 23), (10, 4), (10, 9), (10, 20), (11, 4), (11, 8), (11, 16), (12, 9), (12, 22), (12, 23), (23, 7), (1, 17), (1, 18), (1, 19), (1, 24), (17, 5), (17, 13), (17, 22), (18, 5), (19, 5), (19, 6), (19, 8), (24, 7), (24, 16), (2, 4), (2, 13), (2, 14), (2, 15), (4, 6), (13, 5), (13, 21), (14, 6), (14, 15), (15, 6), (15, 21), (3, 16), (3, 20), (3, 21), (3, 22), (16, 8), (20, 8), (21, 9), (22, 7)])
```

### Step 4: Assign F = value

```python
F = {node: node // s for node in range(num_colors * s)}
```

### Step 5: Assign unknown = value

```python
F[s - 1] = num_colors - 1
```

### Step 6: Assign params = make_params_from_graph(...)

```python
params = make_params_from_graph(G=G, F=F)
```

### Step 7: Call nx.algorithms.coloring.equitable_coloring.procedure_P()

```python
nx.algorithms.coloring.equitable_coloring.procedure_P(V_minus=0, V_plus=num_colors - 1, **params)
```

### Step 8: Call check_state()

```python
check_state(**params)
```


## Complete Example

```python
# Workflow
num_colors, s = (5, 5)
G = nx.Graph()
G.add_edges_from([(0, 10), (0, 11), (0, 12), (0, 23), (10, 4), (10, 9), (10, 20), (11, 4), (11, 8), (11, 16), (12, 9), (12, 22), (12, 23), (23, 7), (1, 17), (1, 18), (1, 19), (1, 24), (17, 5), (17, 13), (17, 22), (18, 5), (19, 5), (19, 6), (19, 8), (24, 7), (24, 16), (2, 4), (2, 13), (2, 14), (2, 15), (4, 6), (13, 5), (13, 21), (14, 6), (14, 15), (15, 6), (15, 21), (3, 16), (3, 20), (3, 21), (3, 22), (16, 8), (20, 8), (21, 9), (22, 7)])
F = {node: node // s for node in range(num_colors * s)}
F[s - 1] = num_colors - 1
params = make_params_from_graph(G=G, F=F)
nx.algorithms.coloring.equitable_coloring.procedure_P(V_minus=0, V_plus=num_colors - 1, **params)
check_state(**params)
```

## Next Steps


---

*Source: test_coloring.py:202 | Complexity: Advanced | Last updated: 2026-06-02*