# How To: 3D Layout

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 3d layout

## Prerequisites

**Required Modules:**
- `warnings`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert len(pos) == 5
```

### Step 2: Assign G = self.build_graph(...)

```python
G = self.build_graph(G)
```

**Verification:**
```python
assert len(pos[0]) == 3
```

### Step 3: Assign unknown = 3

```python
G.graph['dimen'] = 3
```

### Step 4: Assign pos = nx.nx_agraph.pygraphviz_layout(...)

```python
pos = nx.nx_agraph.pygraphviz_layout(G, prog='neato')
```

### Step 5: Assign pos = list(...)

```python
pos = list(pos.values())
```

**Verification:**
```python
assert len(pos) == 5
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G = self.build_graph(G)
G.graph['dimen'] = 3
pos = nx.nx_agraph.pygraphviz_layout(G, prog='neato')
pos = list(pos.values())
assert len(pos) == 5
assert len(pos[0]) == 3
```

## Next Steps


---

*Source: test_agraph.py:218 | Complexity: Intermediate | Last updated: 2026-06-02*