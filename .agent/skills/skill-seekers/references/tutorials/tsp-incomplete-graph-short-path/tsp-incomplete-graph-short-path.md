# How To: Tsp Incomplete Graph Short Path

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test TSP incomplete graph short path

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.approximation`
- `networkx.algorithms.approximation.traveling_salesman`
- `networkx.algorithms.approximation.traveling_salesman`
- `networkx.algorithms.approximation.traveling_salesman`
- `networkx.algorithms.approximation.traveling_salesman`
- `networkx.algorithms.approximation.traveling_salesman`
- `networkx.algorithms.approximation.traveling_salesman`
- `networkx.algorithms.approximation.traveling_salesman`


## Step-by-Step Guide

### Step 1: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(9)
```

**Verification:**
```python
assert len(cycle) == 17 and len(set(cycle)) == 12
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(4, 9), (9, 10), (10, 11), (11, 0)])
```

**Verification:**
```python
assert len(path) == 13 and len(set(path)) == 12
```

### Step 3: Assign unknown = 5

```python
G[4][5]['weight'] = 5
```

### Step 4: Assign cycle = nx_app.traveling_salesman_problem(...)

```python
cycle = nx_app.traveling_salesman_problem(G)
```

**Verification:**
```python
assert len(cycle) == 17 and len(set(cycle)) == 12
```

### Step 5: Assign path = nx_app.traveling_salesman_problem(...)

```python
path = nx_app.traveling_salesman_problem(G, cycle=False)
```

**Verification:**
```python
assert len(path) == 13 and len(set(path)) == 12
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(9)
G.add_edges_from([(4, 9), (9, 10), (10, 11), (11, 0)])
G[4][5]['weight'] = 5
cycle = nx_app.traveling_salesman_problem(G)
assert len(cycle) == 17 and len(set(cycle)) == 12
path = nx_app.traveling_salesman_problem(G, cycle=False)
assert len(path) == 13 and len(set(path)) == 12
```

## Next Steps


---

*Source: test_traveling_salesman.py:382 | Complexity: Intermediate | Last updated: 2026-06-02*