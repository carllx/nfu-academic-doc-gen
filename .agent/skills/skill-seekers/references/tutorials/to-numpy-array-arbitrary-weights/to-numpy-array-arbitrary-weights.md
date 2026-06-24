# How To: To Numpy Array Arbitrary Weights

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to numpy array arbitrary weights

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 2: Assign w = 922337203685477580102

```python
w = 922337203685477580102
```

### Step 3: Call G.add_edge()

```python
G.add_edge(0, 1, weight=922337203685477580102)
```

### Step 4: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G, dtype=object)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([[0, w], [0, 0]], dtype=object)
```

### Step 6: Call npt.assert_array_equal()

```python
npt.assert_array_equal(A, expected)
```

### Step 7: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G.to_undirected(), dtype=object)
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([[0, w], [w, 0]], dtype=object)
```

### Step 9: Call npt.assert_array_equal()

```python
npt.assert_array_equal(A, expected)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
w = 922337203685477580102
G.add_edge(0, 1, weight=922337203685477580102)
A = nx.to_numpy_array(G, dtype=object)
expected = np.array([[0, w], [0, 0]], dtype=object)
npt.assert_array_equal(A, expected)
A = nx.to_numpy_array(G.to_undirected(), dtype=object)
expected = np.array([[0, w], [w, 0]], dtype=object)
npt.assert_array_equal(A, expected)
```

## Next Steps


---

*Source: test_convert_numpy.py:263 | Complexity: Advanced | Last updated: 2026-06-02*