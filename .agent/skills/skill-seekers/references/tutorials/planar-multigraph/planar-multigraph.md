# How To: Planar Multigraph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate MultiGraph: test planar multigraph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.planarity`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph([(1, 2), (1, 2), (1, 2), (1, 2), (2, 3), (3, 1)])
```


## Complete Example

```python
# Workflow
G = nx.MultiGraph([(1, 2), (1, 2), (1, 2), (1, 2), (2, 3), (3, 1)])
```

## Next Steps


---

*Source: test_planarity.py:180 | Complexity: Beginner | Last updated: 2026-06-02*