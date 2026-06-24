# How To: Clear Edges

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test clear edges

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `test_graph`
- `test_graph`
- `test_graph`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.K3
```

**Verification:**
```python
assert list(G.nodes) == nodes
```

### Step 2: Assign unknown = 'K3'

```python
G.graph['name'] = 'K3'
```

**Verification:**
```python
assert G.succ == expected
```

### Step 3: Assign nodes = list(...)

```python
nodes = list(G.nodes)
```

**Verification:**
```python
assert G.pred == expected
```

### Step 4: Call G.clear_edges()

```python
G.clear_edges()
```

**Verification:**
```python
assert list(G.edges) == []
```

### Step 5: Assign expected = value

```python
expected = {0: {}, 1: {}, 2: {}}
```

**Verification:**
```python
assert G.graph['name'] == 'K3'
```


## Complete Example

```python
# Workflow
G = self.K3
G.graph['name'] = 'K3'
nodes = list(G.nodes)
G.clear_edges()
assert list(G.nodes) == nodes
expected = {0: {}, 1: {}, 2: {}}
assert G.succ == expected
assert G.pred == expected
assert list(G.edges) == []
assert G.graph['name'] == 'K3'
```

## Next Steps


---

*Source: test_digraph.py:290 | Complexity: Intermediate | Last updated: 2026-06-02*