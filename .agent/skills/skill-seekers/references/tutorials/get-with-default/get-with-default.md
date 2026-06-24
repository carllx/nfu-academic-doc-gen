# How To: Get With Default

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get with default

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign d0 = value

```python
d0 = ['a', 'b', 'c', 'd']
```

**Verification:**
```python
assert s.get(i) == d
```

### Step 2: Assign d1 = np.arange(...)

```python
d1 = np.arange(4, dtype='int64')
```

**Verification:**
```python
assert s.get(i, d) == d
```

### Step 3: Assign s = Series(...)

```python
s = Series(data, index=index)
```

**Verification:**
```python
assert s.get(i, 'z') == d
```

### Step 4: Assign msg = 'Series.__getitem__ treating keys as positions is deprecated'

```python
msg = 'Series.__getitem__ treating keys as positions is deprecated'
```

**Verification:**
```python
assert s.get('e', 'z') == 'z'
```

### Step 5: Assign warn = None

```python
warn = None
```

**Verification:**
```python
assert s.get('e', 'e') == 'e'
```

### Step 6: Assign warn = FutureWarning

```python
warn = FutureWarning
```

**Verification:**
```python
assert s.get(10, 'z') == 'z'
```


## Complete Example

```python
# Workflow
d0 = ['a', 'b', 'c', 'd']
d1 = np.arange(4, dtype='int64')
for data, index in ((d0, d1), (d1, d0)):
    s = Series(data, index=index)
    for i, d in zip(index, data):
        assert s.get(i) == d
        assert s.get(i, d) == d
        assert s.get(i, 'z') == d
        assert s.get('e', 'z') == 'z'
        assert s.get('e', 'e') == 'e'
        msg = 'Series.__getitem__ treating keys as positions is deprecated'
        warn = None
        if index is d0:
            warn = FutureWarning
        with tm.assert_produces_warning(warn, match=msg):
            assert s.get(10, 'z') == 'z'
            assert s.get(10, 10) == 10
```

## Next Steps


---

*Source: test_get.py:145 | Complexity: Intermediate | Last updated: 2026-06-02*