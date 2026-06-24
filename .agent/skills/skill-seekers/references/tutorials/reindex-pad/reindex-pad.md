# How To: Reindex Pad

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex pad

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.arange(10), dtype='int64')
```

### Step 2: Assign s2 = value

```python
s2 = s[::2]
```

### Step 3: Assign reindexed = s2.reindex(...)

```python
reindexed = s2.reindex(s.index, method='pad')
```

### Step 4: Assign reindexed2 = s2.reindex(...)

```python
reindexed2 = s2.reindex(s.index, method='ffill')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(reindexed, reindexed2)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([0, 0, 2, 2, 4, 4, 6, 6, 8, 8])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(reindexed, expected)
```


## Complete Example

```python
# Workflow
s = Series(np.arange(10), dtype='int64')
s2 = s[::2]
reindexed = s2.reindex(s.index, method='pad')
reindexed2 = s2.reindex(s.index, method='ffill')
tm.assert_series_equal(reindexed, reindexed2)
expected = Series([0, 0, 2, 2, 4, 4, 6, 6, 8, 8])
tm.assert_series_equal(reindexed, expected)
```

## Next Steps


---

*Source: test_reindex.py:119 | Complexity: Intermediate | Last updated: 2026-06-02*