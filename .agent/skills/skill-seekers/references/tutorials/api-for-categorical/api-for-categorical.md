# How To: Api For Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test api for categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.core.strings.accessor`

**Required Fixtures:**
- `api_client` fixture

**Setup Required:**
```python
# Fixtures: any_string_method, any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(list('aabb'), dtype=any_string_dtype)
```

**Verification:**
```python
assert isinstance(c.str, StringMethods)
```

### Step 2: Assign s = value

```python
s = s + ' ' + s
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign c = s.astype(...)

```python
c = s.astype('category')
```

### Step 4: Assign c = c.astype(...)

```python
c = c.astype(CategoricalDtype(c.dtype.categories.astype('object')))
```

**Verification:**
```python
assert isinstance(c.str, StringMethods)
```

### Step 5: Assign unknown = any_string_method

```python
method_name, args, kwargs = any_string_method
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(c.str, method_name)(*args, **kwargs)
```

### Step 7: Assign expected = getattr(...)

```python
expected = getattr(s.astype('object').str, method_name)(*args, **kwargs)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: any_string_method, any_string_dtype

# Workflow
s = Series(list('aabb'), dtype=any_string_dtype)
s = s + ' ' + s
c = s.astype('category')
c = c.astype(CategoricalDtype(c.dtype.categories.astype('object')))
assert isinstance(c.str, StringMethods)
method_name, args, kwargs = any_string_method
result = getattr(c.str, method_name)(*args, **kwargs)
expected = getattr(s.astype('object').str, method_name)(*args, **kwargs)
if isinstance(result, DataFrame):
    tm.assert_frame_equal(result, expected)
elif isinstance(result, Series):
    tm.assert_series_equal(result, expected)
else:
    assert result == expected
```

## Next Steps


---

*Source: test_api.py:186 | Complexity: Advanced | Last updated: 2026-06-02*