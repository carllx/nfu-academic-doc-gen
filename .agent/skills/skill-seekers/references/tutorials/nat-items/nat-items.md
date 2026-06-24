# How To: Nat Items

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nat items

## Prerequisites

**Required Modules:**
- `itertools`
- `os`
- `re`
- `sys`
- `warnings`
- `weakref`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `datetime`


## Step-by-Step Guide

### Step 1: Assign nadt_no_unit = np.datetime64(...)

```python
nadt_no_unit = np.datetime64('NaT')
```

### Step 2: Assign nadt_s = np.datetime64(...)

```python
nadt_s = np.datetime64('NaT', 's')
```

### Step 3: Assign nadt_d = np.datetime64(...)

```python
nadt_d = np.datetime64('NaT', 'ns')
```

### Step 4: Assign natd_no_unit = np.timedelta64(...)

```python
natd_no_unit = np.timedelta64('NaT')
```

### Step 5: Assign natd_s = np.timedelta64(...)

```python
natd_s = np.timedelta64('NaT', 's')
```

### Step 6: Assign natd_d = np.timedelta64(...)

```python
natd_d = np.timedelta64('NaT', 'ns')
```

### Step 7: Assign dts = value

```python
dts = [nadt_no_unit, nadt_s, nadt_d]
```

### Step 8: Assign tds = value

```python
tds = [natd_no_unit, natd_s, natd_d]
```

### Step 9: Call self._assert_func()

```python
self._assert_func(a, b)
```

### Step 10: Call self._assert_func()

```python
self._assert_func([a], [b])
```

### Step 11: Call self._test_not_equal()

```python
self._test_not_equal([a], b)
```

### Step 12: Call self._assert_func()

```python
self._assert_func(a, b)
```

### Step 13: Call self._assert_func()

```python
self._assert_func([a], [b])
```

### Step 14: Call self._test_not_equal()

```python
self._test_not_equal([a], b)
```

### Step 15: Call self._test_not_equal()

```python
self._test_not_equal(a, b)
```

### Step 16: Call self._test_not_equal()

```python
self._test_not_equal(a, [b])
```

### Step 17: Call self._test_not_equal()

```python
self._test_not_equal([a], [b])
```

### Step 18: Call self._test_not_equal()

```python
self._test_not_equal([a], np.datetime64('2017-01-01', 's'))
```

### Step 19: Call self._test_not_equal()

```python
self._test_not_equal([b], np.datetime64('2017-01-01', 's'))
```

### Step 20: Call self._test_not_equal()

```python
self._test_not_equal([a], np.timedelta64(123, 's'))
```

### Step 21: Call self._test_not_equal()

```python
self._test_not_equal([b], np.timedelta64(123, 's'))
```


## Complete Example

```python
# Workflow
nadt_no_unit = np.datetime64('NaT')
nadt_s = np.datetime64('NaT', 's')
nadt_d = np.datetime64('NaT', 'ns')
natd_no_unit = np.timedelta64('NaT')
natd_s = np.timedelta64('NaT', 's')
natd_d = np.timedelta64('NaT', 'ns')
dts = [nadt_no_unit, nadt_s, nadt_d]
tds = [natd_no_unit, natd_s, natd_d]
for a, b in itertools.product(dts, dts):
    self._assert_func(a, b)
    self._assert_func([a], [b])
    self._test_not_equal([a], b)
for a, b in itertools.product(tds, tds):
    self._assert_func(a, b)
    self._assert_func([a], [b])
    self._test_not_equal([a], b)
for a, b in itertools.product(tds, dts):
    self._test_not_equal(a, b)
    self._test_not_equal(a, [b])
    self._test_not_equal([a], [b])
    self._test_not_equal([a], np.datetime64('2017-01-01', 's'))
    self._test_not_equal([b], np.datetime64('2017-01-01', 's'))
    self._test_not_equal([a], np.timedelta64(123, 's'))
    self._test_not_equal([b], np.timedelta64(123, 's'))
```

## Next Steps


---

*Source: test_utils.py:429 | Complexity: Advanced | Last updated: 2026-06-02*