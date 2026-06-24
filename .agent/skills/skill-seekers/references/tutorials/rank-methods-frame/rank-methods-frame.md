# How To: Rank Methods Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank methods frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ax, m
```

## Step-by-Step Guide

### Step 1: Assign sp_stats = pytest.importorskip(...)

```python
sp_stats = pytest.importorskip('scipy.stats')
```

### Step 2: Assign xs = np.random.default_rng.integers(...)

```python
xs = np.random.default_rng(2).integers(0, 21, (100, 26))
```

### Step 3: Assign xs = value

```python
xs = (xs - 10.0) / 10.0
```

### Step 4: Assign cols = value

```python
cols = [chr(ord('z') - i) for i in range(xs.shape[1])]
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(vals, columns=cols)
```

### Step 6: Assign result = df.rank(...)

```python
result = df.rank(axis=ax, method=m)
```

### Step 7: Assign sprank = np.apply_along_axis(...)

```python
sprank = np.apply_along_axis(sp_stats.rankdata, ax, vals, m if m != 'first' else 'ordinal')
```

### Step 8: Assign sprank = sprank.astype(...)

```python
sprank = sprank.astype(np.float64)
```

### Step 9: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame(sprank, columns=cols).astype('float64')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ax, m

# Workflow
sp_stats = pytest.importorskip('scipy.stats')
xs = np.random.default_rng(2).integers(0, 21, (100, 26))
xs = (xs - 10.0) / 10.0
cols = [chr(ord('z') - i) for i in range(xs.shape[1])]
for vals in [xs, xs + 1000000.0, xs * 1e-06]:
    df = DataFrame(vals, columns=cols)
    result = df.rank(axis=ax, method=m)
    sprank = np.apply_along_axis(sp_stats.rankdata, ax, vals, m if m != 'first' else 'ordinal')
    sprank = sprank.astype(np.float64)
    expected = DataFrame(sprank, columns=cols).astype('float64')
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:229 | Complexity: Advanced | Last updated: 2026-06-02*