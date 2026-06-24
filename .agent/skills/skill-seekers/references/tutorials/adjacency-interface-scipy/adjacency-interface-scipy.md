# How To: Adjacency Interface Scipy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test adjacency interface scipy

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(self.Gs, dtype='d')
```

**Verification:**
```python
assert pos.shape == (6, 2)
```

### Step 2: Assign pos = nx.drawing.layout._sparse_fruchterman_reingold(...)

```python
pos = nx.drawing.layout._sparse_fruchterman_reingold(A)
```

**Verification:**
```python
assert pos.shape == (6, 2)
```

### Step 3: Assign pos = nx.drawing.layout._sparse_spectral(...)

```python
pos = nx.drawing.layout._sparse_spectral(A)
```

**Verification:**
```python
assert pos.shape == (6, 3)
```

### Step 4: Assign pos = nx.drawing.layout._sparse_fruchterman_reingold(...)

```python
pos = nx.drawing.layout._sparse_fruchterman_reingold(A, dim=3)
```

**Verification:**
```python
assert pos.shape == (6, 3)
```


## Complete Example

```python
# Workflow
A = nx.to_scipy_sparse_array(self.Gs, dtype='d')
pos = nx.drawing.layout._sparse_fruchterman_reingold(A)
assert pos.shape == (6, 2)
pos = nx.drawing.layout._sparse_spectral(A)
assert pos.shape == (6, 2)
pos = nx.drawing.layout._sparse_fruchterman_reingold(A, dim=3)
assert pos.shape == (6, 3)
```

## Next Steps


---

*Source: test_layout.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*