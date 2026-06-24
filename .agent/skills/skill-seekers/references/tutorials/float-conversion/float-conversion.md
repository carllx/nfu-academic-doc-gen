# How To: Float Conversion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Some tests that the conversion to float64 works as accurately as the
Python built-in `float` function. In a naive version of the float parser,
these strings resulted in values that were off by an ULP or two.

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `io`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: '\n    Some tests that the conversion to float64 works as accurately as the\n    Python built-in `float` function. In a naive version of the float parser,\n    these strings resulted in values that were off by an ULP or two.\n    '

```python
'\n    Some tests that the conversion to float64 works as accurately as the\n    Python built-in `float` function. In a naive version of the float parser,\n    these strings resulted in values that were off by an ULP or two.\n    '
```

**Verification:**
```python
assert_equal(res, expected)
```

### Step 2: Assign strings = value

```python
strings = ['0.9999999999999999', '9876543210.123456', '5.43215432154321e+300', '0.901', '0.333']
```

### Step 3: Assign txt = StringIO(...)

```python
txt = StringIO('\n'.join(strings))
```

### Step 4: Assign res = np.loadtxt(...)

```python
res = np.loadtxt(txt)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([float(s) for s in strings])
```

### Step 6: Call assert_equal()

```python
assert_equal(res, expected)
```


## Complete Example

```python
# Workflow
'\n    Some tests that the conversion to float64 works as accurately as the\n    Python built-in `float` function. In a naive version of the float parser,\n    these strings resulted in values that were off by an ULP or two.\n    '
strings = ['0.9999999999999999', '9876543210.123456', '5.43215432154321e+300', '0.901', '0.333']
txt = StringIO('\n'.join(strings))
res = np.loadtxt(txt)
expected = np.array([float(s) for s in strings])
assert_equal(res, expected)
```

## Next Steps


---

*Source: test_loadtxt.py:367 | Complexity: Intermediate | Last updated: 2026-06-02*