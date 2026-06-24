# How To: Equals Mismatched Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals mismatched nas

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `copy`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nulls_fixture, nulls_fixture2
```

## Step-by-Step Guide

### Step 1: Assign left = nulls_fixture

```python
left = nulls_fixture
```

**Verification:**
```python
assert ser.equals(ser2)
```

### Step 2: Assign right = nulls_fixture2

```python
right = nulls_fixture2
```

**Verification:**
```python
assert ser.equals(ser2)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([left], dtype=object)
```

**Verification:**
```python
assert not ser.equals(ser2)
```

### Step 4: Assign ser2 = Series(...)

```python
ser2 = Series([right], dtype=object)
```

### Step 5: Assign right = right.copy(...)

```python
right = right.copy()
```

### Step 6: Assign right = copy.copy(...)

```python
right = copy.copy(right)
```

**Verification:**
```python
assert ser.equals(ser2)
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture, nulls_fixture2

# Workflow
left = nulls_fixture
right = nulls_fixture2
if hasattr(right, 'copy'):
    right = right.copy()
else:
    right = copy.copy(right)
ser = Series([left], dtype=object)
ser2 = Series([right], dtype=object)
if is_matching_na(left, right):
    assert ser.equals(ser2)
elif left is None and is_float(right) or (right is None and is_float(left)):
    assert ser.equals(ser2)
else:
    assert not ser.equals(ser2)
```

## Next Steps


---

*Source: test_equals.py:103 | Complexity: Intermediate | Last updated: 2026-06-02*