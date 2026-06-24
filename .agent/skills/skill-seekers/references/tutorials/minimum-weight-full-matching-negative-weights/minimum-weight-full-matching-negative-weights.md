# How To: Minimum Weight Full Matching Negative Weights

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test minimum weight full matching negative weights

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.bipartite.matching`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(2, 2)
```

**Verification:**
```python
assert matching == {0: 3, 1: 2, 2: 1, 3: 0}
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 2, weight=-2)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 3, weight=0.2)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(1, 2, weight=-2)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 3, weight=0.3)
```

### Step 6: Assign matching = minimum_weight_full_matching(...)

```python
matching = minimum_weight_full_matching(G)
```

**Verification:**
```python
assert matching == {0: 3, 1: 2, 2: 1, 3: 0}
```


## Complete Example

```python
# Workflow
G = nx.complete_bipartite_graph(2, 2)
G.add_edge(0, 2, weight=-2)
G.add_edge(0, 3, weight=0.2)
G.add_edge(1, 2, weight=-2)
G.add_edge(1, 3, weight=0.3)
matching = minimum_weight_full_matching(G)
assert matching == {0: 3, 1: 2, 2: 1, 3: 0}
```

## Next Steps


---

*Source: test_matching.py:311 | Complexity: Intermediate | Last updated: 2026-06-02*