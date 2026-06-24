# How To: Object Subclass

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test object subclass

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

### Step 1: Assign x = sub(...)

```python
x = sub([None, None])
```

**Verification:**
```python
assert_equal(repr(x), 'sub([None, None], dtype=object)')
```

### Step 2: Call assert_equal()

```python
assert_equal(repr(x), 'sub([None, None], dtype=object)')
```

**Verification:**
```python
assert_equal(str(x), '[None None]')
```

### Step 3: Call assert_equal()

```python
assert_equal(str(x), '[None None]')
```

**Verification:**
```python
assert_equal(repr(x), 'sub([None, sub([None, None], dtype=object)], dtype=object)')
```

### Step 4: Assign x = sub(...)

```python
x = sub([None, sub([None, None])])
```

**Verification:**
```python
assert_equal(str(x), '[None sub([None, None], dtype=object)]')
```

### Step 5: Call assert_equal()

```python
assert_equal(repr(x), 'sub([None, sub([None, None], dtype=object)], dtype=object)')
```

### Step 6: Call assert_equal()

```python
assert_equal(str(x), '[None sub([None, None], dtype=object)]')
```

### Step 7: Assign obj = np.asarray.view(...)

```python
obj = np.asarray(inp).view(cls)
```

### Step 8: Assign ret = super.__getitem__(...)

```python
ret = super().__getitem__(ind)
```


## Complete Example

```python
# Workflow
class sub(np.ndarray):

    def __new__(cls, inp):
        obj = np.asarray(inp).view(cls)
        return obj

    def __getitem__(self, ind):
        ret = super().__getitem__(ind)
        return sub(ret)
x = sub([None, None])
assert_equal(repr(x), 'sub([None, None], dtype=object)')
assert_equal(str(x), '[None None]')
x = sub([None, sub([None, None])])
assert_equal(repr(x), 'sub([None, sub([None, None], dtype=object)], dtype=object)')
assert_equal(str(x), '[None sub([None, None], dtype=object)]')
```

## Next Steps


---

*Source: test_arrayprint.py:49 | Complexity: Advanced | Last updated: 2026-06-02*