# How To: Nlargest

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test nlargest

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign e = Series(...)

```python
e = Series([3, 2, 1, 3, 3, 2], index=MultiIndex.from_arrays([list('aaabbb'), [2, 3, 1, 6, 5, 7]]))
```


## Complete Example

```python
# Workflow
e = Series([3, 2, 1, 3, 3, 2], index=MultiIndex.from_arrays([list('aaabbb'), [2, 3, 1, 6, 5, 7]]))
```

## Next Steps


---

*Source: test_nlargest_nsmallest.py:25 | Complexity: Beginner | Last updated: 2026-06-02*