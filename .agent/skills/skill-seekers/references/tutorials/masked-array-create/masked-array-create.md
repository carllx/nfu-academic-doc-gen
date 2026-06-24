# How To: Masked Array Create

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate masked_array: test masked array create

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.testing`
- `numpy.ma`


## Step-by-Step Guide

### Step 1: Assign x = np.ma.masked_array(...)

```python
x = np.ma.masked_array([0, 1, 2, 3, 0, 4, 5, 6], mask=[0, 0, 0, 1, 1, 1, 0, 0])
```


## Complete Example

```python
# Workflow
x = np.ma.masked_array([0, 1, 2, 3, 0, 4, 5, 6], mask=[0, 0, 0, 1, 1, 1, 0, 0])
```

## Next Steps


---

*Source: test_regression.py:8 | Complexity: Beginner | Last updated: 2026-06-02*