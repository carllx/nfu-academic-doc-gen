# How To: Nodelist

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Conversion from graph to sparse matrix to graph with nodelist.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Conversion from graph to sparse matrix to graph with nodelist.'

```python
'Conversion from graph to sparse matrix to graph with nodelist.'
```

**Verification:**
```python
assert nx.is_isomorphic(GA, P3)
```

### Step 2: Assign P4 = nx.path_graph(...)

```python
P4 = nx.path_graph(4)
```

### Step 3: Assign P3 = nx.path_graph(...)

```python
P3 = nx.path_graph(3)
```

### Step 4: Assign nodelist = list(...)

```python
nodelist = list(P3.nodes())
```

### Step 5: Assign A = nx.to_scipy_sparse_array(...)

```python
A = nx.to_scipy_sparse_array(P4, nodelist=nodelist)
```

### Step 6: Assign GA = nx.Graph(...)

```python
GA = nx.Graph(A)
```

**Verification:**
```python
assert nx.is_isomorphic(GA, P3)
```

### Step 7: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.to_scipy_sparse_array, P3, nodelist=[])
```

### Step 8: Assign long_nl = value

```python
long_nl = nodelist + [0]
```

### Step 9: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.to_scipy_sparse_array, P3, nodelist=long_nl)
```

### Step 10: Assign non_nl = value

```python
non_nl = [-1, 0, 1, 2]
```

### Step 11: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.to_scipy_sparse_array, P3, nodelist=non_nl)
```


## Complete Example

```python
# Workflow
'Conversion from graph to sparse matrix to graph with nodelist.'
P4 = nx.path_graph(4)
P3 = nx.path_graph(3)
nodelist = list(P3.nodes())
A = nx.to_scipy_sparse_array(P4, nodelist=nodelist)
GA = nx.Graph(A)
assert nx.is_isomorphic(GA, P3)
pytest.raises(nx.NetworkXError, nx.to_scipy_sparse_array, P3, nodelist=[])
long_nl = nodelist + [0]
pytest.raises(nx.NetworkXError, nx.to_scipy_sparse_array, P3, nodelist=long_nl)
non_nl = [-1, 0, 1, 2]
pytest.raises(nx.NetworkXError, nx.to_scipy_sparse_array, P3, nodelist=non_nl)
```

## Next Steps


---

*Source: test_convert_scipy.py:89 | Complexity: Advanced | Last updated: 2026-06-02*