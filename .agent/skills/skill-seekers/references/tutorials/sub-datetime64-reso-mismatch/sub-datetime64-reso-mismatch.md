# How To: Sub Datetime64 Reso Mismatch

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sub datetime64 reso mismatch

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `zoneinfo`


## Step-by-Step Guide

### Step 1: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('2016-01-01', periods=3)
```

### Step 2: Assign left = dti._data.as_unit(...)

```python
left = dti._data.as_unit('s')
```

### Step 3: Assign right = left.as_unit(...)

```python
right = left.as_unit('ms')
```

### Step 4: Assign result = value

```python
result = left - right
```

### Step 5: Assign exp_values = np.array(...)

```python
exp_values = np.array([0, 0, 0], dtype='m8[ms]')
```

### Step 6: Assign expected = TimedeltaArray._simple_new(...)

```python
expected = TimedeltaArray._simple_new(exp_values, dtype=exp_values.dtype)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 8: Assign result2 = value

```python
result2 = right - left
```

### Step 9: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result2, expected)
```


## Complete Example

```python
# Workflow
dti = pd.date_range('2016-01-01', periods=3)
left = dti._data.as_unit('s')
right = left.as_unit('ms')
result = left - right
exp_values = np.array([0, 0, 0], dtype='m8[ms]')
expected = TimedeltaArray._simple_new(exp_values, dtype=exp_values.dtype)
tm.assert_extension_array_equal(result, expected)
result2 = right - left
tm.assert_extension_array_equal(result2, expected)
```

## Next Steps


---

*Source: test_datetimes.py:259 | Complexity: Advanced | Last updated: 2026-06-02*