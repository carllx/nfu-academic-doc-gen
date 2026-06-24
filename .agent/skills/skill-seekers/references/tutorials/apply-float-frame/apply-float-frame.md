# How To: Apply Float Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply float frame

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: float_frame, engine
```

## Step-by-Step Guide

### Step 1: Assign no_rows = value

```python
no_rows = float_frame[:0]
```

### Step 2: Assign result = no_rows.apply(...)

```python
result = no_rows.apply(lambda x: x.mean(), engine=engine)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(np.nan, index=float_frame.columns)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign no_cols = value

```python
no_cols = float_frame.loc[:, []]
```

### Step 6: Assign result = no_cols.apply(...)

```python
result = no_cols.apply(lambda x: x.mean(), axis=1, engine=engine)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(np.nan, index=float_frame.index)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, engine

# Workflow
no_rows = float_frame[:0]
result = no_rows.apply(lambda x: x.mean(), engine=engine)
expected = Series(np.nan, index=float_frame.columns)
tm.assert_series_equal(result, expected)
no_cols = float_frame.loc[:, []]
result = no_cols.apply(lambda x: x.mean(), axis=1, engine=engine)
expected = Series(np.nan, index=float_frame.index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:133 | Complexity: Advanced | Last updated: 2026-06-02*