# How To: Get Dummies Index

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate from_tuples: test get dummies index

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples([(1, 1, 0), (1, 0, 1), (0, 1, 1)], names=('a', 'b', 'c'))
```


## Complete Example

```python
# Workflow
expected = MultiIndex.from_tuples([(1, 1, 0), (1, 0, 1), (0, 1, 1)], names=('a', 'b', 'c'))
```

## Next Steps


---

*Source: test_get_dummies.py:29 | Complexity: Beginner | Last updated: 2026-06-02*