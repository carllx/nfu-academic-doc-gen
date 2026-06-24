# How To: From Numpy Array Nodelist Bad Size

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: An exception is raised when `len(nodelist) != A.shape[0]`.

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'An exception is raised when `len(nodelist) != A.shape[0]`.'

```python
'An exception is raised when `len(nodelist) != A.shape[0]`.'
```

**Verification:**
```python
assert graphs_equal(nx.from_numpy_array(A, edge_attr=None), expected)
```

### Step 2: Assign n = 5

```python
n = 5
```

**Verification:**
```python
assert graphs_equal(nx.from_numpy_array(A, edge_attr=None, nodelist=nodes), expected)
```

### Step 3: Assign A = np.diag(...)

```python
A = np.diag(np.ones(n - 1), k=1)
```

### Step 4: Assign expected = nx.path_graph(...)

```python
expected = nx.path_graph(n)
```

**Verification:**
```python
assert graphs_equal(nx.from_numpy_array(A, edge_attr=None), expected)
```

### Step 5: Assign nodes = list(...)

```python
nodes = list(range(n))
```

**Verification:**
```python
assert graphs_equal(nx.from_numpy_array(A, edge_attr=None, nodelist=nodes), expected)
```

### Step 6: Assign nodes = list(...)

```python
nodes = list(range(n + 1))
```

### Step 7: Assign nodes = list(...)

```python
nodes = list(range(n - 1))
```

### Step 8: Call nx.from_numpy_array()

```python
nx.from_numpy_array(A, nodelist=nodes)
```

### Step 9: Call nx.from_numpy_array()

```python
nx.from_numpy_array(A, nodelist=nodes)
```


## Complete Example

```python
# Workflow
'An exception is raised when `len(nodelist) != A.shape[0]`.'
n = 5
A = np.diag(np.ones(n - 1), k=1)
expected = nx.path_graph(n)
assert graphs_equal(nx.from_numpy_array(A, edge_attr=None), expected)
nodes = list(range(n))
assert graphs_equal(nx.from_numpy_array(A, edge_attr=None, nodelist=nodes), expected)
nodes = list(range(n + 1))
with pytest.raises(ValueError, match='nodelist must have the same length as A'):
    nx.from_numpy_array(A, nodelist=nodes)
nodes = list(range(n - 1))
with pytest.raises(ValueError, match='nodelist must have the same length as A'):
    nx.from_numpy_array(A, nodelist=nodes)
```

## Next Steps


---

*Source: test_convert_numpy.py:399 | Complexity: Advanced | Last updated: 2026-06-02*