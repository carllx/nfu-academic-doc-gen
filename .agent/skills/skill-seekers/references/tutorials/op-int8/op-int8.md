# How To: Op Int8

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test op int8

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: left_array, right_array, opname
```

## Step-by-Step Guide

### Step 1: Assign op = getattr(...)

```python
op = getattr(operator, opname)
```

### Step 2: Assign result = op(...)

```python
result = op(left_array, right_array)
```

### Step 3: Assign expected = op(...)

```python
expected = op(left_array.astype('Int8'), right_array.astype('Int8'))
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign msg = "operator '.*' not implemented for bool dtypes"

```python
msg = "operator '.*' not implemented for bool dtypes"
```

### Step 6: Assign result = op(...)

```python
result = op(left_array, right_array)
```


## Complete Example

```python
# Setup
# Fixtures: left_array, right_array, opname

# Workflow
op = getattr(operator, opname)
if opname != 'mod':
    msg = "operator '.*' not implemented for bool dtypes"
    with pytest.raises(NotImplementedError, match=msg):
        result = op(left_array, right_array)
    return
result = op(left_array, right_array)
expected = op(left_array.astype('Int8'), right_array.astype('Int8'))
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*