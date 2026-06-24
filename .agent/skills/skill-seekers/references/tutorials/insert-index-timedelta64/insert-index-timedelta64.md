# How To: Insert Index Timedelta64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert index timedelta64

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign obj = pd.TimedeltaIndex(...)

```python
obj = pd.TimedeltaIndex(['1 day', '2 day', '3 day', '4 day'])
```

**Verification:**
```python
assert obj.dtype == 'timedelta64[ns]'
```

### Step 2: Assign exp = pd.TimedeltaIndex(...)

```python
exp = pd.TimedeltaIndex(['1 day', '10 day', '2 day', '3 day', '4 day'])
```

**Verification:**
```python
assert expected.dtype == object
```

### Step 3: Call self._assert_insert_conversion()

```python
self._assert_insert_conversion(obj, pd.Timedelta('10 day'), exp, 'timedelta64[ns]')
```

### Step 4: Assign result = obj.insert(...)

```python
result = obj.insert(1, item)
```

### Step 5: Assign expected = obj.astype.insert(...)

```python
expected = obj.astype(object).insert(1, item)
```

**Verification:**
```python
assert expected.dtype == object
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
obj = pd.TimedeltaIndex(['1 day', '2 day', '3 day', '4 day'])
assert obj.dtype == 'timedelta64[ns]'
exp = pd.TimedeltaIndex(['1 day', '10 day', '2 day', '3 day', '4 day'])
self._assert_insert_conversion(obj, pd.Timedelta('10 day'), exp, 'timedelta64[ns]')
for item in [pd.Timestamp('2012-01-01'), 1]:
    result = obj.insert(1, item)
    expected = obj.astype(object).insert(1, item)
    assert expected.dtype == object
    tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_coercion.py:303 | Complexity: Intermediate | Last updated: 2026-06-02*