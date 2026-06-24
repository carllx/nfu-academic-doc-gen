# How To: Scalar Float

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test scalar float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(np.arange(5.0))
```

**Verification:**
```python
assert 3.0 in s
```

### Step 2: Assign s = gen_obj(...)

```python
s = gen_obj(frame_or_series, index)
```

### Step 3: Assign indexer = value

```python
indexer = index[3]
```

**Verification:**
```python
assert 3.0 in s
```

### Step 4: Assign expected = value

```python
expected = s.iloc[3]
```

### Step 5: Assign s2 = s.copy(...)

```python
s2 = s.copy()
```

### Step 6: Assign unknown = expected

```python
s2.iloc[3] = expected
```

### Step 7: Assign result = value

```python
result = s2.iloc[3]
```

### Step 8: Call self.check()

```python
self.check(result, s, 3, False)
```

### Step 9: Assign getitem = value

```python
getitem = idxr is not tm.loc
```

### Step 10: Assign result = value

```python
result = idxr(s)[indexer]
```

### Step 11: Call self.check()

```python
self.check(result, s, 3, getitem)
```

### Step 12: Assign s2 = s.copy(...)

```python
s2 = s.copy()
```

### Step 13: Assign result = value

```python
result = idxr(s2)[indexer]
```

### Step 14: Call self.check()

```python
self.check(result, s, 3, getitem)
```

### Step 15: idxr(s)[3.5]

```python
idxr(s)[3.5]
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
index = Index(np.arange(5.0))
s = gen_obj(frame_or_series, index)
indexer = index[3]
for idxr in [tm.loc, tm.setitem]:
    getitem = idxr is not tm.loc
    result = idxr(s)[indexer]
    self.check(result, s, 3, getitem)
    s2 = s.copy()
    result = idxr(s2)[indexer]
    self.check(result, s, 3, getitem)
    with pytest.raises(KeyError, match='^3\\.5$'):
        idxr(s)[3.5]
assert 3.0 in s
expected = s.iloc[3]
s2 = s.copy()
s2.iloc[3] = expected
result = s2.iloc[3]
self.check(result, s, 3, False)
```

## Next Steps


---

*Source: test_floats.py:185 | Complexity: Advanced | Last updated: 2026-06-02*