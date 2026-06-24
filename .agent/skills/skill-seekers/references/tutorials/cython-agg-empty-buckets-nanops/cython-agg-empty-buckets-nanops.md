# How To: Cython Agg Empty Buckets Nanops

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython agg empty buckets nanops

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: observed
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([11, 12, 13], columns=['a'])
```

### Step 2: Assign grps = np.arange(...)

```python
grps = np.arange(0, 25, 5, dtype=int)
```

### Step 3: Assign result = df.groupby._cython_agg_general(...)

```python
result = df.groupby(pd.cut(df['a'], grps), observed=observed)._cython_agg_general('sum', alt=None, numeric_only=True)
```

### Step 4: Assign intervals = pd.interval_range(...)

```python
intervals = pd.interval_range(0, 20, freq=5)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [0, 0, 36, 0]}, index=pd.CategoricalIndex(intervals, name='a', ordered=True))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = df.groupby._cython_agg_general(...)

```python
result = df.groupby(pd.cut(df['a'], grps), observed=observed)._cython_agg_general('prod', alt=None, numeric_only=True)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 1, 1716, 1]}, index=pd.CategoricalIndex(intervals, name='a', ordered=True))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign expected = value

```python
expected = expected[expected.a != 0]
```

### Step 11: Assign expected = value

```python
expected = expected[expected.a != 1]
```


## Complete Example

```python
# Setup
# Fixtures: observed

# Workflow
df = DataFrame([11, 12, 13], columns=['a'])
grps = np.arange(0, 25, 5, dtype=int)
result = df.groupby(pd.cut(df['a'], grps), observed=observed)._cython_agg_general('sum', alt=None, numeric_only=True)
intervals = pd.interval_range(0, 20, freq=5)
expected = DataFrame({'a': [0, 0, 36, 0]}, index=pd.CategoricalIndex(intervals, name='a', ordered=True))
if observed:
    expected = expected[expected.a != 0]
tm.assert_frame_equal(result, expected)
result = df.groupby(pd.cut(df['a'], grps), observed=observed)._cython_agg_general('prod', alt=None, numeric_only=True)
expected = DataFrame({'a': [1, 1, 1716, 1]}, index=pd.CategoricalIndex(intervals, name='a', ordered=True))
if observed:
    expected = expected[expected.a != 1]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_cython.py:230 | Complexity: Advanced | Last updated: 2026-06-02*