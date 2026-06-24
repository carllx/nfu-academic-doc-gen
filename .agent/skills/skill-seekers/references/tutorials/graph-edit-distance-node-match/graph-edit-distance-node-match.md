# How To: Graph Edit Distance Node Match

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph edit distance node match

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.similarity`
- `networkx.generators.classic`


## Step-by-Step Guide

### Step 1: Assign G1 = cycle_graph(...)

```python
G1 = cycle_graph(5)
```

**Verification:**
```python
assert graph_edit_distance(G1, G2) == 0
```

### Step 2: Assign G2 = cycle_graph(...)

```python
G2 = cycle_graph(5)
```

**Verification:**
```python
assert graph_edit_distance(G1, G2, node_match=lambda n1, n2: n1['color'] == n2['color']) == 1
```

### Step 3: Assign unknown = value

```python
attr['color'] = 'red' if n % 2 == 0 else 'blue'
```

### Step 4: Assign unknown = value

```python
attr['color'] = 'red' if n % 2 == 1 else 'blue'
```


## Complete Example

```python
# Workflow
G1 = cycle_graph(5)
G2 = cycle_graph(5)
for n, attr in G1.nodes.items():
    attr['color'] = 'red' if n % 2 == 0 else 'blue'
for n, attr in G2.nodes.items():
    attr['color'] = 'red' if n % 2 == 1 else 'blue'
assert graph_edit_distance(G1, G2) == 0
assert graph_edit_distance(G1, G2, node_match=lambda n1, n2: n1['color'] == n2['color']) == 1
```

## Next Steps


---

*Source: test_similarity.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*