# How To: Graph Converter Needs Backend

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test graph converter needs backend

## Prerequisites

**Required Modules:**
- `pickle`
- `pytest`
- `networkx`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests`
- `networkx.classes.tests.dispatch_interface`
- `networkx.classes.tests.dispatch_interface`


## Step-by-Step Guide

### Step 1: Assign A = sp.sparse.coo_array(...)

```python
A = sp.sparse.coo_array([[0, 3, 2], [3, 0, 1], [2, 1, 0]])
```

**Verification:**
```python
assert side_effects == []
```

### Step 2: Assign side_effects = value

```python
side_effects = []
```

**Verification:**
```python
assert type(nx.from_scipy_sparse_array(A)) is nx.Graph
```

### Step 3: Assign orig_convert_to_nx = value

```python
orig_convert_to_nx = LoopbackBackendInterface.convert_to_nx
```

**Verification:**
```python
assert side_effects == [1]
```

### Step 4: Assign LoopbackBackendInterface.convert_to_nx = convert_to_nx

```python
LoopbackBackendInterface.convert_to_nx = convert_to_nx
```

**Verification:**
```python
assert type(nx.from_scipy_sparse_array(A, backend='nx_loopback')) is LoopbackGraph
```

### Step 5: Assign LoopbackBackendInterface.from_scipy_sparse_array = from_scipy_sparse_array

```python
LoopbackBackendInterface.from_scipy_sparse_array = from_scipy_sparse_array
```

**Verification:**
```python
assert side_effects == [1, 1]
```

### Step 6: Call side_effects.append()

```python
side_effects.append(1)
```

**Verification:**
```python
assert type(nx.from_scipy_sparse_array(A, backend='networkx')) is nx.Graph
```

### Step 7: Assign LoopbackBackendInterface.convert_to_nx = staticmethod(...)

```python
LoopbackBackendInterface.convert_to_nx = staticmethod(orig_convert_to_nx)
```

**Verification:**
```python
assert side_effects == [1, 1]
```

### Step 8: Call nx.from_scipy_sparse_array()

```python
nx.from_scipy_sparse_array(A, backend='bad-backend-name')
```


## Complete Example

```python
# Workflow
from networkx.classes.tests.dispatch_interface import LoopbackBackendInterface, LoopbackGraph
A = sp.sparse.coo_array([[0, 3, 2], [3, 0, 1], [2, 1, 0]])
side_effects = []

def from_scipy_sparse_array(self, *args, **kwargs):
    side_effects.append(1)
    return self.convert_from_nx(self.__getattr__('from_scipy_sparse_array')(*args, **kwargs), preserve_edge_attrs=True, preserve_node_attrs=True, preserve_graph_attrs=True)

@staticmethod
def convert_to_nx(obj, *, name=None):
    if type(obj) is nx.Graph:
        return obj
    return nx.Graph(obj)
orig_convert_to_nx = LoopbackBackendInterface.convert_to_nx
LoopbackBackendInterface.convert_to_nx = convert_to_nx
LoopbackBackendInterface.from_scipy_sparse_array = from_scipy_sparse_array
try:
    assert side_effects == []
    assert type(nx.from_scipy_sparse_array(A)) is nx.Graph
    assert side_effects == [1]
    assert type(nx.from_scipy_sparse_array(A, backend='nx_loopback')) is LoopbackGraph
    assert side_effects == [1, 1]
    assert type(nx.from_scipy_sparse_array(A, backend='networkx')) is nx.Graph
    assert side_effects == [1, 1]
finally:
    LoopbackBackendInterface.convert_to_nx = staticmethod(orig_convert_to_nx)
    del LoopbackBackendInterface.from_scipy_sparse_array
with pytest.raises(ImportError, match='backend is not installed'):
    nx.from_scipy_sparse_array(A, backend='bad-backend-name')
```

## Next Steps


---

*Source: test_backends.py:44 | Complexity: Advanced | Last updated: 2026-06-02*