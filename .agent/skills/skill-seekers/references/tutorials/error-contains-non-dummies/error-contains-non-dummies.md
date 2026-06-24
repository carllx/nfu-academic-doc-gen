# How To: Error Contains Non Dummies

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test error contains non dummies

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dummies = DataFrame(...)

```python
dummies = DataFrame({'a': [1, 6, 3, 1], 'b': [0, 1, 0, 2], 'c': ['c1', 'c2', 'c3', 'c4']})
```


## Complete Example

```python
# Workflow
dummies = DataFrame({'a': [1, 6, 3, 1], 'b': [0, 1, 0, 2], 'c': ['c1', 'c2', 'c3', 'c4']})
```

## Next Steps


---

*Source: test_from_dummies.py:93 | Complexity: Beginner | Last updated: 2026-06-02*