# How To: Basic

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test basic

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = pd.Series(...)

```python
expected = pd.Series([0, 1, 2, np.nan, np.nan, 3, 4], index=list('aaabcdd'), dtype=object, name='foo')
```


## Complete Example

```python
# Workflow
expected = pd.Series([0, 1, 2, np.nan, np.nan, 3, 4], index=list('aaabcdd'), dtype=object, name='foo')
```

## Next Steps


---

*Source: test_explode.py:11 | Complexity: Beginner | Last updated: 2026-06-02*