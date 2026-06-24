# How To: Series Apply Map Box Timestamps

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series apply map box timestamps

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
ser = Series(date_range('1/1/2000', periods=10))
```

### Step 2: Assign result = ser.apply(...)

```python
result = ser.apply(func, by_row=by_row)
```

### Step 3: Assign expected = ser.map(...)

```python
expected = ser.map(func)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign msg = "Series' object has no attribute 'hour'"

```python
msg = "Series' object has no attribute 'hour'"
```

### Step 6: Call ser.apply()

```python
ser.apply(func, by_row=by_row)
```


## Complete Example

```python
# Setup
# Fixtures: by_row

# Workflow
ser = Series(date_range('1/1/2000', periods=10))

def func(x):
    return (x.hour, x.day, x.month)
if not by_row:
    msg = "Series' object has no attribute 'hour'"
    with pytest.raises(AttributeError, match=msg):
        ser.apply(func, by_row=by_row)
    return
result = ser.apply(func, by_row=by_row)
expected = ser.map(func)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_series_apply.py:136 | Complexity: Intermediate | Last updated: 2026-06-02*