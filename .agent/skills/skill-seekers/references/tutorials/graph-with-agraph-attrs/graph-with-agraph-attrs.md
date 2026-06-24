# How To: Graph With Agraph Attrs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph with AGraph attrs

## Prerequisites

**Required Modules:**
- `warnings`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(2)
```

**Verification:**
```python
assert dict(A.node_attr)['width'] == '0.80'
```

### Step 2: Assign unknown = value

```python
G.graph['node'] = {'width': '0.80'}
```

**Verification:**
```python
assert dict(A.edge_attr)['fontsize'] == '14'
```

### Step 3: Assign unknown = value

```python
G.graph['edge'] = {'fontsize': '14'}
```

### Step 4: Assign unknown = nx.nx_agraph.view_pygraphviz(...)

```python
path, A = nx.nx_agraph.view_pygraphviz(G, show=False)
```

**Verification:**
```python
assert dict(A.node_attr)['width'] == '0.80'
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(2)
G.graph['node'] = {'width': '0.80'}
G.graph['edge'] = {'fontsize': '14'}
path, A = nx.nx_agraph.view_pygraphviz(G, show=False)
assert dict(A.node_attr)['width'] == '0.80'
assert dict(A.edge_attr)['fontsize'] == '14'
```

## Next Steps


---

*Source: test_agraph.py:163 | Complexity: Intermediate | Last updated: 2026-06-02*