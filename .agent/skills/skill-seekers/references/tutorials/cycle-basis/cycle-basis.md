# How To: Cycle Basis

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cycle basis

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.G
```

**Verification:**
```python
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
```

### Step 2: Assign cy = nx.cycle_basis(...)

```python
cy = nx.cycle_basis(G, 0)
```

**Verification:**
```python
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
```

### Step 3: Assign sort_cy = sorted(...)

```python
sort_cy = sorted((sorted(c) for c in cy))
```

**Verification:**
```python
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
```

### Step 4: Assign cy = nx.cycle_basis(...)

```python
cy = nx.cycle_basis(G, 1)
```

**Verification:**
```python
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5], ['A', 'B', 'C']]
```

### Step 5: Assign sort_cy = sorted(...)

```python
sort_cy = sorted((sorted(c) for c in cy))
```

**Verification:**
```python
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
```

### Step 6: Assign cy = nx.cycle_basis(...)

```python
cy = nx.cycle_basis(G, 9)
```

### Step 7: Assign sort_cy = sorted(...)

```python
sort_cy = sorted((sorted(c) for c in cy))
```

**Verification:**
```python
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
```

### Step 8: Call nx.add_cycle()

```python
nx.add_cycle(G, 'ABC')
```

### Step 9: Assign cy = nx.cycle_basis(...)

```python
cy = nx.cycle_basis(G, 9)
```

### Step 10: Assign sort_cy = value

```python
sort_cy = sorted((sorted(c) for c in cy[:-1])) + [sorted(cy[-1])]
```

**Verification:**
```python
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5], ['A', 'B', 'C']]
```


## Complete Example

```python
# Workflow
G = self.G
cy = nx.cycle_basis(G, 0)
sort_cy = sorted((sorted(c) for c in cy))
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
cy = nx.cycle_basis(G, 1)
sort_cy = sorted((sorted(c) for c in cy))
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
cy = nx.cycle_basis(G, 9)
sort_cy = sorted((sorted(c) for c in cy))
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5]]
nx.add_cycle(G, 'ABC')
cy = nx.cycle_basis(G, 9)
sort_cy = sorted((sorted(c) for c in cy[:-1])) + [sorted(cy[-1])]
assert sort_cy == [[0, 1, 2, 3], [0, 1, 6, 7, 8], [0, 3, 4, 5], ['A', 'B', 'C']]
```

## Next Steps


---

*Source: test_cycles.py:43 | Complexity: Advanced | Last updated: 2026-06-02*