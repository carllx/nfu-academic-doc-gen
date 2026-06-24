# How To: Chordless Cycles Giant Hamiltonian

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test chordless cycles giant hamiltonian

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign n = 1000

```python
n = 1000
```

**Verification:**
```python
assert n % 2 == 0
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert n % 2 == 0
```

### Step 3: Assign expected = value

```python
expected = [[*range(0, n, 2)]] + [[x % n for x in range(i, i + 3)] for i in range(0, n, 2)]
```

### Step 4: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(G, expected, chordless=True)
```

### Step 5: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(G, [c for c in expected if len(c) <= 3], length_bound=3, chordless=True)
```

### Step 6: Assign n = 100

```python
n = 100
```

**Verification:**
```python
assert n % 2 == 0
```

### Step 7: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 8: Assign expected = value

```python
expected = [[*range(n - 2, -2, -2)]] + [[x % n for x in range(i, i + 3)] for i in range(0, n, 2)]
```

### Step 9: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(G, expected, chordless=True)
```

### Step 10: Call self.check_cycle_algorithm()

```python
self.check_cycle_algorithm(G, [c for c in expected if len(c) <= 3], length_bound=3, chordless=True)
```

### Step 11: Call G.add_edge()

```python
G.add_edge(v, (v + 1) % n)
```

### Step 12: Call G.add_edge()

```python
G.add_edge(v, (v + 1) % n)
```

### Step 13: Call G.add_edge()

```python
G.add_edge(v, (v + 2) % n)
```

### Step 14: Call G.add_edge()

```python
G.add_edge((v + 2) % n, v)
```


## Complete Example

```python
# Workflow
n = 1000
assert n % 2 == 0
G = nx.Graph()
for v in range(n):
    if not v % 2:
        G.add_edge(v, (v + 2) % n)
    G.add_edge(v, (v + 1) % n)
expected = [[*range(0, n, 2)]] + [[x % n for x in range(i, i + 3)] for i in range(0, n, 2)]
self.check_cycle_algorithm(G, expected, chordless=True)
self.check_cycle_algorithm(G, [c for c in expected if len(c) <= 3], length_bound=3, chordless=True)
n = 100
assert n % 2 == 0
G = nx.DiGraph()
for v in range(n):
    G.add_edge(v, (v + 1) % n)
    if not v % 2:
        G.add_edge((v + 2) % n, v)
expected = [[*range(n - 2, -2, -2)]] + [[x % n for x in range(i, i + 3)] for i in range(0, n, 2)]
self.check_cycle_algorithm(G, expected, chordless=True)
self.check_cycle_algorithm(G, [c for c in expected if len(c) <= 3], length_bound=3, chordless=True)
```

## Next Steps


---

*Source: test_cycles.py:541 | Complexity: Advanced | Last updated: 2026-06-02*