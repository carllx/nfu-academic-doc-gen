# How To: Array Vs Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array vs scalar

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

### Step 1: Assign a = value

```python
a = [5498.42354, 849.54345, 0.0]
```

### Step 2: Assign b = 5498.42354

```python
b = 5498.42354
```

### Step 3: Assign expected_msg = 'Mismatched elements: 2 / 3 (66.7%)\nMismatch at indices:\n [1]: 849.54345 (ACTUAL), 5498.42354 (DESIRED)\n [2]: 0.0 (ACTUAL), 5498.42354 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: 1.'

```python
expected_msg = 'Mismatched elements: 2 / 3 (66.7%)\nMismatch at indices:\n [1]: 849.54345 (ACTUAL), 5498.42354 (DESIRED)\n [2]: 0.0 (ACTUAL), 5498.42354 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: 1.'
```

### Step 4: Assign expected_msg = 'Mismatched elements: 2 / 3 (66.7%)\nMismatch at indices:\n [1]: 5498.42354 (ACTUAL), 849.54345 (DESIRED)\n [2]: 5498.42354 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: 5.4722099'

```python
expected_msg = 'Mismatched elements: 2 / 3 (66.7%)\nMismatch at indices:\n [1]: 5498.42354 (ACTUAL), 849.54345 (DESIRED)\n [2]: 5498.42354 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: 5.4722099'
```

### Step 5: Assign a = value

```python
a = [5498.42354, 0.0]
```

### Step 6: Assign expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 5498.42354 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: inf'

```python
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 5498.42354 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: inf'
```

### Step 7: Assign b = 0

```python
b = 0
```

### Step 8: Assign expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [0]: 5498.42354 (ACTUAL), 0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: inf'

```python
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [0]: 5498.42354 (ACTUAL), 0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: inf'
```

### Step 9: Call self._assert_func()

```python
self._assert_func(a, b, decimal=9)
```

### Step 10: Call self._assert_func()

```python
self._assert_func(b, a, decimal=9)
```

### Step 11: Call self._assert_func()

```python
self._assert_func(b, a, decimal=7)
```

### Step 12: Call self._assert_func()

```python
self._assert_func(a, b, decimal=7)
```


## Complete Example

```python
# Workflow
a = [5498.42354, 849.54345, 0.0]
b = 5498.42354
expected_msg = 'Mismatched elements: 2 / 3 (66.7%)\nMismatch at indices:\n [1]: 849.54345 (ACTUAL), 5498.42354 (DESIRED)\n [2]: 0.0 (ACTUAL), 5498.42354 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: 1.'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(a, b, decimal=9)
expected_msg = 'Mismatched elements: 2 / 3 (66.7%)\nMismatch at indices:\n [1]: 5498.42354 (ACTUAL), 849.54345 (DESIRED)\n [2]: 5498.42354 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: 5.4722099'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(b, a, decimal=9)
a = [5498.42354, 0.0]
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [1]: 5498.42354 (ACTUAL), 0.0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: inf'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(b, a, decimal=7)
b = 0
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMismatch at index:\n [0]: 5498.42354 (ACTUAL), 0 (DESIRED)\nMax absolute difference among violations: 5498.42354\nMax relative difference among violations: inf'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._assert_func(a, b, decimal=7)
```

## Next Steps


---

*Source: test_utils.py:553 | Complexity: Advanced | Last updated: 2026-06-02*