# How To: To Numpy Array Structured Dtype Nonedge Ary

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Similar to the scalar case, except has a different non-edge value for
each named field.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: G
```

## Step-by-Step Guide

### Step 1: 'Similar to the scalar case, except has a different non-edge value for\n    each named field.'

```python
'Similar to the scalar case, except has a different non-edge value for\n    each named field.'
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 1, weight=10)
```

### Step 3: Assign dtype = np.dtype(...)

```python
dtype = np.dtype([('weight', float), ('cost', float)])
```

### Step 4: Assign nonedges = np.array(...)

```python
nonedges = np.array([(0, np.inf)], dtype=dtype)
```

### Step 5: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G, dtype=dtype, weight=None, nonedge=nonedges)
```

### Step 6: Assign nonedge = value

```python
nonedge = nonedges[attr]
```

### Step 7: Assign expected = nx.to_numpy_array(...)

```python
expected = nx.to_numpy_array(G, dtype=float, weight=attr, nonedge=nonedge)
```

### Step 8: Call npt.assert_array_equal()

```python
npt.assert_array_equal(A[attr], expected)
```


## Complete Example

```python
# Setup
# Fixtures: G

# Workflow
'Similar to the scalar case, except has a different non-edge value for\n    each named field.'
G.add_edge(0, 1, weight=10)
dtype = np.dtype([('weight', float), ('cost', float)])
nonedges = np.array([(0, np.inf)], dtype=dtype)
A = nx.to_numpy_array(G, dtype=dtype, weight=None, nonedge=nonedges)
for attr in dtype.names:
    nonedge = nonedges[attr]
    expected = nx.to_numpy_array(G, dtype=float, weight=attr, nonedge=nonedge)
    npt.assert_array_equal(A[attr], expected)
```

## Next Steps


---

*Source: test_convert_numpy.py:366 | Complexity: Advanced | Last updated: 2026-06-02*