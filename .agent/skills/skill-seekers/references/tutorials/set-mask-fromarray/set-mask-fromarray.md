# How To: Set Mask Fromarray

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set mask fromarray

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `numpy.ma`
- `numpy._core.records`
- `numpy.ma`
- `numpy.ma.mrecords`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign base = self.base.copy(...)

```python
base = self.base.copy()
```

**Verification:**
```python
assert_equal(mbase.a.mask, [1, 0, 0, 0, 1])
```

### Step 2: Assign mbase = base.view(...)

```python
mbase = base.view(mrecarray)
```

**Verification:**
```python
assert_equal(mbase.b.mask, [1, 0, 0, 0, 1])
```

### Step 3: Assign mbase.mask = value

```python
mbase.mask = [1, 0, 0, 0, 1]
```

**Verification:**
```python
assert_equal(mbase.c.mask, [1, 0, 0, 0, 1])
```

### Step 4: Call assert_equal()

```python
assert_equal(mbase.a.mask, [1, 0, 0, 0, 1])
```

**Verification:**
```python
assert_equal(mbase.a.mask, [0, 0, 0, 0, 1])
```

### Step 5: Call assert_equal()

```python
assert_equal(mbase.b.mask, [1, 0, 0, 0, 1])
```

**Verification:**
```python
assert_equal(mbase.b.mask, [0, 0, 0, 0, 1])
```

### Step 6: Call assert_equal()

```python
assert_equal(mbase.c.mask, [1, 0, 0, 0, 1])
```

**Verification:**
```python
assert_equal(mbase.c.mask, [0, 0, 0, 0, 1])
```

### Step 7: Assign mbase.mask = value

```python
mbase.mask = [0, 0, 0, 0, 1]
```

### Step 8: Call assert_equal()

```python
assert_equal(mbase.a.mask, [0, 0, 0, 0, 1])
```

### Step 9: Call assert_equal()

```python
assert_equal(mbase.b.mask, [0, 0, 0, 0, 1])
```

### Step 10: Call assert_equal()

```python
assert_equal(mbase.c.mask, [0, 0, 0, 0, 1])
```


## Complete Example

```python
# Workflow
base = self.base.copy()
mbase = base.view(mrecarray)
mbase.mask = [1, 0, 0, 0, 1]
assert_equal(mbase.a.mask, [1, 0, 0, 0, 1])
assert_equal(mbase.b.mask, [1, 0, 0, 0, 1])
assert_equal(mbase.c.mask, [1, 0, 0, 0, 1])
mbase.mask = [0, 0, 0, 0, 1]
assert_equal(mbase.a.mask, [0, 0, 0, 0, 1])
assert_equal(mbase.b.mask, [0, 0, 0, 0, 1])
assert_equal(mbase.c.mask, [0, 0, 0, 0, 1])
```

## Next Steps


---

*Source: test_mrecords.py:176 | Complexity: Advanced | Last updated: 2026-06-02*