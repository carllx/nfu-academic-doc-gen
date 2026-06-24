# How To: Mul Td64Arr

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test mul td64arr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: left, box_cls
```

## Step-by-Step Guide

### Step 1: Assign right = np.array(...)

```python
right = np.array([1, 2, 3], dtype='m8[s]')
```

**Verification:**
```python
assert expected.dtype == right.dtype
```

### Step 2: Assign right = box_cls(...)

```python
right = box_cls(right)
```

### Step 3: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['10s', '40s', '90s'], dtype=right.dtype)
```

**Verification:**
```python
assert expected.dtype == right.dtype
```

### Step 4: Assign result = value

```python
result = left * right
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = right * left
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series(expected)
```


## Complete Example

```python
# Setup
# Fixtures: left, box_cls

# Workflow
right = np.array([1, 2, 3], dtype='m8[s]')
right = box_cls(right)
expected = TimedeltaIndex(['10s', '40s', '90s'], dtype=right.dtype)
if isinstance(left, Series) or box_cls is Series:
    expected = Series(expected)
assert expected.dtype == right.dtype
result = left * right
tm.assert_equal(result, expected)
result = right * left
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_numeric.py:177 | Complexity: Advanced | Last updated: 2026-06-02*