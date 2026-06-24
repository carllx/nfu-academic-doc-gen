# How To: Inplace Mutation Resets Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test inplace mutation resets values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign levels = value

```python
levels = [['a', 'b', 'c'], [4]]
```

**Verification:**
```python
assert '_values' not in mi1._cache
```

### Step 2: Assign levels2 = value

```python
levels2 = [[1, 2, 3], ['a']]
```

**Verification:**
```python
assert '_values' not in mi2._cache
```

### Step 3: Assign codes = value

```python
codes = [[0, 1, 0, 2, 2, 0], [0, 0, 0, 0, 0, 0]]
```

**Verification:**
```python
assert mi1._values is mi1._cache['_values']
```

### Step 4: Assign mi1 = MultiIndex(...)

```python
mi1 = MultiIndex(levels=levels, codes=codes)
```

**Verification:**
```python
assert mi1.values is mi1._cache['_values']
```

### Step 5: Assign mi2 = MultiIndex(...)

```python
mi2 = MultiIndex(levels=levels2, codes=codes)
```

**Verification:**
```python
assert isinstance(mi1._cache['_values'], np.ndarray)
```

### Step 6: Assign vals = mi1.values.copy(...)

```python
vals = mi1.values.copy()
```

**Verification:**
```python
assert exp_values.shape == (6,)
```

### Step 7: Assign vals2 = mi2.values.copy(...)

```python
vals2 = mi2.values.copy()
```

**Verification:**
```python
assert '_values' not in new_mi._cache
```

### Step 8: Assign new_vals = value

```python
new_vals = mi1.set_levels(levels2).values
```

**Verification:**
```python
assert '_values' in new_mi._cache
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(vals2, new_vals)
```

### Step 10: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(mi1._cache['_values'], vals)
```

### Step 11: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(mi1.values, vals)
```

### Step 12: Assign codes2 = value

```python
codes2 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
```

### Step 13: Assign exp_values = np.empty(...)

```python
exp_values = np.empty((6,), dtype=object)
```

### Step 14: Assign unknown = value

```python
exp_values[:] = [(1, 'a')] * 6
```

**Verification:**
```python
assert exp_values.shape == (6,)
```

### Step 15: Assign new_mi = mi2.set_codes(...)

```python
new_mi = mi2.set_codes(codes2)
```

**Verification:**
```python
assert '_values' not in new_mi._cache
```

### Step 16: Assign new_values = value

```python
new_values = new_mi.values
```

**Verification:**
```python
assert '_values' in new_mi._cache
```

### Step 17: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(mi2._cache['_values'], vals2)
```

### Step 18: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(exp_values, new_values)
```


## Complete Example

```python
# Workflow
levels = [['a', 'b', 'c'], [4]]
levels2 = [[1, 2, 3], ['a']]
codes = [[0, 1, 0, 2, 2, 0], [0, 0, 0, 0, 0, 0]]
mi1 = MultiIndex(levels=levels, codes=codes)
mi2 = MultiIndex(levels=levels2, codes=codes)
assert '_values' not in mi1._cache
assert '_values' not in mi2._cache
vals = mi1.values.copy()
vals2 = mi2.values.copy()
assert mi1._values is mi1._cache['_values']
assert mi1.values is mi1._cache['_values']
assert isinstance(mi1._cache['_values'], np.ndarray)
new_vals = mi1.set_levels(levels2).values
tm.assert_almost_equal(vals2, new_vals)
tm.assert_almost_equal(mi1._cache['_values'], vals)
tm.assert_almost_equal(mi1.values, vals)
codes2 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
exp_values = np.empty((6,), dtype=object)
exp_values[:] = [(1, 'a')] * 6
assert exp_values.shape == (6,)
new_mi = mi2.set_codes(codes2)
assert '_values' not in new_mi._cache
new_values = new_mi.values
assert '_values' in new_mi._cache
tm.assert_almost_equal(mi2._cache['_values'], vals2)
tm.assert_almost_equal(exp_values, new_values)
```

## Next Steps


---

*Source: test_compat.py:39 | Complexity: Advanced | Last updated: 2026-06-02*