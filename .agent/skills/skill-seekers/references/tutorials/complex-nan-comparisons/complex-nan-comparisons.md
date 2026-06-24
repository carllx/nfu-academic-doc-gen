# How To: Complex Nan Comparisons

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complex nan comparisons

## Prerequisites

**Required Modules:**
- `fnmatch`
- `inspect`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `collections`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`
- `platform`
- `decimal`
- `cmath`


## Step-by-Step Guide

### Step 1: Assign nans = value

```python
nans = [complex(np.nan, 0), complex(0, np.nan), complex(np.nan, np.nan)]
```

**Verification:**
```python
assert_equal(x < y, False, err_msg=f'{x!r} < {y!r}')
```

### Step 2: Assign fins = value

```python
fins = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1), complex(1, 1), complex(-1, -1), complex(0, 0)]
```

**Verification:**
```python
assert_equal(x > y, False, err_msg=f'{x!r} > {y!r}')
```

### Step 3: Assign x = np.array(...)

```python
x = np.array([x])
```

**Verification:**
```python
assert_equal(x <= y, False, err_msg=f'{x!r} <= {y!r}')
```

### Step 4: Assign y = np.array(...)

```python
y = np.array([y])
```

**Verification:**
```python
assert_equal(x >= y, False, err_msg=f'{x!r} >= {y!r}')
```

### Step 5: Call assert_equal()

```python
assert_equal(x < y, False, err_msg=f'{x!r} < {y!r}')
```

**Verification:**
```python
assert_equal(x == y, False, err_msg=f'{x!r} == {y!r}')
```

### Step 6: Call assert_equal()

```python
assert_equal(x > y, False, err_msg=f'{x!r} > {y!r}')
```

### Step 7: Call assert_equal()

```python
assert_equal(x <= y, False, err_msg=f'{x!r} <= {y!r}')
```

### Step 8: Call assert_equal()

```python
assert_equal(x >= y, False, err_msg=f'{x!r} >= {y!r}')
```

### Step 9: Call assert_equal()

```python
assert_equal(x == y, False, err_msg=f'{x!r} == {y!r}')
```


## Complete Example

```python
# Workflow
nans = [complex(np.nan, 0), complex(0, np.nan), complex(np.nan, np.nan)]
fins = [complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1), complex(1, 1), complex(-1, -1), complex(0, 0)]
with np.errstate(invalid='ignore'):
    for x in nans + fins:
        x = np.array([x])
        for y in nans + fins:
            y = np.array([y])
            if np.isfinite(x) and np.isfinite(y):
                continue
            assert_equal(x < y, False, err_msg=f'{x!r} < {y!r}')
            assert_equal(x > y, False, err_msg=f'{x!r} > {y!r}')
            assert_equal(x <= y, False, err_msg=f'{x!r} <= {y!r}')
            assert_equal(x >= y, False, err_msg=f'{x!r} >= {y!r}')
            assert_equal(x == y, False, err_msg=f'{x!r} == {y!r}')
```

## Next Steps


---

*Source: test_umath.py:4751 | Complexity: Advanced | Last updated: 2026-06-02*