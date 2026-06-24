# How To: Set Fields Mask

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set fields mask

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
assert_equal(mbase.a, [1, 2, 3, 4, 5])
```

### Step 2: Assign mbase = base.view(...)

```python
mbase = base.view(mrecarray)
```

**Verification:**
```python
assert_equal(mbase.a._mask, [0, 1, 0, 1, 1])
```

### Step 3: Assign unknown = masked

```python
mbase['a'][-2] = masked
```

**Verification:**
```python
assert_equal(mbase.a, [0, 1, 2, 3, 4])
```

### Step 4: Call assert_equal()

```python
assert_equal(mbase.a, [1, 2, 3, 4, 5])
```

**Verification:**
```python
assert_equal(mbase.a._mask, [0, 0, 0, 1, 0])
```

### Step 5: Call assert_equal()

```python
assert_equal(mbase.a._mask, [0, 1, 0, 1, 1])
```

### Step 6: Assign mbase = fromarrays(...)

```python
mbase = fromarrays([np.arange(5), np.random.rand(5)], dtype=[('a', int), ('b', float)])
```

### Step 7: Assign unknown = masked

```python
mbase['a'][-2] = masked
```

### Step 8: Call assert_equal()

```python
assert_equal(mbase.a, [0, 1, 2, 3, 4])
```

### Step 9: Call assert_equal()

```python
assert_equal(mbase.a._mask, [0, 0, 0, 1, 0])
```


## Complete Example

```python
# Workflow
base = self.base.copy()
mbase = base.view(mrecarray)
mbase['a'][-2] = masked
assert_equal(mbase.a, [1, 2, 3, 4, 5])
assert_equal(mbase.a._mask, [0, 1, 0, 1, 1])
mbase = fromarrays([np.arange(5), np.random.rand(5)], dtype=[('a', int), ('b', float)])
mbase['a'][-2] = masked
assert_equal(mbase.a, [0, 1, 2, 3, 4])
assert_equal(mbase.a._mask, [0, 0, 0, 1, 0])
```

## Next Steps


---

*Source: test_mrecords.py:145 | Complexity: Advanced | Last updated: 2026-06-02*