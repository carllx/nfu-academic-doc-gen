# How To: Greedy

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test greedy

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

### Step 1: Assign cycle = nx_app.greedy_tsp(...)

```python
cycle = nx_app.greedy_tsp(self.DG, source='D')
```

### Step 2: Assign cost = sum(...)

```python
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 3: Call validate_solution()

```python
validate_solution(cycle, cost, ['D', 'C', 'B', 'A', 'D'], 31.0)
```

### Step 4: Assign cycle = nx_app.greedy_tsp(...)

```python
cycle = nx_app.greedy_tsp(self.DG2, source='D')
```

### Step 5: Assign cost = sum(...)

```python
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 6: Call validate_solution()

```python
validate_solution(cycle, cost, ['D', 'C', 'B', 'A', 'D'], 78.0)
```

### Step 7: Assign cycle = nx_app.greedy_tsp(...)

```python
cycle = nx_app.greedy_tsp(self.UG, source='D')
```

### Step 8: Assign cost = sum(...)

```python
cost = sum((self.UG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 9: Call validate_solution()

```python
validate_solution(cycle, cost, ['D', 'C', 'B', 'A', 'D'], 33.0)
```

### Step 10: Assign cycle = nx_app.greedy_tsp(...)

```python
cycle = nx_app.greedy_tsp(self.UG2, source='D')
```

### Step 11: Assign cost = sum(...)

```python
cost = sum((self.UG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 12: Call validate_solution()

```python
validate_solution(cycle, cost, ['D', 'C', 'A', 'B', 'D'], 27.0)
```


## Complete Example

```python
# Workflow
cycle = nx_app.greedy_tsp(self.DG, source='D')
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, ['D', 'C', 'B', 'A', 'D'], 31.0)
cycle = nx_app.greedy_tsp(self.DG2, source='D')
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, ['D', 'C', 'B', 'A', 'D'], 78.0)
cycle = nx_app.greedy_tsp(self.UG, source='D')
cost = sum((self.UG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, ['D', 'C', 'B', 'A', 'D'], 33.0)
cycle = nx_app.greedy_tsp(self.UG2, source='D')
cost = sum((self.UG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, ['D', 'C', 'A', 'B', 'D'], 27.0)
```

## Next Steps


---

*Source: test_traveling_salesman.py:136 | Complexity: Advanced | Last updated: 2026-06-02*