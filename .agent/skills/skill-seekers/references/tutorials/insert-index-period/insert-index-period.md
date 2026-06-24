# How To: Insert Index Period

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test insert index period

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: insert, coerced_val, coerced_dtype
```

## Step-by-Step Guide

### Step 1: Assign obj = pd.PeriodIndex(...)

```python
obj = pd.PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq='M')
```

**Verification:**
```python
assert obj.dtype == 'period[M]'
```

### Step 2: Assign data = value

```python
data = [pd.Period('2011-01', freq='M'), coerced_val, pd.Period('2011-02', freq='M'), pd.Period('2011-03', freq='M'), pd.Period('2011-04', freq='M')]
```

### Step 3: Assign exp = pd.PeriodIndex(...)

```python
exp = pd.PeriodIndex(data, freq='M')
```

### Step 4: Call self._assert_insert_conversion()

```python
self._assert_insert_conversion(obj, insert, exp, coerced_dtype)
```

### Step 5: Call self._assert_insert_conversion()

```python
self._assert_insert_conversion(obj, str(insert), exp, coerced_dtype)
```

### Step 6: Assign result = obj.insert(...)

```python
result = obj.insert(0, insert)
```

### Step 7: Assign expected = obj.astype.insert(...)

```python
expected = obj.astype(object).insert(0, insert)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign result = obj.insert(...)

```python
result = obj.insert(0, str(insert))
```

### Step 10: Assign expected = obj.astype.insert(...)

```python
expected = obj.astype(object).insert(0, str(insert))
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: insert, coerced_val, coerced_dtype

# Workflow
obj = pd.PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq='M')
assert obj.dtype == 'period[M]'
data = [pd.Period('2011-01', freq='M'), coerced_val, pd.Period('2011-02', freq='M'), pd.Period('2011-03', freq='M'), pd.Period('2011-04', freq='M')]
if isinstance(insert, pd.Period):
    exp = pd.PeriodIndex(data, freq='M')
    self._assert_insert_conversion(obj, insert, exp, coerced_dtype)
    self._assert_insert_conversion(obj, str(insert), exp, coerced_dtype)
else:
    result = obj.insert(0, insert)
    expected = obj.astype(object).insert(0, insert)
    tm.assert_index_equal(result, expected)
    if not isinstance(insert, pd.Timestamp):
        result = obj.insert(0, str(insert))
        expected = obj.astype(object).insert(0, str(insert))
        tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_coercion.py:328 | Complexity: Advanced | Last updated: 2026-06-02*