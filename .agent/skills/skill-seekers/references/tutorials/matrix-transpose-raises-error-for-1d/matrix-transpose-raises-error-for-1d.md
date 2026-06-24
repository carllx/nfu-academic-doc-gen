# How To: Matrix Transpose Raises Error For 1D

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate masked_array: test matrix transpose raises error for 1d

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.ma`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign ma_arr = masked_array(...)

```python
ma_arr = masked_array(data=[1, 2, 3, 4, 5, 6], mask=[1, 0, 1, 1, 1, 0])
```


## Complete Example

```python
# Workflow
ma_arr = masked_array(data=[1, 2, 3, 4, 5, 6], mask=[1, 0, 1, 1, 1, 0])
```

## Next Steps


---

*Source: test_arrayobject.py:10 | Complexity: Beginner | Last updated: 2026-06-02*