# How To: Directed Chordless Loop Blockade

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed chordless loop blockade

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign g = nx.DiGraph(...)

```python
g = nx.DiGraph(((i, i) for i in range(10)))
```

### Step 2: Call nx.add_cycle()

```python
nx.add_cycle(g, range(10))
```

### Step 3: Assign expected_cycles = value

```python
expected_cycles = [(i,) for i in range(10)]
```

### Step 4: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```

### Step 5: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, length_bound=1)
```

### Step 6: Assign g = nx.MultiDiGraph(...)

```python
g = nx.MultiDiGraph(g)
```

### Step 7: Call g.add_edges_from()

```python
g.add_edges_from(((i, i) for i in range(0, 10, 2)))
```

### Step 8: Assign expected_cycles = value

```python
expected_cycles = [(i,) for i in range(1, 10, 2)]
```

### Step 9: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```


## Complete Example

```python
# Workflow
g = nx.DiGraph(((i, i) for i in range(10)))
nx.add_cycle(g, range(10))
expected_cycles = [(i,) for i in range(10)]
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
self.check_cycle_algorithm(g, expected_cycles, length_bound=1)
g = nx.MultiDiGraph(g)
g.add_edges_from(((i, i) for i in range(0, 10, 2)))
expected_cycles = [(i,) for i in range(1, 10, 2)]
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```

## Next Steps


---

*Source: test_cycles.py:428 | Complexity: Advanced | Last updated: 2026-06-02*