# How To: Immediate Raise

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test immediate raise

## Prerequisites

**Required Modules:**
- `os`
- `pathlib`
- `random`
- `tempfile`
- `pytest`
- `networkx`
- `networkx.utils.decorators`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 2)])
```

### Step 2: Assign D = nx.DiGraph(...)

```python
D = nx.DiGraph()
```

### Step 3: Assign node_iter = yield_nodes(...)

```python
node_iter = yield_nodes(G)
```

### Step 4: Call next()

```python
next(node_iter)
```

### Step 5: Call next()

```python
next(node_iter)
```

### Step 6: yield from G

```python
yield from G
```

### Step 7: Assign node_iter = yield_nodes(...)

```python
node_iter = yield_nodes(D)
```

### Step 8: Assign node_iter = yield_nodes(...)

```python
node_iter = yield_nodes(D)
```

### Step 9: Call next()

```python
next(node_iter)
```


## Complete Example

```python
# Workflow
@not_implemented_for('directed')
def yield_nodes(G):
    yield from G
G = nx.Graph([(1, 2)])
D = nx.DiGraph()
with pytest.raises(nx.NetworkXNotImplemented):
    node_iter = yield_nodes(D)
with pytest.raises(nx.NetworkXNotImplemented):
    node_iter = yield_nodes(D)
node_iter = yield_nodes(G)
next(node_iter)
next(node_iter)
with pytest.raises(StopIteration):
    next(node_iter)
```

## Next Steps


---

*Source: test_decorators.py:489 | Complexity: Advanced | Last updated: 2026-06-02*