# How To: Series Set Value

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series set value

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = [datetime(2001, 1, 1), datetime(2001, 1, 2)]
```

### Step 2: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(dates)
```

### Step 3: Assign s = Series(...)

```python
s = Series(dtype=object)
```

### Step 4: Call s._set_value()

```python
s._set_value(dates[0], 1.0)
```

### Step 5: Call s._set_value()

```python
s._set_value(dates[1], np.nan)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1.0, np.nan], index=index)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```


## Complete Example

```python
# Workflow
dates = [datetime(2001, 1, 1), datetime(2001, 1, 2)]
index = DatetimeIndex(dates)
s = Series(dtype=object)
s._set_value(dates[0], 1.0)
s._set_value(dates[1], np.nan)
expected = Series([1.0, np.nan], index=index)
tm.assert_series_equal(s, expected)
```

## Next Steps


---

*Source: test_set_value.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*