# How To: Set Change Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set change dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.internals`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.internals`
- `pandas.core.internals.blocks`

**Setup Required:**
```python
# Fixtures: mgr
```

## Step-by-Step Guide

### Step 1: Call mgr.insert()

```python
mgr.insert(len(mgr.items), 'baz', np.zeros(N, dtype=bool))
```

**Verification:**
```python
assert mgr.iget(idx).dtype == np.object_
```

### Step 2: Call mgr.iset()

```python
mgr.iset(mgr.items.get_loc('baz'), np.repeat('foo', N))
```

**Verification:**
```python
assert mgr2.iget(idx).dtype == np.object_
```

### Step 3: Assign idx = mgr.items.get_loc(...)

```python
idx = mgr.items.get_loc('baz')
```

**Verification:**
```python
assert mgr2.iget(idx).dtype == np.dtype(int)
```

### Step 4: Assign mgr2 = mgr.consolidate(...)

```python
mgr2 = mgr.consolidate()
```

**Verification:**
```python
assert mgr2.iget(idx).dtype == np.float64
```

### Step 5: Call mgr2.iset()

```python
mgr2.iset(mgr2.items.get_loc('baz'), np.repeat('foo', N))
```

### Step 6: Assign idx = mgr2.items.get_loc(...)

```python
idx = mgr2.items.get_loc('baz')
```

**Verification:**
```python
assert mgr2.iget(idx).dtype == np.object_
```

### Step 7: Call mgr2.insert()

```python
mgr2.insert(len(mgr2.items), 'quux', np.random.default_rng(2).standard_normal(N).astype(int))
```

### Step 8: Assign idx = mgr2.items.get_loc(...)

```python
idx = mgr2.items.get_loc('quux')
```

**Verification:**
```python
assert mgr2.iget(idx).dtype == np.dtype(int)
```

### Step 9: Call mgr2.iset()

```python
mgr2.iset(mgr2.items.get_loc('quux'), np.random.default_rng(2).standard_normal(N))
```

**Verification:**
```python
assert mgr2.iget(idx).dtype == np.float64
```


## Complete Example

```python
# Setup
# Fixtures: mgr

# Workflow
mgr.insert(len(mgr.items), 'baz', np.zeros(N, dtype=bool))
mgr.iset(mgr.items.get_loc('baz'), np.repeat('foo', N))
idx = mgr.items.get_loc('baz')
assert mgr.iget(idx).dtype == np.object_
mgr2 = mgr.consolidate()
mgr2.iset(mgr2.items.get_loc('baz'), np.repeat('foo', N))
idx = mgr2.items.get_loc('baz')
assert mgr2.iget(idx).dtype == np.object_
mgr2.insert(len(mgr2.items), 'quux', np.random.default_rng(2).standard_normal(N).astype(int))
idx = mgr2.items.get_loc('quux')
assert mgr2.iget(idx).dtype == np.dtype(int)
mgr2.iset(mgr2.items.get_loc('quux'), np.random.default_rng(2).standard_normal(N))
assert mgr2.iget(idx).dtype == np.float64
```

## Next Steps


---

*Source: test_internals.py:465 | Complexity: Advanced | Last updated: 2026-06-02*