# How To: Timestamp Multiindex Indexer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timestamp multiindex indexer

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

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([date_range('2019-01-01T00:15:33', periods=100, freq='h', name='date'), ['x'], [3]])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'foo': np.arange(len(idx))}, idx)
```

### Step 3: Assign result = value

```python
result = df.loc[pd.IndexSlice['2019-1-2':, 'x', :], 'foo']
```

### Step 4: Assign qidx = MultiIndex.from_product(...)

```python
qidx = MultiIndex.from_product([date_range(start='2019-01-02T00:15:33', end='2019-01-05T03:15:33', freq='h', name='date'), ['x'], [3]])
```

### Step 5: Assign should_be = pd.Series(...)

```python
should_be = pd.Series(data=np.arange(24, len(qidx) + 24), index=qidx, name='foo')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, should_be)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_product([date_range('2019-01-01T00:15:33', periods=100, freq='h', name='date'), ['x'], [3]])
df = DataFrame({'foo': np.arange(len(idx))}, idx)
result = df.loc[pd.IndexSlice['2019-1-2':, 'x', :], 'foo']
qidx = MultiIndex.from_product([date_range(start='2019-01-02T00:15:33', end='2019-01-05T03:15:33', freq='h', name='date'), ['x'], [3]])
should_be = pd.Series(data=np.arange(24, len(qidx) + 24), index=qidx, name='foo')
tm.assert_series_equal(result, should_be)
```

## Next Steps


---

*Source: test_indexing.py:868 | Complexity: Intermediate | Last updated: 2026-06-02*