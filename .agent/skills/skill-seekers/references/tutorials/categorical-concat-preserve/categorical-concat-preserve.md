# How To: Categorical Concat Preserve

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical concat preserve

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(list('abc'), dtype='category')
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series(list('abd'), dtype='category')
```

### Step 3: Assign exp = Series(...)

```python
exp = Series(list('abcabd'))
```

### Step 4: Assign res = pd.concat(...)

```python
res = pd.concat([s, s2], ignore_index=True)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 6: Assign exp = Series(...)

```python
exp = Series(list('abcabc'), dtype='category')
```

### Step 7: Assign res = pd.concat(...)

```python
res = pd.concat([s, s], ignore_index=True)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 9: Assign exp = Series(...)

```python
exp = Series(list('abcabc'), index=[0, 1, 2, 0, 1, 2], dtype='category')
```

### Step 10: Assign res = pd.concat(...)

```python
res = pd.concat([s, s])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 12: Assign a = Series(...)

```python
a = Series(np.arange(6, dtype='int64'))
```

### Step 13: Assign b = Series(...)

```python
b = Series(list('aabbca'))
```

### Step 14: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': a, 'B': b.astype(CategoricalDtype(list('cab')))})
```

### Step 15: Assign res = pd.concat(...)

```python
res = pd.concat([df2, df2])
```

### Step 16: Assign exp = DataFrame(...)

```python
exp = DataFrame({'A': pd.concat([a, a]), 'B': pd.concat([b, b]).astype(CategoricalDtype(list('cab')))})
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
s = Series(list('abc'), dtype='category')
s2 = Series(list('abd'), dtype='category')
exp = Series(list('abcabd'))
res = pd.concat([s, s2], ignore_index=True)
tm.assert_series_equal(res, exp)
exp = Series(list('abcabc'), dtype='category')
res = pd.concat([s, s], ignore_index=True)
tm.assert_series_equal(res, exp)
exp = Series(list('abcabc'), index=[0, 1, 2, 0, 1, 2], dtype='category')
res = pd.concat([s, s])
tm.assert_series_equal(res, exp)
a = Series(np.arange(6, dtype='int64'))
b = Series(list('aabbca'))
df2 = DataFrame({'A': a, 'B': b.astype(CategoricalDtype(list('cab')))})
res = pd.concat([df2, df2])
exp = DataFrame({'A': pd.concat([a, a]), 'B': pd.concat([b, b]).astype(CategoricalDtype(list('cab')))})
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_categorical.py:96 | Complexity: Advanced | Last updated: 2026-06-02*