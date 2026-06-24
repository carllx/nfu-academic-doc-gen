# How To: Planar Digraph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DiGraph: test planar digraph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.planarity`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (2, 3), (2, 4), (4, 1), (4, 2), (1, 4), (3, 2)])
```


## Complete Example

```python
# Workflow
G = nx.DiGraph([(1, 2), (2, 3), (2, 4), (4, 1), (4, 2), (1, 4), (3, 2)])
```

## Next Steps


---

*Source: test_planarity.py:189 | Complexity: Beginner | Last updated: 2026-06-02*