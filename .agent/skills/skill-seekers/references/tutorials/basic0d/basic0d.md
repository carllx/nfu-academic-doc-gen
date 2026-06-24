# How To: Basic0D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic0d

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `itertools`
- `operator`
- `pickle`
- `sys`
- `textwrap`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma.core`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`
- `numpy.testing._private.utils`
- `datetime`
- `copy`
- `io`
- `copy`
- `copy`


## Step-by-Step Guide

### Step 1: Assign x = masked_array(...)

```python
x = masked_array(0)
```

**Verification:**
```python
assert_equal(str(x), '0')
```

### Step 2: Call assert_equal()

```python
assert_equal(str(x), '0')
```

**Verification:**
```python
assert_equal(str(x), str(masked_print_option))
```

### Step 3: Assign x = masked_array(...)

```python
x = masked_array(0, mask=True)
```

**Verification:**
```python
assert_equal(str(x), '0')
```

### Step 4: Call assert_equal()

```python
assert_equal(str(x), str(masked_print_option))
```

**Verification:**
```python
assert_(x.filled().dtype is x._data.dtype)
```

### Step 5: Assign x = masked_array(...)

```python
x = masked_array(0, mask=False)
```

### Step 6: Call assert_equal()

```python
assert_equal(str(x), '0')
```

### Step 7: Assign x = array(...)

```python
x = array(0, mask=1)
```

### Step 8: Call assert_()

```python
assert_(x.filled().dtype is x._data.dtype)
```


## Complete Example

```python
# Workflow
x = masked_array(0)
assert_equal(str(x), '0')
x = masked_array(0, mask=True)
assert_equal(str(x), str(masked_print_option))
x = masked_array(0, mask=False)
assert_equal(str(x), '0')
x = array(0, mask=1)
assert_(x.filled().dtype is x._data.dtype)
```

## Next Steps


---

*Source: test_core.py:186 | Complexity: Advanced | Last updated: 2026-06-02*