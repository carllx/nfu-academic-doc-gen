# How To: Selfloops

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test selfloops

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

### Step 2: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph()
```

**Verification:**
```python
assert graph_edit_distance(G0, G1) == 4
```

### Step 3: Call G1.add_edges_from()

```python
G1.add_edges_from((('A', 'A'), ('A', 'B')))
```

**Verification:**
```python
assert graph_edit_distance(G1, G0) == 4
```

### Step 4: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph()
```

**Verification:**
```python
assert graph_edit_distance(G0, G2) == 4
```

### Step 5: Call G2.add_edges_from()

```python
G2.add_edges_from((('A', 'B'), ('B', 'B')))
```

**Verification:**
```python
assert graph_edit_distance(G2, G0) == 4
```

### Step 6: Assign G3 = nx.Graph(...)

```python
G3 = nx.Graph()
```

**Verification:**
```python
assert graph_edit_distance(G0, G3) == 5
```

### Step 7: Call G3.add_edges_from()

```python
G3.add_edges_from((('A', 'A'), ('A', 'B'), ('B', 'B')))
```

**Verification:**
```python
assert graph_edit_distance(G3, G0) == 5
```


## Complete Example

```python
# Workflow
G0 = nx.Graph()
G1 = nx.Graph()
G1.add_edges_from((('A', 'A'), ('A', 'B')))
G2 = nx.Graph()
G2.add_edges_from((('A', 'B'), ('B', 'B')))
G3 = nx.Graph()
G3.add_edges_from((('A', 'A'), ('A', 'B'), ('B', 'B')))
assert graph_edit_distance(G0, G0) == 0
assert graph_edit_distance(G0, G1) == 4
assert graph_edit_distance(G1, G0) == 4
assert graph_edit_distance(G0, G2) == 4
assert graph_edit_distance(G2, G0) == 4
assert graph_edit_distance(G0, G3) == 5
assert graph_edit_distance(G3, G0) == 5
assert graph_edit_distance(G1, G1) == 0
assert graph_edit_distance(G1, G2) == 0
assert graph_edit_distance(G2, G1) == 0
assert graph_edit_distance(G1, G3) == 1
assert graph_edit_distance(G3, G1) == 1
assert graph_edit_distance(G2, G2) == 0
assert graph_edit_distance(G2, G3) == 1
assert graph_edit_distance(G3, G2) == 1
assert graph_edit_distance(G3, G3) == 0
```

## Next Steps


---

*Source: test_similarity.py:286 | Complexity: Intermediate | Last updated: 2026-06-02*