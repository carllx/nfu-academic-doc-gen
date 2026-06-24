# How To: Filled

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test filled

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

### Step 1: Assign _a = ma.array(...)

```python
_a = ma.array([1, 2, 3], mask=[0, 0, 1], dtype=int)
```

**Verification:**
```python
assert_equal(mrecfilled['a'], np.array((1, 2, 99999), dtype=int))
```

### Step 2: Assign _b = ma.array(...)

```python
_b = ma.array([1.1, 2.2, 3.3], mask=[0, 0, 1], dtype=float)
```

**Verification:**
```python
assert_equal(mrecfilled['b'], np.array((1.1, 2.2, 99999.0), dtype=float))
```

### Step 3: Assign _c = ma.array(...)

```python
_c = ma.array(['one', 'two', 'three'], mask=[0, 0, 1], dtype='|S8')
```

**Verification:**
```python
assert_equal(mrecfilled['c'], np.array(('one', 'two', 'N/A'), dtype='|S8'))
```

### Step 4: Assign ddtype = value

```python
ddtype = [('a', int), ('b', float), ('c', '|S8')]
```

### Step 5: Assign mrec = fromarrays(...)

```python
mrec = fromarrays([_a, _b, _c], dtype=ddtype, fill_value=(99999, 99999.0, 'N/A'))
```

### Step 6: Assign mrecfilled = mrec.filled(...)

```python
mrecfilled = mrec.filled()
```

### Step 7: Call assert_equal()

```python
assert_equal(mrecfilled['a'], np.array((1, 2, 99999), dtype=int))
```

### Step 8: Call assert_equal()

```python
assert_equal(mrecfilled['b'], np.array((1.1, 2.2, 99999.0), dtype=float))
```

### Step 9: Call assert_equal()

```python
assert_equal(mrecfilled['c'], np.array(('one', 'two', 'N/A'), dtype='|S8'))
```


## Complete Example

```python
# Workflow
_a = ma.array([1, 2, 3], mask=[0, 0, 1], dtype=int)
_b = ma.array([1.1, 2.2, 3.3], mask=[0, 0, 1], dtype=float)
_c = ma.array(['one', 'two', 'three'], mask=[0, 0, 1], dtype='|S8')
ddtype = [('a', int), ('b', float), ('c', '|S8')]
mrec = fromarrays([_a, _b, _c], dtype=ddtype, fill_value=(99999, 99999.0, 'N/A'))
mrecfilled = mrec.filled()
assert_equal(mrecfilled['a'], np.array((1, 2, 99999), dtype=int))
assert_equal(mrecfilled['b'], np.array((1.1, 2.2, 99999.0), dtype=float))
assert_equal(mrecfilled['c'], np.array(('one', 'two', 'N/A'), dtype='|S8'))
```

## Next Steps


---

*Source: test_mrecords.py:297 | Complexity: Advanced | Last updated: 2026-06-02*