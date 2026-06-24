# How To: To Numpy Array Multiweight Reduction

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test various functions for reducing multiedge weights.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: func, expected
```

## Step-by-Step Guide

### Step 1: 'Test various functions for reducing multiedge weights.'

```python
'Test various functions for reducing multiedge weights.'
```

**Verification:**
```python
assert np.allclose(A, [[0, expected], [0, 0]])
```

### Step 2: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph()
```

**Verification:**
```python
assert np.allclose(A, [[0, expected], [expected, 0]])
```

### Step 3: Assign weights = value

```python
weights = [-1, 2, 10.0]
```

### Step 4: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G, multigraph_weight=func, dtype=float)
```

**Verification:**
```python
assert np.allclose(A, [[0, expected], [0, 0]])
```

### Step 5: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G.to_undirected(), multigraph_weight=func, dtype=float)
```

**Verification:**
```python
assert np.allclose(A, [[0, expected], [expected, 0]])
```

### Step 6: Call G.add_edge()

```python
G.add_edge(0, 1, weight=w)
```


## Complete Example

```python
# Setup
# Fixtures: func, expected

# Workflow
'Test various functions for reducing multiedge weights.'
G = nx.MultiDiGraph()
weights = [-1, 2, 10.0]
for w in weights:
    G.add_edge(0, 1, weight=w)
A = nx.to_numpy_array(G, multigraph_weight=func, dtype=float)
assert np.allclose(A, [[0, expected], [0, 0]])
A = nx.to_numpy_array(G.to_undirected(), multigraph_weight=func, dtype=float)
assert np.allclose(A, [[0, expected], [expected, 0]])
```

## Next Steps


---

*Source: test_convert_numpy.py:281 | Complexity: Intermediate | Last updated: 2026-06-02*