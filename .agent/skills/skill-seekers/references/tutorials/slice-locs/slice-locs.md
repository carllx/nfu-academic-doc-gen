# How To: Slice Locs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice locs

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
df = DataFrame(np.random.default_rng(2).standard_normal((50, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=50, freq='B'))
```

### Step 2: Assign stacked = df.stack(...)

```python
stacked = df.stack(future_stack=True)
```

### Step 3: Assign idx = value

```python
idx = stacked.index
```

### Step 4: Assign slob = slice(...)

```python
slob = slice(*idx.slice_locs(df.index[5], df.index[15]))
```

### Step 5: Assign sliced = value

```python
sliced = stacked[slob]
```

### Step 6: Assign expected = unknown.stack(...)

```python
expected = df[5:16].stack(future_stack=True)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(sliced.values, expected.values)
```

### Step 8: Assign slob = slice(...)

```python
slob = slice(*idx.slice_locs(df.index[5] + timedelta(seconds=30), df.index[15] - timedelta(seconds=30)))
```

### Step 9: Assign sliced = value

```python
sliced = stacked[slob]
```

### Step 10: Assign expected = unknown.stack(...)

```python
expected = df[6:15].stack(future_stack=True)
```

### Step 11: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(sliced.values, expected.values)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((50, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=50, freq='B'))
stacked = df.stack(future_stack=True)
idx = stacked.index
slob = slice(*idx.slice_locs(df.index[5], df.index[15]))
sliced = stacked[slob]
expected = df[5:16].stack(future_stack=True)
tm.assert_almost_equal(sliced.values, expected.values)
slob = slice(*idx.slice_locs(df.index[5] + timedelta(seconds=30), df.index[15] - timedelta(seconds=30)))
sliced = stacked[slob]
expected = df[6:15].stack(future_stack=True)
tm.assert_almost_equal(sliced.values, expected.values)
```

## Next Steps


---

*Source: test_indexing.py:40 | Complexity: Advanced | Last updated: 2026-06-02*