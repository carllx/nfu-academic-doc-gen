# How To: Pred

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pred

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign edges_gone = self.hide_edges_filter(...)

```python
edges_gone = self.hide_edges_filter(self.hide_edges)
```

**Verification:**
```python
assert list(G.pred[2]) == [1]
```

### Step 2: Assign hide_nodes = value

```python
hide_nodes = [4, 5, 111]
```

**Verification:**
```python
assert list(G.pred[6]) == []
```

### Step 3: Assign nodes_gone = nx.filters.hide_nodes(...)

```python
nodes_gone = nx.filters.hide_nodes(hide_nodes)
```

### Step 4: Assign G = self.gview(...)

```python
G = self.gview(self.G, filter_node=nodes_gone, filter_edge=edges_gone)
```

**Verification:**
```python
assert list(G.pred[2]) == [1]
```


## Complete Example

```python
# Workflow
edges_gone = self.hide_edges_filter(self.hide_edges)
hide_nodes = [4, 5, 111]
nodes_gone = nx.filters.hide_nodes(hide_nodes)
G = self.gview(self.G, filter_node=nodes_gone, filter_edge=edges_gone)
assert list(G.pred[2]) == [1]
assert list(G.pred[6]) == []
```

## Next Steps


---

*Source: test_subgraphviews.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*