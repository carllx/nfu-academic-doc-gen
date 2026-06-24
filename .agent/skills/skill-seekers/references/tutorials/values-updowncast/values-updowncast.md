# How To: Values Updowncast

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test values updowncast

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign test1 = np.array(...)

```python
test1 = np.array([self.ucs_value * self.ulen] * 2, dtype=f'U{self.ulen}')
```

**Verification:**
```python
assert_((ua == ua2).all())
```

### Step 2: Assign test2 = value

```python
test2 = np.repeat(test1, 2)[::2]
```

**Verification:**
```python
assert_(ua[-1] == ua2[-1])
```

### Step 3: Assign longer_type = np.dtype.newbyteorder(...)

```python
longer_type = np.dtype(f'U{self.ulen + 1}').newbyteorder()
```

**Verification:**
```python
assert_equal(ua, ua3)
```

### Step 4: Assign ua2 = ua.astype(...)

```python
ua2 = ua.astype(dtype=longer_type)
```

### Step 5: Call assert_()

```python
assert_((ua == ua2).all())
```

### Step 6: Call assert_()

```python
assert_(ua[-1] == ua2[-1])
```

### Step 7: Assign ua3 = ua2.astype(...)

```python
ua3 = ua2.astype(dtype=ua.dtype)
```

### Step 8: Call assert_equal()

```python
assert_equal(ua, ua3)
```


## Complete Example

```python
# Workflow
test1 = np.array([self.ucs_value * self.ulen] * 2, dtype=f'U{self.ulen}')
test2 = np.repeat(test1, 2)[::2]
for ua in (test1, test2):
    longer_type = np.dtype(f'U{self.ulen + 1}').newbyteorder()
    ua2 = ua.astype(dtype=longer_type)
    assert_((ua == ua2).all())
    assert_(ua[-1] == ua2[-1])
    ua3 = ua2.astype(dtype=ua.dtype)
    assert_equal(ua, ua3)
```

## Next Steps


---

*Source: test_unicode.py:319 | Complexity: Advanced | Last updated: 2026-06-02*