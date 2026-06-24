# How To: From Arrays Mismatched Datetimelike Resos

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test from arrays mismatched datetimelike resos

## Prerequisites

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign left = date_range(...)

```python
left = date_range('2016-01-01', periods=3, unit='s')
```

### Step 2: Assign right = date_range(...)

```python
right = date_range('2017-01-01', periods=3, unit='ms')
```

### Step 3: Assign result = interval_cls.from_arrays(...)

```python
result = interval_cls.from_arrays(left, right)
```

### Step 4: Assign expected = interval_cls.from_arrays(...)

```python
expected = interval_cls.from_arrays(left.as_unit('ms'), right)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign left2 = value

```python
left2 = left - left[0]
```

### Step 7: Assign right2 = value

```python
right2 = right - left[0]
```

### Step 8: Assign result2 = interval_cls.from_arrays(...)

```python
result2 = interval_cls.from_arrays(left2, right2)
```

### Step 9: Assign expected2 = interval_cls.from_arrays(...)

```python
expected2 = interval_cls.from_arrays(left2.as_unit('ms'), right2)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(result2, expected2)
```

### Step 11: Assign left3 = left.tz_localize(...)

```python
left3 = left.tz_localize('UTC')
```

### Step 12: Assign right3 = right.tz_localize(...)

```python
right3 = right.tz_localize('UTC')
```

### Step 13: Assign result3 = interval_cls.from_arrays(...)

```python
result3 = interval_cls.from_arrays(left3, right3)
```

### Step 14: Assign expected3 = interval_cls.from_arrays(...)

```python
expected3 = interval_cls.from_arrays(left3.as_unit('ms'), right3)
```

### Step 15: Call tm.assert_equal()

```python
tm.assert_equal(result3, expected3)
```


## Complete Example

```python
# Workflow
left = date_range('2016-01-01', periods=3, unit='s')
right = date_range('2017-01-01', periods=3, unit='ms')
result = interval_cls.from_arrays(left, right)
expected = interval_cls.from_arrays(left.as_unit('ms'), right)
tm.assert_equal(result, expected)
left2 = left - left[0]
right2 = right - left[0]
result2 = interval_cls.from_arrays(left2, right2)
expected2 = interval_cls.from_arrays(left2.as_unit('ms'), right2)
tm.assert_equal(result2, expected2)
left3 = left.tz_localize('UTC')
right3 = right.tz_localize('UTC')
result3 = interval_cls.from_arrays(left3, right3)
expected3 = interval_cls.from_arrays(left3.as_unit('ms'), right3)
tm.assert_equal(result3, expected3)
```

## Next Steps


---

*Source: test_constructors.py:263 | Complexity: Advanced | Last updated: 2026-06-02*