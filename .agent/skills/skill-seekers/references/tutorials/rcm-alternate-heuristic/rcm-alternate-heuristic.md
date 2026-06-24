# How To: Rcm Alternate Heuristic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rcm alternate heuristic

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(0, 0), (0, 4), (1, 1), (1, 2), (1, 5), (1, 7), (2, 2), (2, 4), (3, 3), (3, 6), (4, 4), (5, 5), (5, 7), (6, 6), (7, 7)])
```

**Verification:**
```python
assert rcm in answers
```

### Step 2: Assign answers = value

```python
answers = [[6, 3, 5, 7, 1, 2, 4, 0], [6, 3, 7, 5, 1, 2, 4, 0], [7, 5, 1, 2, 4, 0, 6, 3]]
```

### Step 3: Assign rcm = list(...)

```python
rcm = list(reverse_cuthill_mckee_ordering(G, heuristic=smallest_degree))
```

**Verification:**
```python
assert rcm in answers
```

### Step 4: Assign unknown = min(...)

```python
deg, node = min(((d, n) for n, d in G.degree()))
```


## Complete Example

```python
# Workflow
G = nx.Graph([(0, 0), (0, 4), (1, 1), (1, 2), (1, 5), (1, 7), (2, 2), (2, 4), (3, 3), (3, 6), (4, 4), (5, 5), (5, 7), (6, 6), (7, 7)])
answers = [[6, 3, 5, 7, 1, 2, 4, 0], [6, 3, 7, 5, 1, 2, 4, 0], [7, 5, 1, 2, 4, 0, 6, 3]]

def smallest_degree(G):
    deg, node = min(((d, n) for n, d in G.degree()))
    return node
rcm = list(reverse_cuthill_mckee_ordering(G, heuristic=smallest_degree))
assert rcm in answers
```

## Next Steps


---

*Source: test_rcm.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*