# How To: Apply Categorical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply categorical

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
# Fixtures: by_row, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign values = pd.Categorical(...)

```python
values = pd.Categorical(list('ABBABCD'), categories=list('DCBA'), ordered=True)
```

**Verification:**
```python
assert ser.apply(lambda x: 'A', by_row=by_row) == 'A'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(values, name='XX', index=list('abcdefg'))
```

**Verification:**
```python
assert result.dtype == object if not using_infer_string else 'str'
```

### Step 3: Assign result = ser.apply(...)

```python
result = ser.apply(lambda x: x.lower(), by_row=by_row)
```

### Step 4: Assign values = pd.Categorical(...)

```python
values = pd.Categorical(list('abbabcd'), categories=list('dcba'), ordered=True)
```

### Step 5: Assign exp = Series(...)

```python
exp = Series(values, name='XX', index=list('abcdefg'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 7: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result.values, exp.values)
```

### Step 8: Assign result = ser.apply(...)

```python
result = ser.apply(lambda x: 'A')
```

### Step 9: Assign exp = Series(...)

```python
exp = Series(['A'] * 7, name='XX', index=list('abcdefg'))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

**Verification:**
```python
assert result.dtype == object if not using_infer_string else 'str'
```

### Step 11: Assign msg = "Series' object has no attribute 'lower"

```python
msg = "Series' object has no attribute 'lower"
```

**Verification:**
```python
assert ser.apply(lambda x: 'A', by_row=by_row) == 'A'
```

### Step 12: Call ser.apply()

```python
ser.apply(lambda x: x.lower(), by_row=by_row)
```


## Complete Example

```python
# Setup
# Fixtures: by_row, using_infer_string

# Workflow
values = pd.Categorical(list('ABBABCD'), categories=list('DCBA'), ordered=True)
ser = Series(values, name='XX', index=list('abcdefg'))
if not by_row:
    msg = "Series' object has no attribute 'lower"
    with pytest.raises(AttributeError, match=msg):
        ser.apply(lambda x: x.lower(), by_row=by_row)
    assert ser.apply(lambda x: 'A', by_row=by_row) == 'A'
    return
result = ser.apply(lambda x: x.lower(), by_row=by_row)
values = pd.Categorical(list('abbabcd'), categories=list('dcba'), ordered=True)
exp = Series(values, name='XX', index=list('abcdefg'))
tm.assert_series_equal(result, exp)
tm.assert_categorical_equal(result.values, exp.values)
result = ser.apply(lambda x: 'A')
exp = Series(['A'] * 7, name='XX', index=list('abcdefg'))
tm.assert_series_equal(result, exp)
assert result.dtype == object if not using_infer_string else 'str'
```

## Next Steps


---

*Source: test_series_apply.py:224 | Complexity: Advanced | Last updated: 2026-06-02*