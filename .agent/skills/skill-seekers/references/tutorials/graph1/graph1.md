# How To: Graph1

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: test graph1

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.planarity`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(3, 10), (2, 13), (1, 13), (7, 11), (0, 8), (8, 13), (0, 2), (0, 7), (0, 10), (1, 7)])
```


## Complete Example

```python
# Workflow
G = nx.Graph([(3, 10), (2, 13), (1, 13), (7, 11), (0, 8), (8, 13), (0, 2), (0, 7), (0, 10), (1, 7)])
```

## Next Steps


---

*Source: test_planarity.py:205 | Complexity: Beginner | Last updated: 2026-06-02*