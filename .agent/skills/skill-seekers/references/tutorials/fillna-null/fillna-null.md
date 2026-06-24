# How To: Fillna Null

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fillna null

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: null_obj, index_or_series_obj
```

## Step-by-Step Guide

### Step 1: Assign obj = index_or_series_obj

```python
obj = index_or_series_obj
```

**Verification:**
```python
assert obj is not result
```

### Step 2: Assign klass = type(...)

```python
klass = type(obj)
```

### Step 3: Assign values = value

```python
values = obj._values
```

### Step 4: Assign fill_value = value

```python
fill_value = values[0]
```

### Step 5: Assign expected = values.copy(...)

```python
expected = values.copy()
```

### Step 6: Assign unknown = null_obj

```python
values[0:2] = null_obj
```

### Step 7: Assign unknown = fill_value

```python
expected[0:2] = fill_value
```

### Step 8: Assign expected = klass(...)

```python
expected = klass(expected)
```

### Step 9: Assign obj = klass(...)

```python
obj = klass(values)
```

### Step 10: Assign result = obj.fillna(...)

```python
result = obj.fillna(fill_value)
```

### Step 11: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

**Verification:**
```python
assert obj is not result
```

### Step 12: Call pytest.skip()

```python
pytest.skip(f"{klass} doesn't allow for NA operations")
```

### Step 13: Call pytest.skip()

```python
pytest.skip("Test doesn't make sense on empty data")
```

### Step 14: Call pytest.skip()

```python
pytest.skip(f"MultiIndex can't hold '{null_obj}'")
```


## Complete Example

```python
# Setup
# Fixtures: null_obj, index_or_series_obj

# Workflow
obj = index_or_series_obj
klass = type(obj)
if not allow_na_ops(obj):
    pytest.skip(f"{klass} doesn't allow for NA operations")
elif len(obj) < 1:
    pytest.skip("Test doesn't make sense on empty data")
elif isinstance(obj, MultiIndex):
    pytest.skip(f"MultiIndex can't hold '{null_obj}'")
values = obj._values
fill_value = values[0]
expected = values.copy()
values[0:2] = null_obj
expected[0:2] = fill_value
expected = klass(expected)
obj = klass(values)
result = obj.fillna(fill_value)
tm.assert_equal(result, expected)
assert obj is not result
```

## Next Steps


---

*Source: test_fillna.py:35 | Complexity: Advanced | Last updated: 2026-06-02*