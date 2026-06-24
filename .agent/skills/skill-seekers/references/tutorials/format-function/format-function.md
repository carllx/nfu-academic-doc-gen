# How To: Format Function

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test custom format function for each element in array.

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: 'Test custom format function for each element in array.'

```python
'Test custom format function for each element in array.'
```

**Verification:**
```python
assert_(np.array2string(x, formatter={'all': _format_function}) == '[. o O]')
```

### Step 2: Assign x = np.arange(...)

```python
x = np.arange(3)
```

**Verification:**
```python
assert_(np.array2string(x, formatter={'int_kind': _format_function}) == '[. o O]')
```

### Step 3: Assign x_hex = '[0x0 0x1 0x2]'

```python
x_hex = '[0x0 0x1 0x2]'
```

**Verification:**
```python
assert_(np.array2string(x, formatter={'all': lambda x: f'{x:.4f}'}) == '[0.0000 1.0000 2.0000]')
```

### Step 4: Assign x_oct = '[0o0 0o1 0o2]'

```python
x_oct = '[0o0 0o1 0o2]'
```

**Verification:**
```python
assert_equal(np.array2string(x, formatter={'int': hex}), x_hex)
```

### Step 5: Call assert_()

```python
assert_(np.array2string(x, formatter={'all': _format_function}) == '[. o O]')
```

**Verification:**
```python
assert_equal(np.array2string(x, formatter={'int': oct}), x_oct)
```

### Step 6: Call assert_()

```python
assert_(np.array2string(x, formatter={'int_kind': _format_function}) == '[. o O]')
```

**Verification:**
```python
assert_(np.array2string(x, formatter={'float_kind': lambda x: f'{x:.2f}'}) == '[0.00 1.00 2.00]')
```

### Step 7: Call assert_()

```python
assert_(np.array2string(x, formatter={'all': lambda x: f'{x:.4f}'}) == '[0.0000 1.0000 2.0000]')
```

**Verification:**
```python
assert_(np.array2string(x, formatter={'float': lambda x: f'{x:.2f}'}) == '[0.00 1.00 2.00]')
```

### Step 8: Call assert_equal()

```python
assert_equal(np.array2string(x, formatter={'int': hex}), x_hex)
```

**Verification:**
```python
assert_(np.array2string(s, formatter={'numpystr': lambda s: s * 2}) == '[abcabc defdef]')
```

### Step 9: Call assert_equal()

```python
assert_equal(np.array2string(x, formatter={'int': oct}), x_oct)
```

### Step 10: Assign x = np.arange(...)

```python
x = np.arange(3.0)
```

### Step 11: Call assert_()

```python
assert_(np.array2string(x, formatter={'float_kind': lambda x: f'{x:.2f}'}) == '[0.00 1.00 2.00]')
```

### Step 12: Call assert_()

```python
assert_(np.array2string(x, formatter={'float': lambda x: f'{x:.2f}'}) == '[0.00 1.00 2.00]')
```

### Step 13: Assign s = np.array(...)

```python
s = np.array(['abc', 'def'])
```

### Step 14: Call assert_()

```python
assert_(np.array2string(s, formatter={'numpystr': lambda s: s * 2}) == '[abcabc defdef]')
```


## Complete Example

```python
# Workflow
'Test custom format function for each element in array.'

def _format_function(x):
    if np.abs(x) < 1:
        return '.'
    elif np.abs(x) < 2:
        return 'o'
    else:
        return 'O'
x = np.arange(3)
x_hex = '[0x0 0x1 0x2]'
x_oct = '[0o0 0o1 0o2]'
assert_(np.array2string(x, formatter={'all': _format_function}) == '[. o O]')
assert_(np.array2string(x, formatter={'int_kind': _format_function}) == '[. o O]')
assert_(np.array2string(x, formatter={'all': lambda x: f'{x:.4f}'}) == '[0.0000 1.0000 2.0000]')
assert_equal(np.array2string(x, formatter={'int': hex}), x_hex)
assert_equal(np.array2string(x, formatter={'int': oct}), x_oct)
x = np.arange(3.0)
assert_(np.array2string(x, formatter={'float_kind': lambda x: f'{x:.2f}'}) == '[0.00 1.00 2.00]')
assert_(np.array2string(x, formatter={'float': lambda x: f'{x:.2f}'}) == '[0.00 1.00 2.00]')
s = np.array(['abc', 'def'])
assert_(np.array2string(s, formatter={'numpystr': lambda s: s * 2}) == '[abcabc defdef]')
```

## Next Steps


---

*Source: test_arrayprint.py:235 | Complexity: Advanced | Last updated: 2026-06-02*