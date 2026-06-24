# How To: Failure Of Costs Too High When Iterations Low

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test failure of costs too high when iterations low

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

### Step 1: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.DG2, 'greedy', source='D', move='1-0', N_inner=1, max_iterations=1, seed=4)
```

**Verification:**
```python
assert cost > self.DG2_cost
```

### Step 2: Assign cost = sum(...)

```python
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

**Verification:**
```python
assert cost > self.DG_cost
```

### Step 3: Assign initial_sol = value

```python
initial_sol = ['D', 'A', 'B', 'C', 'D']
```

### Step 4: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.DG, initial_sol, source='D', move='1-0', threshold=-3, seed=42)
```

### Step 5: Assign cost = sum(...)

```python
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

**Verification:**
```python
assert cost > self.DG_cost
```


## Complete Example

```python
# Workflow
cycle = self.tsp(self.DG2, 'greedy', source='D', move='1-0', N_inner=1, max_iterations=1, seed=4)
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
assert cost > self.DG2_cost
initial_sol = ['D', 'A', 'B', 'C', 'D']
cycle = self.tsp(self.DG, initial_sol, source='D', move='1-0', threshold=-3, seed=42)
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
assert cost > self.DG_cost
```

## Next Steps


---

*Source: test_traveling_salesman.py:273 | Complexity: Intermediate | Last updated: 2026-06-02*