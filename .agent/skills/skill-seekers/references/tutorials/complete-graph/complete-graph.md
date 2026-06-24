# How To: Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete graph

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign K10 = cnlti(...)

```python
K10 = cnlti(nx.complete_graph(10), first_label=1)
```

**Verification:**
```python
assert list(nx.edge_boundary(K10, [])) == []
```


## Complete Example

```python
# Workflow
K10 = cnlti(nx.complete_graph(10), first_label=1)

def ilen(iterable):
    return sum((1 for i in iterable))
assert list(nx.edge_boundary(K10, [])) == []
assert list(nx.edge_boundary(K10, [], [])) == []
assert ilen(nx.edge_boundary(K10, [1, 2, 3])) == 21
assert ilen(nx.edge_boundary(K10, [4, 5, 6, 7])) == 24
assert ilen(nx.edge_boundary(K10, [3, 4, 5, 6, 7])) == 25
assert ilen(nx.edge_boundary(K10, [8, 9, 10])) == 21
assert edges_equal(nx.edge_boundary(K10, [4, 5, 6], [9, 10]), [(4, 9), (4, 10), (5, 9), (5, 10), (6, 9), (6, 10)])
assert edges_equal(nx.edge_boundary(K10, [1, 2, 3], [3, 4, 5]), [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5)])
```

## Next Steps


---

*Source: test_boundary.py:110 | Complexity: Beginner | Last updated: 2026-06-02*