# How To: Group Var Large Inputs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test group var large inputs

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.groupby`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign prng = np.random.default_rng(...)

```python
prng = np.random.default_rng(2)
```

**Verification:**
```python
assert counts[0] == 10 ** 6
```

### Step 2: Assign out = np.array(...)

```python
out = np.array([[np.nan]], dtype=self.dtype)
```

### Step 3: Assign counts = np.array(...)

```python
counts = np.array([0], dtype='int64')
```

### Step 4: Assign values = unknown.astype(...)

```python
values = (prng.random(10 ** 6) + 10 ** 12).astype(self.dtype)
```

### Step 5: Assign values.shape = value

```python
values.shape = (10 ** 6, 1)
```

### Step 6: Assign labels = np.zeros(...)

```python
labels = np.zeros(10 ** 6, dtype='intp')
```

### Step 7: Call self.algo()

```python
self.algo(out, counts, values, labels)
```

**Verification:**
```python
assert counts[0] == 10 ** 6
```

### Step 8: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(out[0, 0], 1.0 / 12, rtol=0.0005)
```


## Complete Example

```python
# Workflow
prng = np.random.default_rng(2)
out = np.array([[np.nan]], dtype=self.dtype)
counts = np.array([0], dtype='int64')
values = (prng.random(10 ** 6) + 10 ** 12).astype(self.dtype)
values.shape = (10 ** 6, 1)
labels = np.zeros(10 ** 6, dtype='intp')
self.algo(out, counts, values, labels)
assert counts[0] == 10 ** 6
tm.assert_almost_equal(out[0, 0], 1.0 / 12, rtol=0.0005)
```

## Next Steps


---

*Source: test_libgroupby.py:111 | Complexity: Advanced | Last updated: 2026-06-02*