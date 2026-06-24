# How To: Minimum Weight Full Matching Smaller Right

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test minimum weight full matching smaller right

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.bipartite.matching`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(4, 3)
```

**Verification:**
```python
assert matching == {1: 4, 2: 6, 3: 5, 4: 1, 5: 3, 6: 2}
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 4, weight=400)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 5, weight=400)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(0, 6, weight=300)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 4, weight=150)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(1, 5, weight=450)
```

### Step 7: Call G.add_edge()

```python
G.add_edge(1, 6, weight=225)
```

### Step 8: Call G.add_edge()

```python
G.add_edge(2, 4, weight=400)
```

### Step 9: Call G.add_edge()

```python
G.add_edge(2, 5, weight=600)
```

### Step 10: Call G.add_edge()

```python
G.add_edge(2, 6, weight=290)
```

### Step 11: Call G.add_edge()

```python
G.add_edge(3, 4, weight=1)
```

### Step 12: Call G.add_edge()

```python
G.add_edge(3, 5, weight=2)
```

### Step 13: Call G.add_edge()

```python
G.add_edge(3, 6, weight=3)
```

### Step 14: Assign matching = minimum_weight_full_matching(...)

```python
matching = minimum_weight_full_matching(G)
```

**Verification:**
```python
assert matching == {1: 4, 2: 6, 3: 5, 4: 1, 5: 3, 6: 2}
```


## Complete Example

```python
# Workflow
G = nx.complete_bipartite_graph(4, 3)
G.add_edge(0, 4, weight=400)
G.add_edge(0, 5, weight=400)
G.add_edge(0, 6, weight=300)
G.add_edge(1, 4, weight=150)
G.add_edge(1, 5, weight=450)
G.add_edge(1, 6, weight=225)
G.add_edge(2, 4, weight=400)
G.add_edge(2, 5, weight=600)
G.add_edge(2, 6, weight=290)
G.add_edge(3, 4, weight=1)
G.add_edge(3, 5, weight=2)
G.add_edge(3, 6, weight=3)
matching = minimum_weight_full_matching(G)
assert matching == {1: 4, 2: 6, 3: 5, 4: 1, 5: 3, 6: 2}
```

## Next Steps


---

*Source: test_matching.py:294 | Complexity: Advanced | Last updated: 2026-06-02*