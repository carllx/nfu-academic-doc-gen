# How To: Directed Chordless Cycle Parallel Multiedges

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed chordless cycle parallel multiedges

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign g = nx.MultiGraph(...)

```python
g = nx.MultiGraph()
```

### Step 2: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 3: Assign expected = value

```python
expected = [[*range(5)]]
```

### Step 4: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected, chordless=True)
```

### Step 5: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 6: Assign expected = value

```python
expected = [*cycle_edges(range(5))]
```

### Step 7: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected, chordless=True)
```

### Step 8: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 9: Assign expected = value

```python
expected = []
```

### Step 10: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected, chordless=True)
```

### Step 11: Assign g = nx.MultiDiGraph(...)

```python
g = nx.MultiDiGraph()
```

### Step 12: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 13: Assign expected = value

```python
expected = [[*range(5)]]
```

### Step 14: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected, chordless=True)
```

### Step 15: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 16: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, [], chordless=True)
```

### Step 17: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 18: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, [], chordless=True)
```

### Step 19: Assign g = nx.MultiDiGraph(...)

```python
g = nx.MultiDiGraph()
```

### Step 20: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 21: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5)[::-1])
```

### Step 22: Assign expected = value

```python
expected = [*cycle_edges(range(5))]
```

### Step 23: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, expected, chordless=True)
```

### Step 24: Call nx.add_cycle()

```python
nx.add_cycle(g, range(5))
```

### Step 25: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(g, [], chordless=True)
```


## Complete Example

```python
# Workflow
g = nx.MultiGraph()
nx.add_cycle(g, range(5))
expected = [[*range(5)]]
self.check_cycle_algorithm(g, expected, chordless=True)
nx.add_cycle(g, range(5))
expected = [*cycle_edges(range(5))]
self.check_cycle_algorithm(g, expected, chordless=True)
nx.add_cycle(g, range(5))
expected = []
self.check_cycle_algorithm(g, expected, chordless=True)
g = nx.MultiDiGraph()
nx.add_cycle(g, range(5))
expected = [[*range(5)]]
self.check_cycle_algorithm(g, expected, chordless=True)
nx.add_cycle(g, range(5))
self.check_cycle_algorithm(g, [], chordless=True)
nx.add_cycle(g, range(5))
self.check_cycle_algorithm(g, [], chordless=True)
g = nx.MultiDiGraph()
nx.add_cycle(g, range(5))
nx.add_cycle(g, range(5)[::-1])
expected = [*cycle_edges(range(5))]
self.check_cycle_algorithm(g, expected, chordless=True)
nx.add_cycle(g, range(5))
self.check_cycle_algorithm(g, [], chordless=True)
```

## Next Steps


---

*Source: test_cycles.py:486 | Complexity: Advanced | Last updated: 2026-06-02*