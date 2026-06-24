# How To: Graph Edit Distance Edge Match

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph edit distance edge match

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.similarity`
- `networkx.generators.classic`


## Step-by-Step Guide

### Step 1: Assign G1 = path_graph(...)

```python
G1 = path_graph(6)
```

**Verification:**
```python
assert graph_edit_distance(G1, G2) == 0
```

### Step 2: Assign G2 = path_graph(...)

```python
G2 = path_graph(6)
```

**Verification:**
```python
assert graph_edit_distance(G1, G2, edge_match=lambda e1, e2: e1['color'] == e2['color']) == 2
```

### Step 3: Assign unknown = value

```python
attr['color'] = 'red' if min(e) % 2 == 0 else 'blue'
```

### Step 4: Assign unknown = value

```python
attr['color'] = 'red' if min(e) // 3 == 0 else 'blue'
```


## Complete Example

```python
# Workflow
G1 = path_graph(6)
G2 = path_graph(6)
for e, attr in G1.edges.items():
    attr['color'] = 'red' if min(e) % 2 == 0 else 'blue'
for e, attr in G2.edges.items():
    attr['color'] = 'red' if min(e) // 3 == 0 else 'blue'
assert graph_edit_distance(G1, G2) == 0
assert graph_edit_distance(G1, G2, edge_match=lambda e1, e2: e1['color'] == e2['color']) == 2
```

## Next Steps


---

*Source: test_similarity.py:135 | Complexity: Intermediate | Last updated: 2026-06-02*