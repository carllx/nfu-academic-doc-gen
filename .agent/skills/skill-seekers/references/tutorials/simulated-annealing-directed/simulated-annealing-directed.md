# How To: Simulated Annealing Directed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simulated annealing directed

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
cycle = self.tsp(self.DG, 'greedy', source='D', seed=42)
```

### Step 2: Assign cost = sum(...)

```python
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 3: Call validate_solution()

```python
validate_solution(cycle, cost, self.DG_cycle, self.DG_cost)
```

### Step 4: Assign initial_sol = value

```python
initial_sol = ['D', 'B', 'A', 'C', 'D']
```

### Step 5: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.DG, initial_sol, source='D', seed=42)
```

### Step 6: Assign cost = sum(...)

```python
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 7: Call validate_solution()

```python
validate_solution(cycle, cost, self.DG_cycle, self.DG_cost)
```

### Step 8: Assign initial_sol = value

```python
initial_sol = ['D', 'A', 'C', 'B', 'D']
```

### Step 9: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.DG, initial_sol, move='1-0', source='D', seed=42)
```

### Step 10: Assign cost = sum(...)

```python
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 11: Call validate_solution()

```python
validate_solution(cycle, cost, self.DG_cycle, self.DG_cost)
```

### Step 12: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.DG2, 'greedy', source='D', seed=42)
```

### Step 13: Assign cost = sum(...)

```python
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 14: Call validate_solution()

```python
validate_solution(cycle, cost, self.DG2_cycle, self.DG2_cost)
```

### Step 15: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.DG2, 'greedy', move='1-0', source='D', seed=42)
```

### Step 16: Assign cost = sum(...)

```python
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 17: Call validate_solution()

```python
validate_solution(cycle, cost, self.DG2_cycle, self.DG2_cost)
```


## Complete Example

```python
# Workflow
cycle = self.tsp(self.DG, 'greedy', source='D', seed=42)
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, self.DG_cycle, self.DG_cost)
initial_sol = ['D', 'B', 'A', 'C', 'D']
cycle = self.tsp(self.DG, initial_sol, source='D', seed=42)
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, self.DG_cycle, self.DG_cost)
initial_sol = ['D', 'A', 'C', 'B', 'D']
cycle = self.tsp(self.DG, initial_sol, move='1-0', source='D', seed=42)
cost = sum((self.DG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, self.DG_cycle, self.DG_cost)
cycle = self.tsp(self.DG2, 'greedy', source='D', seed=42)
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, self.DG2_cycle, self.DG2_cost)
cycle = self.tsp(self.DG2, 'greedy', move='1-0', source='D', seed=42)
cost = sum((self.DG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, self.DG2_cycle, self.DG2_cost)
```

## Next Steps


---

*Source: test_traveling_salesman.py:178 | Complexity: Advanced | Last updated: 2026-06-02*