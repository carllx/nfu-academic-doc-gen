# How To: Regularity

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the generated graph is `k`-out-regular.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.classes`
- `networkx.generators.directed`
- `numpy`


## Step-by-Step Guide

### Step 1: 'Tests that the generated graph is `k`-out-regular.'

```python
'Tests that the generated graph is `k`-out-regular.'
```

**Verification:**
```python
assert all((d == k for v, d in G.out_degree()))
```

### Step 2: Assign n = 10

```python
n = 10
```

**Verification:**
```python
assert all((d == k for v, d in G.out_degree()))
```

### Step 3: Assign k = 3

```python
k = 3
```

### Step 4: Assign G = random_uniform_k_out_graph(...)

```python
G = random_uniform_k_out_graph(n, k)
```

**Verification:**
```python
assert all((d == k for v, d in G.out_degree()))
```

### Step 5: Assign G = random_uniform_k_out_graph(...)

```python
G = random_uniform_k_out_graph(n, k, seed=42)
```

**Verification:**
```python
assert all((d == k for v, d in G.out_degree()))
```


## Complete Example

```python
# Workflow
'Tests that the generated graph is `k`-out-regular.'
n = 10
k = 3
G = random_uniform_k_out_graph(n, k)
assert all((d == k for v, d in G.out_degree()))
G = random_uniform_k_out_graph(n, k, seed=42)
assert all((d == k for v, d in G.out_degree()))
```

## Next Steps


---

*Source: test_directed.py:155 | Complexity: Intermediate | Last updated: 2026-06-02*