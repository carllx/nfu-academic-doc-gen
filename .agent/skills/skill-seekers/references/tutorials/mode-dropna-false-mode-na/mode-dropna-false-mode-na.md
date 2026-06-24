# How To: Mode Dropna False Mode Na

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mode dropna false mode na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `decimal`
- `io`
- `operator`
- `pickle`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.api.extensions`
- `pandas.api.types`
- `pandas.tests.extension`
- `pandas.core.arrays.arrow.array`
- `pandas.core.arrays.arrow.extension_types`

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign more_nans = pd.Series(...)

```python
more_nans = pd.Series([None, None, data[0]], dtype=data.dtype)
```

### Step 2: Assign result = more_nans.mode(...)

```python
result = more_nans.mode(dropna=False)
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series([None], dtype=data.dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = pd.Series(...)

```python
expected = pd.Series([data[0], None], dtype=data.dtype)
```

### Step 6: Assign result = expected.mode(...)

```python
result = expected.mode(dropna=False)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
more_nans = pd.Series([None, None, data[0]], dtype=data.dtype)
result = more_nans.mode(dropna=False)
expected = pd.Series([None], dtype=data.dtype)
tm.assert_series_equal(result, expected)
expected = pd.Series([data[0], None], dtype=data.dtype)
result = expected.mode(dropna=False)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arrow.py:1416 | Complexity: Intermediate | Last updated: 2026-06-02*