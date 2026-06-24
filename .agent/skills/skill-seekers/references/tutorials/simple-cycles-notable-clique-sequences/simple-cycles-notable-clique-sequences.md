# How To: Simple Cycles Notable Clique Sequences

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple cycles notable clique sequences

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign g_family = value

```python
g_family = [self.K(n) for n in range(2, 12)]
```

### Step 2: Assign expected = value

```python
expected = [0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220]
```

### Step 3: Call self.check_cycle_enumeration_integer_sequence()

```python
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=3)
```

### Step 4: Assign g_family = value

```python
g_family = [self.D(n) for n in range(2, 12)]
```

### Step 5: Assign expected = value

```python
expected = [2 * e for e in expected]
```

### Step 6: Call self.check_cycle_enumeration_integer_sequence()

```python
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=3, algorithm=triangles)
```

### Step 7: Assign expected = value

```python
expected = [0, 0, 0, 3, 15, 45, 105, 210, 378, 630, 990]
```

### Step 8: Assign g_family = value

```python
g_family = [self.K(n) for n in range(1, 12)]
```

### Step 9: Call self.check_cycle_enumeration_integer_sequence()

```python
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=4, algorithm=four_cycles)
```

### Step 10: Assign expected = value

```python
expected = [2 * e for e in expected]
```

### Step 11: Assign g_family = value

```python
g_family = [self.D(n) for n in range(1, 15)]
```

### Step 12: Call self.check_cycle_enumeration_integer_sequence()

```python
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=4, algorithm=four_cycles)
```

### Step 13: Assign expected = value

```python
expected = [0, 1, 5, 20, 84, 409, 2365]
```

### Step 14: Assign g_family = value

```python
g_family = [self.D(n) for n in range(1, 8)]
```

### Step 15: Call self.check_cycle_enumeration_integer_sequence()

```python
self.check_cycle_enumeration_integer_sequence(g_family, expected)
```

### Step 16: Assign expected = value

```python
expected = [0, 0, 0, 1, 7, 37, 197, 1172]
```

### Step 17: Assign g_family = value

```python
g_family = [self.K(n) for n in range(8)]
```

### Step 18: Call self.check_cycle_enumeration_integer_sequence()

```python
self.check_cycle_enumeration_integer_sequence(g_family, expected)
```

### Step 19: yield from (c for c in nx.simple_cycles(g, **kwargs) if len(c) == 3)

```python
yield from (c for c in nx.simple_cycles(g, **kwargs) if len(c) == 3)
```

### Step 20: yield from (c for c in nx.simple_cycles(g, **kwargs) if len(c) == 4)

```python
yield from (c for c in nx.simple_cycles(g, **kwargs) if len(c) == 4)
```


## Complete Example

```python
# Workflow
g_family = [self.K(n) for n in range(2, 12)]
expected = [0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220]
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=3)

def triangles(g, **kwargs):
    yield from (c for c in nx.simple_cycles(g, **kwargs) if len(c) == 3)
g_family = [self.D(n) for n in range(2, 12)]
expected = [2 * e for e in expected]
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=3, algorithm=triangles)

def four_cycles(g, **kwargs):
    yield from (c for c in nx.simple_cycles(g, **kwargs) if len(c) == 4)
expected = [0, 0, 0, 3, 15, 45, 105, 210, 378, 630, 990]
g_family = [self.K(n) for n in range(1, 12)]
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=4, algorithm=four_cycles)
expected = [2 * e for e in expected]
g_family = [self.D(n) for n in range(1, 15)]
self.check_cycle_enumeration_integer_sequence(g_family, expected, length_bound=4, algorithm=four_cycles)
expected = [0, 1, 5, 20, 84, 409, 2365]
g_family = [self.D(n) for n in range(1, 8)]
self.check_cycle_enumeration_integer_sequence(g_family, expected)
expected = [0, 0, 0, 1, 7, 37, 197, 1172]
g_family = [self.K(n) for n in range(8)]
self.check_cycle_enumeration_integer_sequence(g_family, expected)
```

## Next Steps


---

*Source: test_cycles.py:441 | Complexity: Advanced | Last updated: 2026-06-02*