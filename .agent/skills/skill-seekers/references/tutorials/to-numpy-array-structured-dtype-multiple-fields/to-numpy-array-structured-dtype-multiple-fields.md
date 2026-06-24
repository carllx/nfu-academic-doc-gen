# How To: To Numpy Array Structured Dtype Multiple Fields

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy array structured dtype multiple fields

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: graph_type, edge
```

## Step-by-Step Guide

### Step 1: Assign G = graph_type(...)

```python
G = graph_type([edge])
```

### Step 2: Assign dtype = np.dtype(...)

```python
dtype = np.dtype([('weight', float), ('cost', float), ('flow', float)])
```

### Step 3: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G, dtype=dtype, weight=None)
```

### Step 4: Assign expected = nx.to_numpy_array(...)

```python
expected = nx.to_numpy_array(G, dtype=float, weight=attr)
```

### Step 5: Call npt.assert_array_equal()

```python
npt.assert_array_equal(A[attr], expected)
```


## Complete Example

```python
# Setup
# Fixtures: graph_type, edge

# Workflow
G = graph_type([edge])
dtype = np.dtype([('weight', float), ('cost', float), ('flow', float)])
A = nx.to_numpy_array(G, dtype=dtype, weight=None)
for attr in dtype.names:
    expected = nx.to_numpy_array(G, dtype=float, weight=attr)
    npt.assert_array_equal(A[attr], expected)
```

## Next Steps


---

*Source: test_convert_numpy.py:346 | Complexity: Intermediate | Last updated: 2026-06-02*