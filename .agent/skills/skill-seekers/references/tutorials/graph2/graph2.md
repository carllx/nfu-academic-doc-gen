# How To: Graph2

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: test graph2

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.planarity`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 2), (4, 13), (0, 13), (4, 5), (7, 10), (1, 7), (0, 3), (2, 6), (5, 6), (7, 13), (4, 8), (0, 8), (0, 9), (2, 13), (6, 7), (3, 6), (2, 8)])
```


## Complete Example

```python
# Workflow
G = nx.Graph([(1, 2), (4, 13), (0, 13), (4, 5), (7, 10), (1, 7), (0, 3), (2, 6), (5, 6), (7, 13), (4, 8), (0, 8), (0, 9), (2, 13), (6, 7), (3, 6), (2, 8)])
```

## Next Steps


---

*Source: test_planarity.py:222 | Complexity: Beginner | Last updated: 2026-06-02*