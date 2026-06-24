# How To: Graph Chain

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph chain

## Prerequisites

**Required Modules:**
- `gc`
- `pickle`
- `platform`
- `weakref`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = self.Graph(...)

```python
G = self.Graph([(0, 1), (1, 2)])
```

**Verification:**
```python
assert G is DG._graph
```

### Step 2: Assign DG = G.to_directed(...)

```python
DG = G.to_directed(as_view=True)
```

**Verification:**
```python
assert DG is SDG._graph
```

### Step 3: Assign SDG = DG.subgraph(...)

```python
SDG = DG.subgraph([0, 1])
```

**Verification:**
```python
assert SDG is RSDG._graph
```

### Step 4: Assign RSDG = SDG.reverse(...)

```python
RSDG = SDG.reverse(copy=False)
```

**Verification:**
```python
assert G is DG._graph
```


## Complete Example

```python
# Workflow
G = self.Graph([(0, 1), (1, 2)])
DG = G.to_directed(as_view=True)
SDG = DG.subgraph([0, 1])
RSDG = SDG.reverse(copy=False)
assert G is DG._graph
assert DG is SDG._graph
assert SDG is RSDG._graph
```

## Next Steps


---

*Source: test_graph.py:255 | Complexity: Intermediate | Last updated: 2026-06-02*