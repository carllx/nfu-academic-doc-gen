# How To: Rank Apply

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rank apply

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign lev1 = np.array(...)

```python
lev1 = np.array(['a' * 10] * 100, dtype=object)
```

### Step 2: Assign lev2 = np.array(...)

```python
lev2 = np.array(['b' * 10] * 130, dtype=object)
```

### Step 3: Assign lab1 = np.random.default_rng.integers(...)

```python
lab1 = np.random.default_rng(2).integers(0, 100, size=500, dtype=int)
```

### Step 4: Assign lab2 = np.random.default_rng.integers(...)

```python
lab2 = np.random.default_rng(2).integers(0, 130, size=500, dtype=int)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'value': np.random.default_rng(2).standard_normal(500), 'key1': lev1.take(lab1), 'key2': lev2.take(lab2)})
```

### Step 6: Assign result = df.groupby.value.rank(...)

```python
result = df.groupby(['key1', 'key2']).value.rank()
```

### Step 7: Assign expected = value

```python
expected = [piece.value.rank() for key, piece in df.groupby(['key1', 'key2'])]
```

### Step 8: Assign expected = concat(...)

```python
expected = concat(expected, axis=0)
```

### Step 9: Assign expected = expected.reindex(...)

```python
expected = expected.reindex(result.index)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = df.groupby.value.rank(...)

```python
result = df.groupby(['key1', 'key2']).value.rank(pct=True)
```

### Step 12: Assign expected = value

```python
expected = [piece.value.rank(pct=True) for key, piece in df.groupby(['key1', 'key2'])]
```

### Step 13: Assign expected = concat(...)

```python
expected = concat(expected, axis=0)
```

### Step 14: Assign expected = expected.reindex(...)

```python
expected = expected.reindex(result.index)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
lev1 = np.array(['a' * 10] * 100, dtype=object)
lev2 = np.array(['b' * 10] * 130, dtype=object)
lab1 = np.random.default_rng(2).integers(0, 100, size=500, dtype=int)
lab2 = np.random.default_rng(2).integers(0, 130, size=500, dtype=int)
df = DataFrame({'value': np.random.default_rng(2).standard_normal(500), 'key1': lev1.take(lab1), 'key2': lev2.take(lab2)})
result = df.groupby(['key1', 'key2']).value.rank()
expected = [piece.value.rank() for key, piece in df.groupby(['key1', 'key2'])]
expected = concat(expected, axis=0)
expected = expected.reindex(result.index)
tm.assert_series_equal(result, expected)
result = df.groupby(['key1', 'key2']).value.rank(pct=True)
expected = [piece.value.rank(pct=True) for key, piece in df.groupby(['key1', 'key2'])]
expected = concat(expected, axis=0)
expected = expected.reindex(result.index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:33 | Complexity: Advanced | Last updated: 2026-06-02*