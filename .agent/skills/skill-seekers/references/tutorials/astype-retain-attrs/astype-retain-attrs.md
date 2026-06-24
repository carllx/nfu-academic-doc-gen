# How To: Astype Retain Attrs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype retain attrs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `importlib`
- `string`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([0, 1, 2, 3])
```

### Step 2: Assign unknown = 'Michigan'

```python
ser.attrs['Location'] = 'Michigan'
```

### Step 3: Assign result = value

```python
result = ser.astype(any_numpy_dtype).attrs
```

### Step 4: Assign expected = value

```python
expected = ser.attrs
```

### Step 5: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: any_numpy_dtype

# Workflow
ser = Series([0, 1, 2, 3])
ser.attrs['Location'] = 'Michigan'
result = ser.astype(any_numpy_dtype).attrs
expected = ser.attrs
tm.assert_dict_equal(expected, result)
```

## Next Steps


---

*Source: test_astype.py:490 | Complexity: Intermediate | Last updated: 2026-06-02*