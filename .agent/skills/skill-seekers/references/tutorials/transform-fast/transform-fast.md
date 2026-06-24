# How To: Transform Fast

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform fast

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'id': np.arange(100000) / 3, 'val': np.random.default_rng(2).standard_normal(100000)})
```

### Step 2: Assign grp = value

```python
grp = df.groupby('id')['val']
```

### Step 3: Assign values = np.repeat(...)

```python
values = np.repeat(grp.mean().values, ensure_platform_int(grp.count().values))
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(values, index=df.index, name='val')
```

### Step 5: Assign msg = 'using SeriesGroupBy.mean'

```python
msg = 'using SeriesGroupBy.mean'
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = grp.transform(...)

```python
result = grp.transform('mean')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = grp.transform(...)

```python
result = grp.transform(np.mean)
```


## Complete Example

```python
# Workflow
df = DataFrame({'id': np.arange(100000) / 3, 'val': np.random.default_rng(2).standard_normal(100000)})
grp = df.groupby('id')['val']
values = np.repeat(grp.mean().values, ensure_platform_int(grp.count().values))
expected = Series(values, index=df.index, name='val')
msg = 'using SeriesGroupBy.mean'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = grp.transform(np.mean)
tm.assert_series_equal(result, expected)
result = grp.transform('mean')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_transform.py:88 | Complexity: Advanced | Last updated: 2026-06-02*