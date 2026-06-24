# How To: Shift Datetime

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift datetime

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign a = IntervalArray.from_breaks(...)

```python
a = IntervalArray.from_breaks(date_range('2000', periods=4))
```

### Step 2: Assign result = a.shift(...)

```python
result = a.shift(2)
```

### Step 3: Assign expected = a.take(...)

```python
expected = a.take([-1, -1, 0], allow_fill=True)
```

### Step 4: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(result, expected)
```

### Step 5: Assign result = a.shift(...)

```python
result = a.shift(-1)
```

### Step 6: Assign expected = a.take(...)

```python
expected = a.take([1, 2, -1], allow_fill=True)
```

### Step 7: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(result, expected)
```

### Step 8: Assign msg = 'can only insert Interval objects and NA into an IntervalArray'

```python
msg = 'can only insert Interval objects and NA into an IntervalArray'
```

### Step 9: Call a.shift()

```python
a.shift(1, fill_value=np.timedelta64('NaT', 'ns'))
```


## Complete Example

```python
# Workflow
a = IntervalArray.from_breaks(date_range('2000', periods=4))
result = a.shift(2)
expected = a.take([-1, -1, 0], allow_fill=True)
tm.assert_interval_array_equal(result, expected)
result = a.shift(-1)
expected = a.take([1, 2, -1], allow_fill=True)
tm.assert_interval_array_equal(result, expected)
msg = 'can only insert Interval objects and NA into an IntervalArray'
with pytest.raises(TypeError, match=msg):
    a.shift(1, fill_value=np.timedelta64('NaT', 'ns'))
```

## Next Steps


---

*Source: test_interval.py:100 | Complexity: Advanced | Last updated: 2026-06-02*