# How To: Graph Edit Distance

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph edit distance

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.similarity`
- `networkx.generators.classic`


## Step-by-Step Guide

### Step 1: Assign G0 = nx.Graph(...)

```python
G0 = nx.Graph()
```

**Verification:**
```python
assert graph_edit_distance(G0, G0) == 0
```

### Step 2: Assign G1 = path_graph(...)

```python
G1 = path_graph(6)
```

**Verification:**
```python
assert graph_edit_distance(G0, G1) == 11
```

### Step 3: Assign G2 = cycle_graph(...)

```python
G2 = cycle_graph(6)
```

**Verification:**
```python
assert graph_edit_distance(G1, G0) == 11
```

### Step 4: Assign G3 = wheel_graph(...)

```python
G3 = wheel_graph(7)
```

**Verification:**
```python
assert graph_edit_distance(G0, G2) == 12
```


## Complete Example

```python
# Workflow
G0 = nx.Graph()
G1 = path_graph(6)
G2 = cycle_graph(6)
G3 = wheel_graph(7)
assert graph_edit_distance(G0, G0) == 0
assert graph_edit_distance(G0, G1) == 11
assert graph_edit_distance(G1, G0) == 11
assert graph_edit_distance(G0, G2) == 12
assert graph_edit_distance(G2, G0) == 12
assert graph_edit_distance(G0, G3) == 19
assert graph_edit_distance(G3, G0) == 19
assert graph_edit_distance(G1, G1) == 0
assert graph_edit_distance(G1, G2) == 1
assert graph_edit_distance(G2, G1) == 1
assert graph_edit_distance(G1, G3) == 8
assert graph_edit_distance(G3, G1) == 8
assert graph_edit_distance(G2, G2) == 0
assert graph_edit_distance(G2, G3) == 7
assert graph_edit_distance(G3, G2) == 7
assert graph_edit_distance(G3, G3) == 0
```

## Next Steps


---

*Source: test_similarity.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*