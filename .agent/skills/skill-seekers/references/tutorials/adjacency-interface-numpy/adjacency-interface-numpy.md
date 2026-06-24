# How To: Adjacency Interface Numpy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test adjacency interface numpy

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(self.Gs)
```

**Verification:**
```python
assert pos.shape == (6, 2)
```

### Step 2: Assign pos = nx.drawing.layout._fruchterman_reingold(...)

```python
pos = nx.drawing.layout._fruchterman_reingold(A)
```

**Verification:**
```python
assert pos.shape == (6, 3)
```

### Step 3: Assign pos = nx.drawing.layout._fruchterman_reingold(...)

```python
pos = nx.drawing.layout._fruchterman_reingold(A, dim=3)
```

**Verification:**
```python
assert pos.shape == (6, 2)
```

### Step 4: Assign pos = nx.drawing.layout._sparse_fruchterman_reingold(...)

```python
pos = nx.drawing.layout._sparse_fruchterman_reingold(A)
```

**Verification:**
```python
assert pos.shape == (6, 2)
```


## Complete Example

```python
# Workflow
A = nx.to_numpy_array(self.Gs)
pos = nx.drawing.layout._fruchterman_reingold(A)
assert pos.shape == (6, 2)
pos = nx.drawing.layout._fruchterman_reingold(A, dim=3)
assert pos.shape == (6, 3)
pos = nx.drawing.layout._sparse_fruchterman_reingold(A)
assert pos.shape == (6, 2)
```

## Next Steps


---

*Source: test_layout.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*