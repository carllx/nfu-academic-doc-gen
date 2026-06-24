# How To: Dtypes Gh8722

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dtypes gh8722

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_string_frame
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
float_string_frame['bool'] = float_string_frame['A'] > 0
```

### Step 2: Assign result = value

```python
result = float_string_frame.dtypes
```

### Step 3: Assign expected = Series(...)

```python
expected = Series({k: v.dtype for k, v in float_string_frame.items()}, index=result.index)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign msg = 'use_inf_as_na option is deprecated'

```python
msg = 'use_inf_as_na option is deprecated'
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame([[1]])
```

### Step 7: Assign result = value

```python
result = df.dtypes
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series({0: np.dtype('int64')}))
```


## Complete Example

```python
# Setup
# Fixtures: float_string_frame

# Workflow
float_string_frame['bool'] = float_string_frame['A'] > 0
result = float_string_frame.dtypes
expected = Series({k: v.dtype for k, v in float_string_frame.items()}, index=result.index)
tm.assert_series_equal(result, expected)
msg = 'use_inf_as_na option is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    with option_context('use_inf_as_na', True):
        df = DataFrame([[1]])
        result = df.dtypes
        tm.assert_series_equal(result, Series({0: np.dtype('int64')}))
```

## Next Steps


---

*Source: test_dtypes.py:90 | Complexity: Advanced | Last updated: 2026-06-02*