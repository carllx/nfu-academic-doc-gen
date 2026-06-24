# How To: Fillna No Op Returns Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna no op returns copy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `string`
- `typing`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.base`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays`
- `pandas.core.arrays.string_`
- `pandas.tests.arrays.string_.test_string`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = data[~data.isna()]
```

**Verification:**
```python
assert result is not data
```

### Step 2: Assign valid = value

```python
valid = data[0]
```

**Verification:**
```python
assert result is not data
```

### Step 3: Assign result = data.fillna(...)

```python
result = data.fillna(valid)
```

**Verification:**
```python
assert result is not data
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, data)
```

### Step 5: Assign result = data.fillna(...)

```python
result = data.fillna(method='backfill')
```

**Verification:**
```python
assert result is not data
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, data)
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
data = data[~data.isna()]
valid = data[0]
result = data.fillna(valid)
assert result is not data
tm.assert_extension_array_equal(result, data)
result = data.fillna(method='backfill')
assert result is not data
tm.assert_extension_array_equal(result, data)
```

## Next Steps


---

*Source: test_string.py:156 | Complexity: Intermediate | Last updated: 2026-06-02*