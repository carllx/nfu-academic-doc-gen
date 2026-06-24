# How To: Subclass That Overrides Eq

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclass that overrides eq

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

### Step 1: Assign a = np.array.view(...)

```python
a = np.array([1.0, 2.0]).view(MyArray)
```

**Verification:**
```python
assert_(type(a == a), bool)
```

### Step 2: Assign b = np.array.view(...)

```python
b = np.array([2.0, 3.0]).view(MyArray)
```

**Verification:**
```python
assert_(a == a)
```

### Step 3: Call assert_()

```python
assert_(type(a == a), bool)
```

**Verification:**
```python
assert_(a != b)
```

### Step 4: Call assert_()

```python
assert_(a == a)
```

### Step 5: Call assert_()

```python
assert_(a != b)
```

### Step 6: Call self._test_equal()

```python
self._test_equal(a, a)
```

### Step 7: Call self._test_not_equal()

```python
self._test_not_equal(a, b)
```

### Step 8: Call self._test_not_equal()

```python
self._test_not_equal(b, a)
```

### Step 9: Assign expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMax absolute difference among violations: 1.\nMax relative difference among violations: 0.5'

```python
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMax absolute difference among violations: 1.\nMax relative difference among violations: 0.5'
```

### Step 10: Assign c = np.array.view(...)

```python
c = np.array([0.0, 2.9]).view(MyArray)
```

### Step 11: Assign expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMax absolute difference among violations: 2.\nMax relative difference among violations: inf'

```python
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMax absolute difference among violations: 2.\nMax relative difference among violations: inf'
```

### Step 12: Call self._test_equal()

```python
self._test_equal(a, b)
```

### Step 13: Call self._test_equal()

```python
self._test_equal(b, c)
```


## Complete Example

```python
# Workflow
class MyArray(np.ndarray):

    def __eq__(self, other):
        return bool(np.equal(self, other).all())

    def __ne__(self, other):
        return not self == other
a = np.array([1.0, 2.0]).view(MyArray)
b = np.array([2.0, 3.0]).view(MyArray)
assert_(type(a == a), bool)
assert_(a == a)
assert_(a != b)
self._test_equal(a, a)
self._test_not_equal(a, b)
self._test_not_equal(b, a)
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMax absolute difference among violations: 1.\nMax relative difference among violations: 0.5'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._test_equal(a, b)
c = np.array([0.0, 2.9]).view(MyArray)
expected_msg = 'Mismatched elements: 1 / 2 (50%)\nMax absolute difference among violations: 2.\nMax relative difference among violations: inf'
with pytest.raises(AssertionError, match=re.escape(expected_msg)):
    self._test_equal(b, c)
```

## Next Steps


---

*Source: test_utils.py:237 | Complexity: Advanced | Last updated: 2026-06-02*