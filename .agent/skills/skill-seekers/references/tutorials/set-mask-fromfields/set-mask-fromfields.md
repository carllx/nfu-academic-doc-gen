# How To: Set Mask Fromfields

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set mask fromfields

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

### Step 1: Assign mbase = self.base.copy.view(...)

```python
mbase = self.base.copy().view(mrecarray)
```

**Verification:**
```python
assert_equal(mbase.a.mask, [0, 0, 1, 1, 0])
```

### Step 2: Assign nmask = np.array(...)

```python
nmask = np.array([(0, 1, 0), (0, 1, 0), (1, 0, 1), (1, 0, 1), (0, 0, 0)], dtype=[('a', bool), ('b', bool), ('c', bool)])
```

**Verification:**
```python
assert_equal(mbase.b.mask, [1, 1, 0, 0, 0])
```

### Step 3: Assign mbase.mask = nmask

```python
mbase.mask = nmask
```

**Verification:**
```python
assert_equal(mbase.c.mask, [0, 0, 1, 1, 0])
```

### Step 4: Call assert_equal()

```python
assert_equal(mbase.a.mask, [0, 0, 1, 1, 0])
```

**Verification:**
```python
assert_equal(mbase.a.mask, [0, 0, 1, 1, 0])
```

### Step 5: Call assert_equal()

```python
assert_equal(mbase.b.mask, [1, 1, 0, 0, 0])
```

**Verification:**
```python
assert_equal(mbase.b.mask, [1, 1, 0, 0, 0])
```

### Step 6: Call assert_equal()

```python
assert_equal(mbase.c.mask, [0, 0, 1, 1, 0])
```

**Verification:**
```python
assert_equal(mbase.c.mask, [0, 0, 1, 1, 0])
```

### Step 7: Assign mbase.mask = False

```python
mbase.mask = False
```

### Step 8: Assign mbase.fieldmask = nmask

```python
mbase.fieldmask = nmask
```

### Step 9: Call assert_equal()

```python
assert_equal(mbase.a.mask, [0, 0, 1, 1, 0])
```

### Step 10: Call assert_equal()

```python
assert_equal(mbase.b.mask, [1, 1, 0, 0, 0])
```

### Step 11: Call assert_equal()

```python
assert_equal(mbase.c.mask, [0, 0, 1, 1, 0])
```


## Complete Example

```python
# Workflow
mbase = self.base.copy().view(mrecarray)
nmask = np.array([(0, 1, 0), (0, 1, 0), (1, 0, 1), (1, 0, 1), (0, 0, 0)], dtype=[('a', bool), ('b', bool), ('c', bool)])
mbase.mask = nmask
assert_equal(mbase.a.mask, [0, 0, 1, 1, 0])
assert_equal(mbase.b.mask, [1, 1, 0, 0, 0])
assert_equal(mbase.c.mask, [0, 0, 1, 1, 0])
mbase.mask = False
mbase.fieldmask = nmask
assert_equal(mbase.a.mask, [0, 0, 1, 1, 0])
assert_equal(mbase.b.mask, [1, 1, 0, 0, 0])
assert_equal(mbase.c.mask, [0, 0, 1, 1, 0])
```

## Next Steps


---

*Source: test_mrecords.py:190 | Complexity: Advanced | Last updated: 2026-06-02*