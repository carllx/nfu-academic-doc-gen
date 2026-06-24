# How To: Nst Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nst complete graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `math`
- `math`
- `random`
- `random`
- `itertools`


## Step-by-Step Guide

### Step 1: Assign N = 5

```python
N = 5
```

**Verification:**
```python
assert np.isclose(nx.number_of_spanning_trees(G), N ** (N - 2))
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(N)
```

**Verification:**
```python
assert np.isclose(nx.number_of_spanning_trees(G), N ** (N - 2))
```


## Complete Example

```python
# Workflow
N = 5
G = nx.complete_graph(N)
assert np.isclose(nx.number_of_spanning_trees(G), N ** (N - 2))
```

## Next Steps


---

*Source: test_mst.py:863 | Complexity: Beginner | Last updated: 2026-06-02*