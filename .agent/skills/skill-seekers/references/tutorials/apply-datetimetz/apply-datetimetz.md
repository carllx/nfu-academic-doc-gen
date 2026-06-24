# How To: Apply Datetimetz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply datetimetz

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

### Step 1: Assign values = date_range.tz_localize(...)

```python
values = date_range('2011-01-01', '2011-01-02', freq='h').tz_localize('Asia/Tokyo')
```

**Verification:**
```python
assert result == 'Asia/Tokyo'
```

### Step 2: Assign s = Series(...)

```python
s = Series(values, name='XX')
```

### Step 3: Assign result = s.apply(...)

```python
result = s.apply(lambda x: x + pd.offsets.Day(), by_row=by_row)
```

### Step 4: Assign exp_values = date_range.tz_localize(...)

```python
exp_values = date_range('2011-01-02', '2011-01-03', freq='h').tz_localize('Asia/Tokyo')
```

### Step 5: Assign exp = Series(...)

```python
exp = Series(exp_values, name='XX')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 7: Assign result = s.apply(...)

```python
result = s.apply(lambda x: x.hour if by_row else x.dt.hour, by_row=by_row)
```

### Step 8: Assign exp = Series(...)

```python
exp = Series(list(range(24)) + [0], name='XX', dtype='int64' if by_row else 'int32')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 10: Assign result = s.apply(...)

```python
result = s.apply(f, by_row=by_row)
```

### Step 11: Assign exp = Series(...)

```python
exp = Series(['Asia/Tokyo'] * 25, name='XX')
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

**Verification:**
```python
assert result == 'Asia/Tokyo'
```


## Complete Example

```python
# Setup
# Fixtures: by_row

# Workflow
values = date_range('2011-01-01', '2011-01-02', freq='h').tz_localize('Asia/Tokyo')
s = Series(values, name='XX')
result = s.apply(lambda x: x + pd.offsets.Day(), by_row=by_row)
exp_values = date_range('2011-01-02', '2011-01-03', freq='h').tz_localize('Asia/Tokyo')
exp = Series(exp_values, name='XX')
tm.assert_series_equal(result, exp)
result = s.apply(lambda x: x.hour if by_row else x.dt.hour, by_row=by_row)
exp = Series(list(range(24)) + [0], name='XX', dtype='int64' if by_row else 'int32')
tm.assert_series_equal(result, exp)

def f(x):
    return str(x.tz) if by_row else str(x.dt.tz)
result = s.apply(f, by_row=by_row)
if by_row:
    exp = Series(['Asia/Tokyo'] * 25, name='XX')
    tm.assert_series_equal(result, exp)
else:
    assert result == 'Asia/Tokyo'
```

## Next Steps


---

*Source: test_series_apply.py:197 | Complexity: Advanced | Last updated: 2026-06-02*