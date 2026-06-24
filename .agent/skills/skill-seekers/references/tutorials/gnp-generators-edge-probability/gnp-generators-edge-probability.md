# How To: Gnp Generators Edge Probability

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that gnp generators generate edges according to the their probability `p`.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: generator, p, directed
```

## Step-by-Step Guide

### Step 1: 'Test that gnp generators generate edges according to the their probability `p`.'

```python
'Test that gnp generators generate edges according to the their probability `p`.'
```

**Verification:**
```python
assert edge_counts[v][w] == 0
```

### Step 2: Assign runs = 5000

```python
runs = 5000
```

**Verification:**
```python
assert abs(edge_counts[v][w] / float(runs) - p) <= 0.03
```

### Step 3: Assign n = 5

```python
n = 5
```

### Step 4: Assign edge_counts = value

```python
edge_counts = [[0] * n for _ in range(n)]
```

### Step 5: Assign G = generator(...)

```python
G = generator(n, p, directed=directed)
```

**Verification:**
```python
assert edge_counts[v][w] == 0
```


## Complete Example

```python
# Setup
# Fixtures: generator, p, directed

# Workflow
'Test that gnp generators generate edges according to the their probability `p`.'
runs = 5000
n = 5
edge_counts = [[0] * n for _ in range(n)]
for i in range(runs):
    G = generator(n, p, directed=directed)
    for v, w in G.edges:
        edge_counts[v][w] += 1
        if not directed:
            edge_counts[w][v] += 1
for v in range(n):
    for w in range(n):
        if v == w:
            assert edge_counts[v][w] == 0
        else:
            assert abs(edge_counts[v][w] / float(runs) - p) <= 0.03
```

## Next Steps


---

*Source: test_random_graphs.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*