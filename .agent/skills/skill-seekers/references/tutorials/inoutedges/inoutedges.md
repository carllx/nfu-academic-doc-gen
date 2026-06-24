# How To: Inoutedges

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inoutedges

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
assert self.G.in_edges - G.in_edges == self.excluded
```

### Step 2: Assign hide_nodes = value

```python
hide_nodes = [4, 5, 111]
```

**Verification:**
```python
assert self.G.out_edges - G.out_edges == self.excluded
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
assert self.G.in_edges - G.in_edges == self.excluded
```


## Complete Example

```python
# Workflow
edges_gone = self.hide_edges_filter(self.hide_edges)
hide_nodes = [4, 5, 111]
nodes_gone = nx.filters.hide_nodes(hide_nodes)
G = self.gview(self.G, filter_node=nodes_gone, filter_edge=edges_gone)
assert self.G.in_edges - G.in_edges == self.excluded
assert self.G.out_edges - G.out_edges == self.excluded
```

## Next Steps


---

*Source: test_subgraphviews.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*