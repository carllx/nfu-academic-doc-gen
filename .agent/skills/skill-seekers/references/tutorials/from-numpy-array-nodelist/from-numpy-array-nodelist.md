# How To: From Numpy Array Nodelist

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from numpy array nodelist

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: nodes
```

## Step-by-Step Guide

### Step 1: Assign A = np.diag(...)

```python
A = np.diag(np.ones(4), k=1)
```

**Verification:**
```python
assert graphs_equal(G, expected)
```

### Step 2: Assign expected = nx.relabel_nodes(...)

```python
expected = nx.relabel_nodes(nx.path_graph(5), mapping=dict(enumerate(nodes)), copy=True)
```

**Verification:**
```python
assert graphs_equal(G, expected)
```

### Step 3: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(A, edge_attr=None, nodelist=nodes)
```

**Verification:**
```python
assert graphs_equal(G, expected)
```

### Step 4: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(expected, 1.0, name='weight')
```

### Step 5: Assign G = nx.from_numpy_array(...)

```python
G = nx.from_numpy_array(A, nodelist=nodes)
```

**Verification:**
```python
assert graphs_equal(G, expected)
```


## Complete Example

```python
# Setup
# Fixtures: nodes

# Workflow
A = np.diag(np.ones(4), k=1)
expected = nx.relabel_nodes(nx.path_graph(5), mapping=dict(enumerate(nodes)), copy=True)
G = nx.from_numpy_array(A, edge_attr=None, nodelist=nodes)
assert graphs_equal(G, expected)
nx.set_edge_attributes(expected, 1.0, name='weight')
G = nx.from_numpy_array(A, nodelist=nodes)
assert graphs_equal(G, expected)
```

## Next Steps


---

*Source: test_convert_numpy.py:432 | Complexity: Intermediate | Last updated: 2026-06-02*