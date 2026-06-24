# How To: Constructor Dict With Tzaware Scalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor dict with tzaware scalar

## Prerequisites

**Required Modules:**
- `array`
- `collections`
- `collections.abc`
- `dataclasses`
- `datetime`
- `functools`
- `re`
- `numpy`
- `numpy`
- `numpy.ma`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `numpy.dtypes`


## Step-by-Step Guide

### Step 1: Assign dt = Timestamp.tz_convert(...)

```python
dt = Timestamp('2019-11-03 01:00:00-0700').tz_convert('America/Los_Angeles')
```

### Step 2: Assign dt = dt.as_unit(...)

```python
dt = dt.as_unit('ns')
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'dt': dt}, index=[0])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'dt': [dt]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'dt': dt, 'value': [1]})
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'dt': [dt], 'value': [1]})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
dt = Timestamp('2019-11-03 01:00:00-0700').tz_convert('America/Los_Angeles')
dt = dt.as_unit('ns')
df = DataFrame({'dt': dt}, index=[0])
expected = DataFrame({'dt': [dt]})
tm.assert_frame_equal(df, expected)
df = DataFrame({'dt': dt, 'value': [1]})
expected = DataFrame({'dt': [dt], 'value': [1]})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_constructors.py:97 | Complexity: Advanced | Last updated: 2026-06-02*