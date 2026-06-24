# How To: Read Writer Table

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test read writer table

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([[1, np.nan, 7], [2, np.nan, 8], [3, np.nan, 9]], index=index, columns=['Column 1', 'Unnamed: 2', 'Column 3'])
```


## Complete Example

```python
# Workflow
expected = pd.DataFrame([[1, np.nan, 7], [2, np.nan, 8], [3, np.nan, 9]], index=index, columns=['Column 1', 'Unnamed: 2', 'Column 3'])
```

## Next Steps


---

*Source: test_odf.py:35 | Complexity: Beginner | Last updated: 2026-06-02*