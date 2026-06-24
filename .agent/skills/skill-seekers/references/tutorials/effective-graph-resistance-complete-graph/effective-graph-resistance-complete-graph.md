# How To: Effective Graph Resistance Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test effective graph resistance complete graph

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

### Step 1: Assign N = 10

```python
N = 10
```

**Verification:**
```python
assert np.isclose(RG, N - 1)
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(N)
```

### Step 3: Assign RG = nx.effective_graph_resistance(...)

```python
RG = nx.effective_graph_resistance(G)
```

**Verification:**
```python
assert np.isclose(RG, N - 1)
```


## Complete Example

```python
# Workflow
N = 10
G = nx.complete_graph(N)
RG = nx.effective_graph_resistance(G)
assert np.isclose(RG, N - 1)
```

## Next Steps


---

*Source: test_distance_measures.py:575 | Complexity: Beginner | Last updated: 2026-06-02*