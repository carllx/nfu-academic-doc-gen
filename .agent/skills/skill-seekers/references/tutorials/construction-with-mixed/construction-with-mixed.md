# How To: Construction With Mixed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construction with mixed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.internals.blocks`

**Setup Required:**
```python
# Fixtures: float_string_frame, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign unknown = datetime.now(...)

```python
float_string_frame['datetime'] = datetime.now()
```

**Verification:**
```python
assert float_string_frame['datetime'].dtype == 'M8[us]'
```

### Step 2: Assign unknown = timedelta(...)

```python
float_string_frame['timedelta'] = timedelta(days=1, seconds=1)
```

**Verification:**
```python
assert float_string_frame['timedelta'].dtype == 'm8[us]'
```

### Step 3: Assign result = value

```python
result = float_string_frame.dtypes
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64')] * 4 + [np.dtype('object') if not using_infer_string else pd.StringDtype(na_value=np.nan), np.dtype('datetime64[us]'), np.dtype('timedelta64[us]')], index=list('ABCD') + ['foo', 'datetime', 'timedelta'])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_string_frame, using_infer_string

# Workflow
float_string_frame['datetime'] = datetime.now()
float_string_frame['timedelta'] = timedelta(days=1, seconds=1)
assert float_string_frame['datetime'].dtype == 'M8[us]'
assert float_string_frame['timedelta'].dtype == 'm8[us]'
result = float_string_frame.dtypes
expected = Series([np.dtype('float64')] * 4 + [np.dtype('object') if not using_infer_string else pd.StringDtype(na_value=np.nan), np.dtype('datetime64[us]'), np.dtype('timedelta64[us]')], index=list('ABCD') + ['foo', 'datetime', 'timedelta'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_block_internals.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*