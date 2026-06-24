# How To: Align Series Combinations

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test align series combinations

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 3, 5], 'b': [1, 3, 5]}, index=list('ACE'))
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 2, 4], index=list('ABD'), name='x')
```

### Step 3: Assign unknown = df.align(...)

```python
res1, res2 = df.align(s, axis=0)
```

### Step 4: Assign exp1 = DataFrame(...)

```python
exp1 = DataFrame({'a': [1, np.nan, 3, np.nan, 5], 'b': [1, np.nan, 3, np.nan, 5]}, index=list('ABCDE'))
```

### Step 5: Assign exp2 = Series(...)

```python
exp2 = Series([1, 2, np.nan, 4, np.nan], index=list('ABCDE'), name='x')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res1, exp1)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, exp2)
```

### Step 8: Assign unknown = s.align(...)

```python
res1, res2 = s.align(df)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res1, exp2)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, exp1)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 3, 5], 'b': [1, 3, 5]}, index=list('ACE'))
s = Series([1, 2, 4], index=list('ABD'), name='x')
res1, res2 = df.align(s, axis=0)
exp1 = DataFrame({'a': [1, np.nan, 3, np.nan, 5], 'b': [1, np.nan, 3, np.nan, 5]}, index=list('ABCDE'))
exp2 = Series([1, 2, np.nan, 4, np.nan], index=list('ABCDE'), name='x')
tm.assert_frame_equal(res1, exp1)
tm.assert_series_equal(res2, exp2)
res1, res2 = s.align(df)
tm.assert_series_equal(res1, exp2)
tm.assert_frame_equal(res2, exp1)
```

## Next Steps


---

*Source: test_align.py:276 | Complexity: Advanced | Last updated: 2026-06-02*