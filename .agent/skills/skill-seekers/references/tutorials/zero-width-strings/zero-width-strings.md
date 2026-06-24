# How To: Zero Width Strings

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zero width strings

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

### Step 1: Assign cols = value

```python
cols = [['test'] * 3, [''] * 3]
```

**Verification:**
```python
assert_equal(rec['f0'], ['test', 'test', 'test'])
```

### Step 2: Assign rec = np.rec.fromarrays(...)

```python
rec = np.rec.fromarrays(cols)
```

**Verification:**
```python
assert_equal(rec['f1'], ['', '', ''])
```

### Step 3: Call assert_equal()

```python
assert_equal(rec['f0'], ['test', 'test', 'test'])
```

**Verification:**
```python
assert_equal(rec.itemsize, 4)
```

### Step 4: Call assert_equal()

```python
assert_equal(rec['f1'], ['', '', ''])
```

**Verification:**
```python
assert_equal(rec['f0'], [b'test', b'test', b'test'])
```

### Step 5: Assign dt = np.dtype(...)

```python
dt = np.dtype([('f0', '|S4'), ('f1', '|S')])
```

**Verification:**
```python
assert_equal(rec['f1'], [b'', b'', b''])
```

### Step 6: Assign rec = np.rec.fromarrays(...)

```python
rec = np.rec.fromarrays(cols, dtype=dt)
```

### Step 7: Call assert_equal()

```python
assert_equal(rec.itemsize, 4)
```

### Step 8: Call assert_equal()

```python
assert_equal(rec['f0'], [b'test', b'test', b'test'])
```

### Step 9: Call assert_equal()

```python
assert_equal(rec['f1'], [b'', b'', b''])
```


## Complete Example

```python
# Workflow
cols = [['test'] * 3, [''] * 3]
rec = np.rec.fromarrays(cols)
assert_equal(rec['f0'], ['test', 'test', 'test'])
assert_equal(rec['f1'], ['', '', ''])
dt = np.dtype([('f0', '|S4'), ('f1', '|S')])
rec = np.rec.fromarrays(cols, dtype=dt)
assert_equal(rec.itemsize, 4)
assert_equal(rec['f0'], [b'test', b'test', b'test'])
assert_equal(rec['f1'], [b'', b'', b''])
```

## Next Steps


---

*Source: test_records.py:330 | Complexity: Advanced | Last updated: 2026-06-02*