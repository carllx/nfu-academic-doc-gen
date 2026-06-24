# How To: Fast Multiget Timedelta Resos

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fast multiget timedelta resos

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign td = Timedelta(...)

```python
td = Timedelta(days=1)
```

**Verification:**
```python
assert hash(td) == hash(td.as_unit('ms'))
```

### Step 2: Assign mapping1 = value

```python
mapping1 = {td: 1}
```

**Verification:**
```python
assert hash(td) == hash(td.as_unit('us'))
```

### Step 3: Assign mapping2 = value

```python
mapping2 = {td.as_unit('s'): 1}
```

### Step 4: Assign oindex = Index._values.astype(...)

```python
oindex = Index([td * n for n in range(3)])._values.astype(object)
```

### Step 5: Assign expected = lib.fast_multiget(...)

```python
expected = lib.fast_multiget(mapping1, oindex)
```

### Step 6: Assign result = lib.fast_multiget(...)

```python
result = lib.fast_multiget(mapping2, oindex)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign td = Timedelta(...)

```python
td = Timedelta(np.timedelta64(146000, 'D'))
```

**Verification:**
```python
assert hash(td) == hash(td.as_unit('ms'))
```

### Step 9: Assign mapping1 = value

```python
mapping1 = {td: 1}
```

### Step 10: Assign mapping2 = value

```python
mapping2 = {td.as_unit('ms'): 1}
```

### Step 11: Assign oindex = Index._values.astype(...)

```python
oindex = Index([td * n for n in range(3)])._values.astype(object)
```

### Step 12: Assign expected = lib.fast_multiget(...)

```python
expected = lib.fast_multiget(mapping1, oindex)
```

### Step 13: Assign result = lib.fast_multiget(...)

```python
result = lib.fast_multiget(mapping2, oindex)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
td = Timedelta(days=1)
mapping1 = {td: 1}
mapping2 = {td.as_unit('s'): 1}
oindex = Index([td * n for n in range(3)])._values.astype(object)
expected = lib.fast_multiget(mapping1, oindex)
result = lib.fast_multiget(mapping2, oindex)
tm.assert_numpy_array_equal(result, expected)
td = Timedelta(np.timedelta64(146000, 'D'))
assert hash(td) == hash(td.as_unit('ms'))
assert hash(td) == hash(td.as_unit('us'))
mapping1 = {td: 1}
mapping2 = {td.as_unit('ms'): 1}
oindex = Index([td * n for n in range(3)])._values.astype(object)
expected = lib.fast_multiget(mapping1, oindex)
result = lib.fast_multiget(mapping2, oindex)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_lib.py:48 | Complexity: Advanced | Last updated: 2026-06-02*