# How To: Count Categorical

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test count categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(Categorical([np.nan, 1, 2, np.nan], categories=[5, 4, 3, 2, 1], ordered=True))
```


## Complete Example

```python
# Workflow
ser = Series(Categorical([np.nan, 1, 2, np.nan], categories=[5, 4, 3, 2, 1], ordered=True))
```

## Next Steps


---

*Source: test_count.py:28 | Complexity: Beginner | Last updated: 2026-06-02*