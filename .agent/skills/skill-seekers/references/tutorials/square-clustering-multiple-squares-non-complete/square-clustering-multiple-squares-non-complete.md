# How To: Square Clustering Multiple Squares Non Complete

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: An example where all nodes are part of all squares, but not every node
is connected to every other.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'An example where all nodes are part of all squares, but not every node\n    is connected to every other.'

```python
'An example where all nodes are part of all squares, but not every node\n    is connected to every other.'
```

**Verification:**
```python
assert nx.square_clustering(G) == expected
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph([(0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5)])
```

### Step 3: Assign expected = value

```python
expected = {n: 1 for n in G}
```

**Verification:**
```python
assert nx.square_clustering(G) == expected
```


## Complete Example

```python
# Workflow
'An example where all nodes are part of all squares, but not every node\n    is connected to every other.'
G = nx.Graph([(0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (2, 4), (1, 5), (2, 5)])
expected = {n: 1 for n in G}
assert nx.square_clustering(G) == expected
```

## Next Steps


---

*Source: test_cluster.py:30 | Complexity: Beginner | Last updated: 2026-06-02*