# How To: Read Newlines Between Xml Elements Table

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test read newlines between xml elements table

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
expected = pd.DataFrame([[1.0, 4.0, 7], [np.nan, np.nan, 8], [3.0, 6.0, 9]], columns=['Column 1', 'Column 2', 'Column 3'])
```


## Complete Example

```python
# Workflow
expected = pd.DataFrame([[1.0, 4.0, 7], [np.nan, np.nan, 8], [3.0, 6.0, 9]], columns=['Column 1', 'Column 2', 'Column 3'])
```

## Next Steps


---

*Source: test_odf.py:48 | Complexity: Beginner | Last updated: 2026-06-02*