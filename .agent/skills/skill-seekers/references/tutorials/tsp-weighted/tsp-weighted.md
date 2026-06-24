# How To: Tsp Weighted

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test TSP weighted

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
assert cycle in expected_cycles
```

### Step 2: Assign unknown = 2

```python
G[0][1]['weight'] = 2
```

**Verification:**
```python
assert path in expected_paths
```

### Step 3: Assign unknown = 2

```python
G[1][2]['weight'] = 2
```

**Verification:**
```python
assert tourpath in expected_tourpaths
```

### Step 4: Assign unknown = 2

```python
G[2][3]['weight'] = 2
```

**Verification:**
```python
assert cycle in expected_cycles
```

### Step 5: Assign unknown = 4

```python
G[3][4]['weight'] = 4
```

**Verification:**
```python
assert path in expected_paths
```

### Step 6: Assign unknown = 5

```python
G[4][5]['weight'] = 5
```

**Verification:**
```python
assert tourpath in expected_tourpaths
```

### Step 7: Assign unknown = 4

```python
G[5][6]['weight'] = 4
```

### Step 8: Assign unknown = 2

```python
G[6][7]['weight'] = 2
```

### Step 9: Assign unknown = 2

```python
G[7][8]['weight'] = 2
```

### Step 10: Assign unknown = 2

```python
G[8][0]['weight'] = 2
```

### Step 11: Assign tsp = value

```python
tsp = nx_app.traveling_salesman_problem
```

### Step 12: Assign expected_paths = value

```python
expected_paths = ([3, 2, 1, 0, 8, 7, 6], [6, 7, 8, 0, 1, 2, 3])
```

### Step 13: Assign expected_cycles = value

```python
expected_cycles = ([3, 2, 1, 0, 8, 7, 6, 7, 8, 0, 1, 2, 3], [6, 7, 8, 0, 1, 2, 3, 2, 1, 0, 8, 7, 6])
```

### Step 14: Assign expected_tourpaths = value

```python
expected_tourpaths = ([5, 6, 7, 8, 0, 1, 2, 3, 4], [4, 3, 2, 1, 0, 8, 7, 6, 5])
```

### Step 15: Assign cycle = tsp(...)

```python
cycle = tsp(G, nodes=[3, 6], weight='weight')
```

**Verification:**
```python
assert cycle in expected_cycles
```

### Step 16: Assign path = tsp(...)

```python
path = tsp(G, nodes=[3, 6], weight='weight', cycle=False)
```

**Verification:**
```python
assert path in expected_paths
```

### Step 17: Assign tourpath = tsp(...)

```python
tourpath = tsp(G, weight='weight', cycle=False)
```

**Verification:**
```python
assert tourpath in expected_tourpaths
```

### Step 18: Assign methods = value

```python
methods = [(nx_app.christofides, {}), (nx_app.greedy_tsp, {}), (nx_app.simulated_annealing_tsp, {'init_cycle': 'greedy'}), (nx_app.threshold_accepting_tsp, {'init_cycle': 'greedy'})]
```

### Step 19: Assign cycle = tsp(...)

```python
cycle = tsp(G, nodes=[3, 6], weight='weight', method=method, **kwargs)
```

**Verification:**
```python
assert cycle in expected_cycles
```

### Step 20: Assign path = tsp(...)

```python
path = tsp(G, nodes=[3, 6], weight='weight', method=method, cycle=False, **kwargs)
```

**Verification:**
```python
assert path in expected_paths
```

### Step 21: Assign tourpath = tsp(...)

```python
tourpath = tsp(G, weight='weight', method=method, cycle=False, **kwargs)
```

**Verification:**
```python
assert tourpath in expected_tourpaths
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(9)
G[0][1]['weight'] = 2
G[1][2]['weight'] = 2
G[2][3]['weight'] = 2
G[3][4]['weight'] = 4
G[4][5]['weight'] = 5
G[5][6]['weight'] = 4
G[6][7]['weight'] = 2
G[7][8]['weight'] = 2
G[8][0]['weight'] = 2
tsp = nx_app.traveling_salesman_problem
expected_paths = ([3, 2, 1, 0, 8, 7, 6], [6, 7, 8, 0, 1, 2, 3])
expected_cycles = ([3, 2, 1, 0, 8, 7, 6, 7, 8, 0, 1, 2, 3], [6, 7, 8, 0, 1, 2, 3, 2, 1, 0, 8, 7, 6])
expected_tourpaths = ([5, 6, 7, 8, 0, 1, 2, 3, 4], [4, 3, 2, 1, 0, 8, 7, 6, 5])
cycle = tsp(G, nodes=[3, 6], weight='weight')
assert cycle in expected_cycles
path = tsp(G, nodes=[3, 6], weight='weight', cycle=False)
assert path in expected_paths
tourpath = tsp(G, weight='weight', cycle=False)
assert tourpath in expected_tourpaths
methods = [(nx_app.christofides, {}), (nx_app.greedy_tsp, {}), (nx_app.simulated_annealing_tsp, {'init_cycle': 'greedy'}), (nx_app.threshold_accepting_tsp, {'init_cycle': 'greedy'})]
for method, kwargs in methods:
    cycle = tsp(G, nodes=[3, 6], weight='weight', method=method, **kwargs)
    assert cycle in expected_cycles
    path = tsp(G, nodes=[3, 6], weight='weight', method=method, cycle=False, **kwargs)
    assert path in expected_paths
    tourpath = tsp(G, weight='weight', method=method, cycle=False, **kwargs)
    assert tourpath in expected_tourpaths
```

## Next Steps


---

*Source: test_traveling_salesman.py:323 | Complexity: Advanced | Last updated: 2026-06-02*