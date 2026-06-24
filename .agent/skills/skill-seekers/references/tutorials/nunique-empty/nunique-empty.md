# How To: Nunique Empty

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nunique empty

## Prerequisites

**Required Modules:**
- `datetime`
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['a', 'b', 'c'])
```

### Step 2: Assign result = df.nunique(...)

```python
result = df.nunique()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(0, index=df.columns)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = df.T.nunique(...)

```python
result = df.T.nunique()
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([], dtype=np.float64)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(columns=['a', 'b', 'c'])
result = df.nunique()
expected = Series(0, index=df.columns)
tm.assert_series_equal(result, expected)
result = df.T.nunique()
expected = Series([], dtype=np.float64)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:186 | Complexity: Intermediate | Last updated: 2026-06-02*