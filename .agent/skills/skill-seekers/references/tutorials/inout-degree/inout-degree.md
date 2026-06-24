# How To: Inout Degree

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inout degree

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
assert G.degree(2) == 3
```

### Step 2: Assign hide_nodes = value

```python
hide_nodes = [4, 5, 111]
```

**Verification:**
```python
assert G.out_degree(2) == 2
```

### Step 3: Assign nodes_gone = nx.filters.hide_nodes(...)

```python
nodes_gone = nx.filters.hide_nodes(hide_nodes)
```

**Verification:**
```python
assert G.in_degree(2) == 1
```

### Step 4: Assign G = self.gview(...)

```python
G = self.gview(self.G, filter_node=nodes_gone, filter_edge=edges_gone)
```

**Verification:**
```python
assert G.size() == 6
```


## Complete Example

```python
# Workflow
edges_gone = self.hide_edges_filter(self.hide_edges)
hide_nodes = [4, 5, 111]
nodes_gone = nx.filters.hide_nodes(hide_nodes)
G = self.gview(self.G, filter_node=nodes_gone, filter_edge=edges_gone)
assert G.degree(2) == 3
assert G.out_degree(2) == 2
assert G.in_degree(2) == 1
assert G.size() == 6
```

## Next Steps


---

*Source: test_subgraphviews.py:199 | Complexity: Intermediate | Last updated: 2026-06-02*