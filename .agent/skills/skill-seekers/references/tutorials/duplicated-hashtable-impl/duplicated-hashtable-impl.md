# How To: Duplicated Hashtable Impl

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test duplicated hashtable impl

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: keep, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
n, k = (6, 10)
```

### Step 2: Assign levels = value

```python
levels = [np.arange(n), [str(i) for i in range(n)], 1000 + np.arange(n)]
```

### Step 3: Assign codes = value

```python
codes = [np.random.default_rng(2).choice(n, k * n) for _ in levels]
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Call m.setattr()

```python
m.setattr(libindex, '_SIZE_CUTOFF', 50)
```

### Step 6: Assign mi = MultiIndex(...)

```python
mi = MultiIndex(levels=levels, codes=codes)
```

### Step 7: Assign result = mi.duplicated(...)

```python
result = mi.duplicated(keep=keep)
```

### Step 8: Assign expected = hashtable.duplicated(...)

```python
expected = hashtable.duplicated(mi.values, keep=keep)
```


## Complete Example

```python
# Setup
# Fixtures: keep, monkeypatch

# Workflow
n, k = (6, 10)
levels = [np.arange(n), [str(i) for i in range(n)], 1000 + np.arange(n)]
codes = [np.random.default_rng(2).choice(n, k * n) for _ in levels]
with monkeypatch.context() as m:
    m.setattr(libindex, '_SIZE_CUTOFF', 50)
    mi = MultiIndex(levels=levels, codes=codes)
    result = mi.duplicated(keep=keep)
    expected = hashtable.duplicated(mi.values, keep=keep)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_duplicates.py:257 | Complexity: Advanced | Last updated: 2026-06-02*