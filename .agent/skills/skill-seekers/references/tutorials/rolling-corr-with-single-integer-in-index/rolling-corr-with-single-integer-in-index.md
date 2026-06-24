# How To: Rolling Corr With Single Integer In Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling corr with single integer in index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.groupby.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [(1,), (1,), (1,)], 'b': [4, 5, 6]})
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby(['a'])
```

### Step 3: Assign result = gb.rolling.corr(...)

```python
result = gb.rolling(2).corr(other=df)
```

### Step 4: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([((1,), 0), ((1,), 1), ((1,), 2)], names=['a', None])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [np.nan, np.nan, np.nan], 'b': [np.nan, 1.0, 1.0]}, index=index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [(1,), (1,), (1,)], 'b': [4, 5, 6]})
gb = df.groupby(['a'])
result = gb.rolling(2).corr(other=df)
index = MultiIndex.from_tuples([((1,), 0), ((1,), 1), ((1,), 2)], names=['a', None])
expected = DataFrame({'a': [np.nan, np.nan, np.nan], 'b': [np.nan, 1.0, 1.0]}, index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby.py:1277 | Complexity: Intermediate | Last updated: 2026-06-02*