# How To: Describe With Tz Numeric

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe with tz numeric

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign name, tz = 'CET'

```python
name = tz = 'CET'
```

### Step 2: Assign start = Timestamp(...)

```python
start = Timestamp(2018, 1, 1)
```

### Step 3: Assign end = Timestamp(...)

```python
end = Timestamp(2018, 1, 5)
```

### Step 4: Assign s = Series(...)

```python
s = Series(date_range(start, end, tz=tz), name=name)
```

### Step 5: Assign result = s.describe(...)

```python
result = s.describe()
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([5, Timestamp('2018-01-03 00:00:00', tz=tz), Timestamp('2018-01-01 00:00:00', tz=tz), Timestamp('2018-01-02 00:00:00', tz=tz), Timestamp('2018-01-03 00:00:00', tz=tz), Timestamp('2018-01-04 00:00:00', tz=tz), Timestamp('2018-01-05 00:00:00', tz=tz)], name=name, index=['count', 'mean', 'min', '25%', '50%', '75%', 'max'])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
name = tz = 'CET'
start = Timestamp(2018, 1, 1)
end = Timestamp(2018, 1, 5)
s = Series(date_range(start, end, tz=tz), name=name)
result = s.describe()
expected = Series([5, Timestamp('2018-01-03 00:00:00', tz=tz), Timestamp('2018-01-01 00:00:00', tz=tz), Timestamp('2018-01-02 00:00:00', tz=tz), Timestamp('2018-01-03 00:00:00', tz=tz), Timestamp('2018-01-04 00:00:00', tz=tz), Timestamp('2018-01-05 00:00:00', tz=tz)], name=name, index=['count', 'mean', 'min', '25%', '50%', '75%', 'max'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:121 | Complexity: Intermediate | Last updated: 2026-06-02*