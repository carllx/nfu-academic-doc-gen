# How To: Multiindex Align To Series With Common Index Level Non Unique Cols

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex align to series with common index level non unique cols

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign foo_index = Index(...)

```python
foo_index = Index([1, 2, 3], name='foo')
```

### Step 2: Assign bar_index = Index(...)

```python
bar_index = Index([1, 2], name='bar')
```

### Step 3: Assign series = Series(...)

```python
series = Series([1, 2], index=bar_index, name='foo_series')
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(18).reshape(6, 3), index=pd.MultiIndex.from_product([foo_index, bar_index]))
```

### Step 5: Assign df.columns = value

```python
df.columns = ['cfoo', 'cbar', 'cfoo']
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, 2] * 3, index=df.index, name='foo_series')
```

### Step 7: Assign unknown = df.align(...)

```python
result_left, result_right = df.align(series, axis=0)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_right, expected)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result_left.columns, df.columns)
```


## Complete Example

```python
# Workflow
foo_index = Index([1, 2, 3], name='foo')
bar_index = Index([1, 2], name='bar')
series = Series([1, 2], index=bar_index, name='foo_series')
df = DataFrame(np.arange(18).reshape(6, 3), index=pd.MultiIndex.from_product([foo_index, bar_index]))
df.columns = ['cfoo', 'cbar', 'cfoo']
expected = Series([1, 2] * 3, index=df.index, name='foo_series')
result_left, result_right = df.align(series, axis=0)
tm.assert_series_equal(result_right, expected)
tm.assert_index_equal(result_left.columns, df.columns)
```

## Next Steps


---

*Source: test_align.py:370 | Complexity: Advanced | Last updated: 2026-06-02*