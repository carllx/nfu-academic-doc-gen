# How To: Chain Decomposition Root Not In G

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test chain decomposition when root is not in graph

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Test chain decomposition when root is not in graph'

```python
'Test chain decomposition when root is not in graph'
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_nodes_from()

```python
G.add_nodes_from([1, 2, 3])
```

### Step 4: Call nx.has_bridges()

```python
nx.has_bridges(G, root=6)
```


## Complete Example

```python
# Workflow
'Test chain decomposition when root is not in graph'
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
with pytest.raises(nx.NodeNotFound):
    nx.has_bridges(G, root=6)
```

## Next Steps


---

*Source: test_chains.py:131 | Complexity: Intermediate | Last updated: 2026-06-02*