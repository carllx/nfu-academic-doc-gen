# How To: Isin Mixed Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Test that isin works as expected for mixed dtype input.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.dtypes`
- `numpy.exceptions`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype1, dtype2, kind
```

## Step-by-Step Guide

### Step 1: 'Test that isin works as expected for mixed dtype input.'

```python
'Test that isin works as expected for mixed dtype input.'
```

**Verification:**
```python
assert_array_equal(isin(ar1, ar2, kind=kind), expected)
```

### Step 2: Assign is_dtype2_signed = np.issubdtype(...)

```python
is_dtype2_signed = np.issubdtype(dtype2, np.signedinteger)
```

### Step 3: Assign ar1 = np.array(...)

```python
ar1 = np.array([0, 0, 1, 1], dtype=dtype1)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([True, True, False, False])
```

### Step 5: Assign expect_failure = value

```python
expect_failure = kind == 'table' and (dtype1 == np.int16 and dtype2 == np.int8)
```

### Step 6: Assign ar2 = np.array(...)

```python
ar2 = np.array([-128, 0, 127], dtype=dtype2)
```

### Step 7: Assign ar2 = np.array(...)

```python
ar2 = np.array([127, 0, 255], dtype=dtype2)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(isin(ar1, ar2, kind=kind), expected)
```

### Step 9: Call isin()

```python
isin(ar1, ar2, kind=kind)
```


## Complete Example

```python
# Setup
# Fixtures: dtype1, dtype2, kind

# Workflow
'Test that isin works as expected for mixed dtype input.'
is_dtype2_signed = np.issubdtype(dtype2, np.signedinteger)
ar1 = np.array([0, 0, 1, 1], dtype=dtype1)
if is_dtype2_signed:
    ar2 = np.array([-128, 0, 127], dtype=dtype2)
else:
    ar2 = np.array([127, 0, 255], dtype=dtype2)
expected = np.array([True, True, False, False])
expect_failure = kind == 'table' and (dtype1 == np.int16 and dtype2 == np.int8)
if expect_failure:
    with pytest.raises(RuntimeError, match='exceed the maximum'):
        isin(ar1, ar2, kind=kind)
else:
    assert_array_equal(isin(ar1, ar2, kind=kind), expected)
```

## Next Steps


---

*Source: test_arraysetops.py:425 | Complexity: Advanced | Last updated: 2026-06-02*