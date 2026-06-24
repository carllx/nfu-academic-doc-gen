# How To: Slice Locs With Type Mismatch

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice locs with type mismatch

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
```

### Step 2: Assign stacked = df.stack(...)

```python
stacked = df.stack(future_stack=True)
```

### Step 3: Assign idx = value

```python
idx = stacked.index
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((5, 5)), index=Index([f'i-{i}' for i in range(5)], name='a'), columns=Index([f'i-{i}' for i in range(5)], name='a'))
```

### Step 5: Assign stacked = df.stack(...)

```python
stacked = df.stack(future_stack=True)
```

### Step 6: Assign idx = value

```python
idx = stacked.index
```

### Step 7: Call idx.slice_locs()

```python
idx.slice_locs((1, 3))
```

### Step 8: Call idx.slice_locs()

```python
idx.slice_locs(df.index[5] + timedelta(seconds=30), (5, 2))
```

### Step 9: Call idx.slice_locs()

```python
idx.slice_locs(timedelta(seconds=30))
```

### Step 10: Call idx.slice_locs()

```python
idx.slice_locs(df.index[1], (16, 'a'))
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=10, freq='B'))
stacked = df.stack(future_stack=True)
idx = stacked.index
with pytest.raises(TypeError, match='^Level type mismatch'):
    idx.slice_locs((1, 3))
with pytest.raises(TypeError, match='^Level type mismatch'):
    idx.slice_locs(df.index[5] + timedelta(seconds=30), (5, 2))
df = DataFrame(np.ones((5, 5)), index=Index([f'i-{i}' for i in range(5)], name='a'), columns=Index([f'i-{i}' for i in range(5)], name='a'))
stacked = df.stack(future_stack=True)
idx = stacked.index
with pytest.raises(TypeError, match='^Level type mismatch'):
    idx.slice_locs(timedelta(seconds=30))
with pytest.raises(TypeError, match='^Level type mismatch'):
    idx.slice_locs(df.index[1], (16, 'a'))
```

## Next Steps


---

*Source: test_indexing.py:64 | Complexity: Advanced | Last updated: 2026-06-02*