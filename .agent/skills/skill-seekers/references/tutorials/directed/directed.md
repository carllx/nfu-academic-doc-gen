# How To: Directed

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DiGraph: Tests the node boundary of a directed graph.

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
```


## Complete Example

```python
# Workflow
G = nx.DiGraph([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])
```

## Next Steps


---

*Source: test_boundary.py:64 | Complexity: Beginner | Last updated: 2026-06-02*