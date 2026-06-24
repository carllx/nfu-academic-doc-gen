# How To: Rank Methods Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank methods series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: method, op, value
```

## Step-by-Step Guide

### Step 1: Assign sp_stats = pytest.importorskip(...)

```python
sp_stats = pytest.importorskip('scipy.stats')
```

### Step 2: Assign xs = np.random.default_rng.standard_normal(...)

```python
xs = np.random.default_rng(2).standard_normal(9)
```

### Step 3: Assign xs = np.concatenate(...)

```python
xs = np.concatenate([xs[i:] for i in range(0, 9, 2)])
```

### Step 4: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(xs)
```

### Step 5: Assign index = value

```python
index = [chr(ord('a') + i) for i in range(len(xs))]
```

### Step 6: Assign vals = op(...)

```python
vals = op(xs, value)
```

### Step 7: Assign ts = Series(...)

```python
ts = Series(vals, index=index)
```

### Step 8: Assign result = ts.rank(...)

```python
result = ts.rank(method=method)
```

### Step 9: Assign sprank = sp_stats.rankdata(...)

```python
sprank = sp_stats.rankdata(vals, method if method != 'first' else 'ordinal')
```

### Step 10: Assign expected = Series.astype(...)

```python
expected = Series(sprank, index=index).astype('float64')
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, op, value

# Workflow
sp_stats = pytest.importorskip('scipy.stats')
xs = np.random.default_rng(2).standard_normal(9)
xs = np.concatenate([xs[i:] for i in range(0, 9, 2)])
np.random.default_rng(2).shuffle(xs)
index = [chr(ord('a') + i) for i in range(len(xs))]
vals = op(xs, value)
ts = Series(vals, index=index)
result = ts.rank(method=method)
sprank = sp_stats.rankdata(vals, method if method != 'first' else 'ordinal')
expected = Series(sprank, index=index).astype('float64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:344 | Complexity: Advanced | Last updated: 2026-06-02*