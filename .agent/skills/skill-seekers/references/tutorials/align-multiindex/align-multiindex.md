# How To: Align Multiindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test align multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx = pd.MultiIndex.from_product(...)

```python
midx = pd.MultiIndex.from_product([range(2), range(3), range(2)], names=('a', 'b', 'c'))
```

### Step 2: Assign idx = pd.Index(...)

```python
idx = pd.Index(range(2), name='b')
```

### Step 3: Assign s1 = Series(...)

```python
s1 = Series(np.arange(12, dtype='int64'), index=midx)
```

### Step 4: Assign s2 = Series(...)

```python
s2 = Series(np.arange(2, dtype='int64'), index=idx)
```

### Step 5: Assign unknown = s1.align(...)

```python
res1l, res1r = s1.align(s2, join='left')
```

### Step 6: Assign unknown = s2.align(...)

```python
res2l, res2r = s2.align(s1, join='right')
```

### Step 7: Assign expl = s1

```python
expl = s1
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expl, res1l)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expl, res2r)
```

### Step 10: Assign expr = Series(...)

```python
expr = Series([0, 0, 1, 1, np.nan, np.nan] * 2, index=midx)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expr, res1r)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expr, res2l)
```

### Step 13: Assign unknown = s1.align(...)

```python
res1l, res1r = s1.align(s2, join='right')
```

### Step 14: Assign unknown = s2.align(...)

```python
res2l, res2r = s2.align(s1, join='left')
```

### Step 15: Assign exp_idx = pd.MultiIndex.from_product(...)

```python
exp_idx = pd.MultiIndex.from_product([range(2), range(2), range(2)], names=('a', 'b', 'c'))
```

### Step 16: Assign expl = Series(...)

```python
expl = Series([0, 1, 2, 3, 6, 7, 8, 9], index=exp_idx)
```

### Step 17: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expl, res1l)
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expl, res2r)
```

### Step 19: Assign expr = Series(...)

```python
expr = Series([0, 0, 1, 1] * 2, index=exp_idx)
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expr, res1r)
```

### Step 21: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expr, res2l)
```


## Complete Example

```python
# Workflow
midx = pd.MultiIndex.from_product([range(2), range(3), range(2)], names=('a', 'b', 'c'))
idx = pd.Index(range(2), name='b')
s1 = Series(np.arange(12, dtype='int64'), index=midx)
s2 = Series(np.arange(2, dtype='int64'), index=idx)
res1l, res1r = s1.align(s2, join='left')
res2l, res2r = s2.align(s1, join='right')
expl = s1
tm.assert_series_equal(expl, res1l)
tm.assert_series_equal(expl, res2r)
expr = Series([0, 0, 1, 1, np.nan, np.nan] * 2, index=midx)
tm.assert_series_equal(expr, res1r)
tm.assert_series_equal(expr, res2l)
res1l, res1r = s1.align(s2, join='right')
res2l, res2r = s2.align(s1, join='left')
exp_idx = pd.MultiIndex.from_product([range(2), range(2), range(2)], names=('a', 'b', 'c'))
expl = Series([0, 1, 2, 3, 6, 7, 8, 9], index=exp_idx)
tm.assert_series_equal(expl, res1l)
tm.assert_series_equal(expl, res2r)
expr = Series([0, 0, 1, 1] * 2, index=exp_idx)
tm.assert_series_equal(expr, res1r)
tm.assert_series_equal(expr, res2l)
```

## Next Steps


---

*Source: test_align.py:144 | Complexity: Advanced | Last updated: 2026-06-02*