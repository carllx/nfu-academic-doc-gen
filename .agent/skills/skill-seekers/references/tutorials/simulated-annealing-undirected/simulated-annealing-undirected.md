# How To: Simulated Annealing Undirected

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simulated annealing undirected

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
cycle = self.tsp(self.UG, 'greedy', source='D', seed=42)
```

### Step 2: Assign cost = sum(...)

```python
cost = sum((self.UG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 3: Call validate_solution()

```python
validate_solution(cycle, cost, self.UG_cycle, self.UG_cost)
```

### Step 4: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.UG2, 'greedy', source='D', seed=42)
```

### Step 5: Assign cost = sum(...)

```python
cost = sum((self.UG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 6: Call validate_symmetric_solution()

```python
validate_symmetric_solution(cycle, cost, self.UG2_cycle, self.UG2_cost)
```

### Step 7: Assign cycle = self.tsp(...)

```python
cycle = self.tsp(self.UG2, 'greedy', move='1-0', source='D', seed=42)
```

### Step 8: Assign cost = sum(...)

```python
cost = sum((self.UG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
```

### Step 9: Call validate_symmetric_solution()

```python
validate_symmetric_solution(cycle, cost, self.UG2_cycle, self.UG2_cost)
```


## Complete Example

```python
# Workflow
cycle = self.tsp(self.UG, 'greedy', source='D', seed=42)
cost = sum((self.UG[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_solution(cycle, cost, self.UG_cycle, self.UG_cost)
cycle = self.tsp(self.UG2, 'greedy', source='D', seed=42)
cost = sum((self.UG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_symmetric_solution(cycle, cost, self.UG2_cycle, self.UG2_cost)
cycle = self.tsp(self.UG2, 'greedy', move='1-0', source='D', seed=42)
cost = sum((self.UG2[n][nbr]['weight'] for n, nbr in pairwise(cycle)))
validate_symmetric_solution(cycle, cost, self.UG2_cycle, self.UG2_cost)
```

## Next Steps


---

*Source: test_traveling_salesman.py:201 | Complexity: Advanced | Last updated: 2026-06-02*