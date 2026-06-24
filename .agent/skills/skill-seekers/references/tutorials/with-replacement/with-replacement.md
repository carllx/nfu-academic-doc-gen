# How To: With Replacement

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test with replacement

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.classes`
- `networkx.generators.directed`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign n = 10

```python
n = 10
```

**Verification:**
```python
assert G.is_multigraph()
```

### Step 2: Assign k = 3

```python
k = 3
```

**Verification:**
```python
assert all((d == k for v, d in G.out_degree()))
```

### Step 3: Assign G = random_uniform_k_out_graph(...)

```python
G = random_uniform_k_out_graph(n, k, with_replacement=True)
```

**Verification:**
```python
assert nx.number_of_selfloops(G) == 0
```

### Step 4: Assign n = 10

```python
n = 10
```

**Verification:**
```python
assert all((d == k for v, d in G.out_degree()))
```

### Step 5: Assign k = 9

```python
k = 9
```

### Step 6: Assign G = random_uniform_k_out_graph(...)

```python
G = random_uniform_k_out_graph(n, k, with_replacement=False, self_loops=False)
```

**Verification:**
```python
assert nx.number_of_selfloops(G) == 0
```


## Complete Example

```python
# Workflow
n = 10
k = 3
G = random_uniform_k_out_graph(n, k, with_replacement=True)
assert G.is_multigraph()
assert all((d == k for v, d in G.out_degree()))
n = 10
k = 9
G = random_uniform_k_out_graph(n, k, with_replacement=False, self_loops=False)
assert nx.number_of_selfloops(G) == 0
assert all((d == k for v, d in G.out_degree()))
```

## Next Steps


---

*Source: test_directed.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*