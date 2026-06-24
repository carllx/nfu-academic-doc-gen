# How To: Series Map Box Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series map box timedelta

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`

**Setup Required:**
```python
# Fixtures: by_row
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(timedelta_range('1 day 1 s', periods=3, freq='h'))
```

### Step 2: Assign result = ser.apply(...)

```python
result = ser.apply(f, by_row=by_row)
```

### Step 3: Assign expected = ser.map(...)

```python
expected = ser.map(lambda x: x.total_seconds())
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([86401.0, 90001.0, 93601.0])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: by_row

# Workflow
ser = Series(timedelta_range('1 day 1 s', periods=3, freq='h'))

def f(x):
    return x.total_seconds() if by_row else x.dt.total_seconds()
result = ser.apply(f, by_row=by_row)
expected = ser.map(lambda x: x.total_seconds())
tm.assert_series_equal(result, expected)
expected = Series([86401.0, 90001.0, 93601.0])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_series_apply.py:23 | Complexity: Intermediate | Last updated: 2026-06-02*