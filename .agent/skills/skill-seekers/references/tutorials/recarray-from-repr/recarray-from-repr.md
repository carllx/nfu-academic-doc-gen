# How To: Recarray From Repr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test recarray from repr

## Prerequisites

**Required Modules:**
- `collections.abc`
- `pickle`
- `textwrap`
- `io`
- `os`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([(1, 'ABC'), (2, 'DEF')], dtype=[('foo', int), ('bar', 'S4')])
```

**Verification:**
```python
assert_equal(type(recordarr_r), np.recarray)
```

### Step 2: Assign recordarr = np.rec.array(...)

```python
recordarr = np.rec.array(a)
```

**Verification:**
```python
assert_equal(recordarr_r.dtype.type, np.record)
```

### Step 3: Assign recarr = a.view(...)

```python
recarr = a.view(np.recarray)
```

**Verification:**
```python
assert_equal(recordarr, recordarr_r)
```

### Step 4: Assign recordview = a.view(...)

```python
recordview = a.view(np.dtype((np.record, a.dtype)))
```

**Verification:**
```python
assert_equal(type(recarr_r), np.recarray)
```

### Step 5: Assign recordarr_r = eval(...)

```python
recordarr_r = eval('np.' + repr(recordarr), {'np': np})
```

**Verification:**
```python
assert_equal(recarr_r.dtype.type, np.record)
```

### Step 6: Assign recarr_r = eval(...)

```python
recarr_r = eval('np.' + repr(recarr), {'np': np})
```

**Verification:**
```python
assert_equal(recarr, recarr_r)
```

### Step 7: Assign recordview_r = eval(...)

```python
recordview_r = eval('np.' + repr(recordview), {'np': np, 'numpy': np})
```

**Verification:**
```python
assert_equal(type(recordview_r), np.ndarray)
```

### Step 8: Call assert_equal()

```python
assert_equal(type(recordarr_r), np.recarray)
```

**Verification:**
```python
assert_equal(recordview.dtype.type, np.record)
```

### Step 9: Call assert_equal()

```python
assert_equal(recordarr_r.dtype.type, np.record)
```

**Verification:**
```python
assert_equal(recordview, recordview_r)
```

### Step 10: Call assert_equal()

```python
assert_equal(recordarr, recordarr_r)
```

### Step 11: Call assert_equal()

```python
assert_equal(type(recarr_r), np.recarray)
```

### Step 12: Call assert_equal()

```python
assert_equal(recarr_r.dtype.type, np.record)
```

### Step 13: Call assert_equal()

```python
assert_equal(recarr, recarr_r)
```

### Step 14: Call assert_equal()

```python
assert_equal(type(recordview_r), np.ndarray)
```

### Step 15: Call assert_equal()

```python
assert_equal(recordview.dtype.type, np.record)
```

### Step 16: Call assert_equal()

```python
assert_equal(recordview, recordview_r)
```


## Complete Example

```python
# Workflow
a = np.array([(1, 'ABC'), (2, 'DEF')], dtype=[('foo', int), ('bar', 'S4')])
recordarr = np.rec.array(a)
recarr = a.view(np.recarray)
recordview = a.view(np.dtype((np.record, a.dtype)))
recordarr_r = eval('np.' + repr(recordarr), {'np': np})
recarr_r = eval('np.' + repr(recarr), {'np': np})
recordview_r = eval('np.' + repr(recordview), {'np': np, 'numpy': np})
assert_equal(type(recordarr_r), np.recarray)
assert_equal(recordarr_r.dtype.type, np.record)
assert_equal(recordarr, recordarr_r)
assert_equal(type(recarr_r), np.recarray)
assert_equal(recarr_r.dtype.type, np.record)
assert_equal(recarr, recarr_r)
assert_equal(type(recordview_r), np.ndarray)
assert_equal(recordview.dtype.type, np.record)
assert_equal(recordview, recordview_r)
```

## Next Steps


---

*Source: test_records.py:163 | Complexity: Advanced | Last updated: 2026-06-02*