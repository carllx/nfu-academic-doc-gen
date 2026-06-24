# How To: 0 Ndim Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 0 ndim array

## Prerequisites

**Required Modules:**
- `itertools`
- `os`
- `re`
- `sys`
- `warnings`
- `weakref`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array(473963742225900817127911193656584771)
```

**Verification:**
```python
assert_('Mismatched elements: 1 / 1 (100%)\n' in msg)
```

### Step 2: Assign y = np.array(...)

```python
y = np.array(18535119325151578301457182298393896)
```

### Step 3: Assign msg = str(...)

```python
msg = str(exc_info.value)
```

### Step 4: Call assert_()

```python
assert_('Mismatched elements: 1 / 1 (100%)\n' in msg)
```

### Step 5: Assign y = x

```python
y = x
```

### Step 6: Call self._assert_func()

```python
self._assert_func(x, y)
```

### Step 7: Assign x = np.array(...)

```python
x = np.array(4395065348745.5645)
```

### Step 8: Assign y = np.array(...)

```python
y = np.array(0)
```

### Step 9: Assign expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMax absolute difference among violations: 4.39506535e+12\nMax relative difference among violations: inf\n'

```python
expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMax absolute difference among violations: 4.39506535e+12\nMax relative difference among violations: inf\n'
```

### Step 10: Assign x = y

```python
x = y
```

### Step 11: Call self._assert_func()

```python
self._assert_func(x, y)
```

### Step 12: Call self._assert_func()

```python
self._assert_func(x, y)
```

### Step 13: Call self._assert_func()

```python
self._assert_func(x, y)
```


## Complete Example

```python
# Workflow
x = np.array(473963742225900817127911193656584771)
y = np.array(18535119325151578301457182298393896)
with pytest.raises(AssertionError) as exc_info:
    self._assert_func(x, y)
msg = str(exc_info.value)
assert_('Mismatched elements: 1 / 1 (100%)\n' in msg)
y = x
self._assert_func(x, y)
x = np.array(4395065348745.5645)
y = np.array(0)
expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMax absolute difference among violations: 4.39506535e+12\nMax relative difference among violations: inf\n'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(x, y)
x = y
self._assert_func(x, y)
```

## Next Steps


---

*Source: test_utils.py:110 | Complexity: Advanced | Last updated: 2026-06-02*