# How To: Struct Accessor Dtypes

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test struct accessor dtypes

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas.compat.pyarrow`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([], dtype=ArrowDtype(pa.struct([('int_col', pa.int64()), ('string_col', pa.string()), ('struct_col', pa.struct([('int_col', pa.int64()), ('float_col', pa.float64())]))])))
```


## Complete Example

```python
# Workflow
ser = Series([], dtype=ArrowDtype(pa.struct([('int_col', pa.int64()), ('string_col', pa.string()), ('struct_col', pa.struct([('int_col', pa.int64()), ('float_col', pa.float64())]))])))
```

## Next Steps


---

*Source: test_struct_accessor.py:23 | Complexity: Beginner | Last updated: 2026-06-02*