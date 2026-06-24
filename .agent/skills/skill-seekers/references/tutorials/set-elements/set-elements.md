# How To: Set Elements

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set elements

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
assert_equal(mbase._mask.tolist(), np.array([(0, 0, 0), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1)], dtype=bool))
```

### Step 2: Assign mbase = base.view.copy(...)

```python
mbase = base.view(mrecarray).copy()
```

**Verification:**
```python
assert_equal(mbase.recordmask, [0, 1, 0, 1, 1])
```

### Step 3: Assign unknown = masked

```python
mbase[-2] = masked
```

**Verification:**
```python
assert_equal(mbase.a._data, [5, 5, 3, 4, 5])
```

### Step 4: Call assert_equal()

```python
assert_equal(mbase._mask.tolist(), np.array([(0, 0, 0), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1)], dtype=bool))
```

**Verification:**
```python
assert_equal(mbase.a._mask, [0, 0, 0, 0, 1])
```

### Step 5: Call assert_equal()

```python
assert_equal(mbase.recordmask, [0, 1, 0, 1, 1])
```

**Verification:**
```python
assert_equal(mbase.b._data, [5.0, 5.0, 3.3, 4.4, 5.5])
```

### Step 6: Assign mbase = base.view.copy(...)

```python
mbase = base.view(mrecarray).copy()
```

**Verification:**
```python
assert_equal(mbase.b._mask, [0, 0, 0, 0, 1])
```

### Step 7: Assign unknown = value

```python
mbase[:2] = (5, 5, 5)
```

**Verification:**
```python
assert_equal(mbase.c._data, [b'5', b'5', b'three', b'four', b'five'])
```

### Step 8: Call assert_equal()

```python
assert_equal(mbase.a._data, [5, 5, 3, 4, 5])
```

**Verification:**
```python
assert_equal(mbase.b._mask, [0, 0, 0, 0, 1])
```

### Step 9: Call assert_equal()

```python
assert_equal(mbase.a._mask, [0, 0, 0, 0, 1])
```

**Verification:**
```python
assert_equal(mbase.a._data, [1, 2, 3, 4, 5])
```

### Step 10: Call assert_equal()

```python
assert_equal(mbase.b._data, [5.0, 5.0, 3.3, 4.4, 5.5])
```

**Verification:**
```python
assert_equal(mbase.a._mask, [1, 1, 0, 0, 1])
```

### Step 11: Call assert_equal()

```python
assert_equal(mbase.b._mask, [0, 0, 0, 0, 1])
```

**Verification:**
```python
assert_equal(mbase.b._data, [1.1, 2.2, 3.3, 4.4, 5.5])
```

### Step 12: Call assert_equal()

```python
assert_equal(mbase.c._data, [b'5', b'5', b'three', b'four', b'five'])
```

**Verification:**
```python
assert_equal(mbase.b._mask, [1, 1, 0, 0, 1])
```

### Step 13: Call assert_equal()

```python
assert_equal(mbase.b._mask, [0, 0, 0, 0, 1])
```

**Verification:**
```python
assert_equal(mbase.c._data, [b'one', b'two', b'three', b'four', b'five'])
```

### Step 14: Assign mbase = base.view.copy(...)

```python
mbase = base.view(mrecarray).copy()
```

**Verification:**
```python
assert_equal(mbase.b._mask, [1, 1, 0, 0, 1])
```

### Step 15: Assign unknown = masked

```python
mbase[:2] = masked
```

### Step 16: Call assert_equal()

```python
assert_equal(mbase.a._data, [1, 2, 3, 4, 5])
```

### Step 17: Call assert_equal()

```python
assert_equal(mbase.a._mask, [1, 1, 0, 0, 1])
```

### Step 18: Call assert_equal()

```python
assert_equal(mbase.b._data, [1.1, 2.2, 3.3, 4.4, 5.5])
```

### Step 19: Call assert_equal()

```python
assert_equal(mbase.b._mask, [1, 1, 0, 0, 1])
```

### Step 20: Call assert_equal()

```python
assert_equal(mbase.c._data, [b'one', b'two', b'three', b'four', b'five'])
```

### Step 21: Call assert_equal()

```python
assert_equal(mbase.b._mask, [1, 1, 0, 0, 1])
```


## Complete Example

```python
# Workflow
base = self.base.copy()
mbase = base.view(mrecarray).copy()
mbase[-2] = masked
assert_equal(mbase._mask.tolist(), np.array([(0, 0, 0), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1)], dtype=bool))
assert_equal(mbase.recordmask, [0, 1, 0, 1, 1])
mbase = base.view(mrecarray).copy()
mbase[:2] = (5, 5, 5)
assert_equal(mbase.a._data, [5, 5, 3, 4, 5])
assert_equal(mbase.a._mask, [0, 0, 0, 0, 1])
assert_equal(mbase.b._data, [5.0, 5.0, 3.3, 4.4, 5.5])
assert_equal(mbase.b._mask, [0, 0, 0, 0, 1])
assert_equal(mbase.c._data, [b'5', b'5', b'three', b'four', b'five'])
assert_equal(mbase.b._mask, [0, 0, 0, 0, 1])
mbase = base.view(mrecarray).copy()
mbase[:2] = masked
assert_equal(mbase.a._data, [1, 2, 3, 4, 5])
assert_equal(mbase.a._mask, [1, 1, 0, 0, 1])
assert_equal(mbase.b._data, [1.1, 2.2, 3.3, 4.4, 5.5])
assert_equal(mbase.b._mask, [1, 1, 0, 0, 1])
assert_equal(mbase.c._data, [b'one', b'two', b'three', b'four', b'five'])
assert_equal(mbase.b._mask, [1, 1, 0, 0, 1])
```

## Next Steps


---

*Source: test_mrecords.py:207 | Complexity: Advanced | Last updated: 2026-06-02*