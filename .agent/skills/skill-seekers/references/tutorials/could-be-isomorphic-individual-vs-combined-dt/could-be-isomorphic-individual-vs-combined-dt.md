# How To: Could Be Isomorphic Individual Vs Combined Dt

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: A test case where G and H have identical degree and triangle distributions,
but are different when compared together

## Prerequisites

**Required Modules:**
- `functools`
- `pytest`
- `networkx`
- `networkx.algorithms`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (3, 4), (4, 5), (4, 6)])
```


## Complete Example

```python
# Workflow
G = nx.Graph([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (3, 4), (4, 5), (4, 6)])
```

## Next Steps


---

*Source: test_isomorphism.py:55 | Complexity: Beginner | Last updated: 2026-06-02*