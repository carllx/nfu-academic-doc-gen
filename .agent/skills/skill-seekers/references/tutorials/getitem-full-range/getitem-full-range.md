# How To: Getitem Full Range

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem full range

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(5), index=list(range(5)))
```

### Step 2: Assign result = value

```python
result = ser[list(range(5))]
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ser)
```


## Complete Example

```python
# Workflow
ser = Series(range(5), index=list(range(5)))
result = ser[list(range(5))]
tm.assert_series_equal(result, ser)
```

## Next Steps


---

*Source: test_getitem.py:126 | Complexity: Beginner | Last updated: 2026-06-02*