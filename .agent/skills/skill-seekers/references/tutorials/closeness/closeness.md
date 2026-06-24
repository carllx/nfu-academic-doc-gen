# How To: Closeness

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test closeness

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

### Step 1: Assign expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMax absolute difference among violations: 1.5\nMax relative difference among violations: inf'

```python
expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMax absolute difference among violations: 1.5\nMax relative difference among violations: inf'
```

### Step 2: Call self._assert_func()

```python
self._assert_func([1.499999], [0.0], decimal=0)
```

### Step 3: Assign expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMismatch at index:\n [0]: 1.5 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 1.5\nMax relative difference among violations: inf'

```python
expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMismatch at index:\n [0]: 1.5 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 1.5\nMax relative difference among violations: inf'
```

### Step 4: Assign a = value

```python
a = [1.4999999, 3e-05]
```

### Step 5: Assign b = value

```python
b = [1.49999991, 0]
```

### Step 6: Assign expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 3e-05 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 3.e-05\nMax relative difference among violations: inf'

```python
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 3e-05 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 3.e-05\nMax relative difference among violations: inf'
```

### Step 7: Assign expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 0.0 (ACTUAL), 3e-05 (DESIRED)\nMax absolute difference among violations: 3.e-05\nMax relative difference among violations: 1.'

```python
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 0.0 (ACTUAL), 3e-05 (DESIRED)\nMax absolute difference among violations: 3.e-05\nMax relative difference among violations: 1.'
```

### Step 8: Call self._assert_func()

```python
self._assert_func(1.5, 0.0, decimal=0)
```

### Step 9: Call self._assert_func()

```python
self._assert_func([1.5], [0.0], decimal=0)
```

### Step 10: Call self._assert_func()

```python
self._assert_func(a, b, decimal=7)
```

### Step 11: Call self._assert_func()

```python
self._assert_func(b, a, decimal=7)
```


## Complete Example

```python
# Workflow
expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMax absolute difference among violations: 1.5\nMax relative difference among violations: inf'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(1.5, 0.0, decimal=0)
self._assert_func([1.499999], [0.0], decimal=0)
expected_msg = 'Mismatched elements: 1 / 1 (100%)\nMismatch at index:\n [0]: 1.5 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 1.5\nMax relative difference among violations: inf'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func([1.5], [0.0], decimal=0)
a = [1.4999999, 3e-05]
b = [1.49999991, 0]
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 3e-05 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 3.e-05\nMax relative difference among violations: inf'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(a, b, decimal=7)
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 0.0 (ACTUAL), 3e-05 (DESIRED)\nMax absolute difference among violations: 3.e-05\nMax relative difference among violations: 1.'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(b, a, decimal=7)
```

## Next Steps


---

*Source: test_utils.py:493 | Complexity: Advanced | Last updated: 2026-06-02*