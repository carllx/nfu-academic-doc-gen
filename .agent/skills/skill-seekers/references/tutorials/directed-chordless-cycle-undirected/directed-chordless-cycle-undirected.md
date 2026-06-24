# How To: Directed Chordless Cycle Undirected

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed chordless cycle undirected

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
g = nx.DiGraph([(1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (5, 1), (0, 2)])
```

### Step 2: Assign expected_cycles = value

```python
expected_cycles = [(0, 2, 3, 4, 5), (1, 2, 3, 4, 5)]
```

### Step 3: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```

### Step 4: Assign g = nx.DiGraph(...)

```python
g = nx.DiGraph()
```

### Step 5: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 6: Call nx.add_cycle()

```python
nx.add_cycle(g, range(4, 9))
```

### Step 7: Call g.add_edge()

```python
g.add_edge(7, 3)
```

### Step 8: Assign expected_cycles = value

```python
expected_cycles = [(0, 1, 2, 3, 4), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8)]
```

### Step 9: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```

### Step 10: Call g.add_edge()

```python
g.add_edge(3, 7)
```

### Step 11: Assign expected_cycles = value

```python
expected_cycles = [(0, 1, 2, 3, 4), (3, 7), (4, 5, 6, 7, 8)]
```

### Step 12: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```

### Step 13: Assign expected_cycles = value

```python
expected_cycles = [(3, 7)]
```

### Step 14: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True, length_bound=4)
```

### Step 15: Call g.remove_edge()

```python
g.remove_edge(7, 3)
```

### Step 16: Assign expected_cycles = value

```python
expected_cycles = [(0, 1, 2, 3, 4), (4, 5, 6, 7, 8)]
```

### Step 17: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```

### Step 18: Assign g = nx.DiGraph(...)

```python
g = nx.DiGraph(((i, j) for i in range(10) for j in range(i)))
```

### Step 19: Assign expected_cycles = value

```python
expected_cycles = []
```

### Step 20: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```


## Complete Example

```python
# Workflow
g = nx.DiGraph([(1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (5, 1), (0, 2)])
expected_cycles = [(0, 2, 3, 4, 5), (1, 2, 3, 4, 5)]
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
g = nx.DiGraph()
nx.add_cycle(g, range(5))
nx.add_cycle(g, range(4, 9))
g.add_edge(7, 3)
expected_cycles = [(0, 1, 2, 3, 4), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8)]
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
g.add_edge(3, 7)
expected_cycles = [(0, 1, 2, 3, 4), (3, 7), (4, 5, 6, 7, 8)]
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
expected_cycles = [(3, 7)]
self.check_cycle_algorithm(g, expected_cycles, chordless=True, length_bound=4)
g.remove_edge(7, 3)
expected_cycles = [(0, 1, 2, 3, 4), (4, 5, 6, 7, 8)]
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
g = nx.DiGraph(((i, j) for i in range(10) for j in range(i)))
expected_cycles = []
self.check_cycle_algorithm(g, expected_cycles, chordless=True)
```

## Next Steps


---

*Source: test_cycles.py:358 | Complexity: Advanced | Last updated: 2026-06-02*