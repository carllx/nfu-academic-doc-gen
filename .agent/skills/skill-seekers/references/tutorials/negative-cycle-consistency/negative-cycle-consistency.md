# How To: Negative Cycle Consistency

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test negative cycle consistency

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `random`


## Step-by-Step Guide

### Step 1: Assign unif = value

```python
unif = random.uniform
```

**Verification:**
```python
assert no_heuristic == with_heuristic
```

### Step 2: Call random.seed()

```python
random.seed(random_seed)
```

### Step 3: Assign G = nx.binomial_graph(...)

```python
G = nx.binomial_graph(N, density, seed=4, directed=True)
```

### Step 4: Assign edges = value

```python
edges = ((u, v, unif(-1, max_cost)) for u, v in G.edges)
```

### Step 5: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from(edges)
```

### Step 6: Assign no_heuristic = nx.negative_edge_cycle(...)

```python
no_heuristic = nx.negative_edge_cycle(G, heuristic=False)
```

### Step 7: Assign with_heuristic = nx.negative_edge_cycle(...)

```python
with_heuristic = nx.negative_edge_cycle(G, heuristic=True)
```

**Verification:**
```python
assert no_heuristic == with_heuristic
```


## Complete Example

```python
# Workflow
import random
unif = random.uniform
for random_seed in range(2):
    random.seed(random_seed)
    for density in [0.1, 0.9]:
        for N in [1, 10, 20]:
            for max_cost in [1, 90]:
                G = nx.binomial_graph(N, density, seed=4, directed=True)
                edges = ((u, v, unif(-1, max_cost)) for u, v in G.edges)
                G.add_weighted_edges_from(edges)
                no_heuristic = nx.negative_edge_cycle(G, heuristic=False)
                with_heuristic = nx.negative_edge_cycle(G, heuristic=True)
                assert no_heuristic == with_heuristic
```

## Next Steps


---

*Source: test_weighted.py:545 | Complexity: Intermediate | Last updated: 2026-06-02*