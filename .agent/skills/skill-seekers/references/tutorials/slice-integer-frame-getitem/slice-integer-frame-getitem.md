# How To: Slice Integer Frame Getitem

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test slice integer frame getitem

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign s = DataFrame(...)

```python
s = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), index=index)
```

### Step 2: Assign msg = value

```python
msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[-10\\.0\\] of type float'
```

### Step 3: Assign result = value

```python
result = s.loc[idx]
```

### Step 4: Assign indexer = slice(...)

```python
indexer = slice(0, 2)
```

### Step 5: Call self.check()

```python
self.check(result, s, indexer, False)
```

### Step 6: Assign msg = value

```python
msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[(0|1)\\.0\\] of type float'
```

### Step 7: Assign result = value

```python
result = s.loc[idx]
```

### Step 8: Call self.check()

```python
self.check(result, s, slice(-10, 10), True)
```

### Step 9: s[slice(-10.0, 10.0)]

```python
s[slice(-10.0, 10.0)]
```

### Step 10: Assign result = value

```python
result = s.loc[idx]
```

### Step 11: Call self.check()

```python
self.check(result, s, res, False)
```

### Step 12: Assign msg = value

```python
msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[0\\.5\\] of type float'
```

### Step 13: s[idx]

```python
s[idx]
```

### Step 14: s[idx]

```python
s[idx]
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
s = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), index=index)
for idx in [slice(0.0, 1), slice(0, 1.0), slice(0.0, 1.0)]:
    result = s.loc[idx]
    indexer = slice(0, 2)
    self.check(result, s, indexer, False)
    msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[(0|1)\\.0\\] of type float'
    with pytest.raises(TypeError, match=msg):
        s[idx]
for idx in [slice(-10, 10), slice(-10.0, 10.0)]:
    result = s.loc[idx]
    self.check(result, s, slice(-10, 10), True)
msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[-10\\.0\\] of type float'
with pytest.raises(TypeError, match=msg):
    s[slice(-10.0, 10.0)]
for idx, res in [(slice(0.5, 1), slice(1, 2)), (slice(0, 0.5), slice(0, 1)), (slice(0.5, 1.5), slice(1, 2))]:
    result = s.loc[idx]
    self.check(result, s, res, False)
    msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[0\\.5\\] of type float'
    with pytest.raises(TypeError, match=msg):
        s[idx]
```

## Next Steps


---

*Source: test_floats.py:357 | Complexity: Advanced | Last updated: 2026-06-02*