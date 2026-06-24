# How To: Reindex With Multi Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex with multi index

## Prerequisites

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'a': [-1] * 7 + [0] * 7 + [1] * 7, 'b': list(range(7)) * 3, 'c': ['A', 'B', 'C', 'D', 'E', 'F', 'G'] * 3}).set_index(['a', 'b'])
```

### Step 2: Assign new_index = value

```python
new_index = [0.5, 2.0, 5.0, 5.8]
```

### Step 3: Assign new_multi_index = MultiIndex.from_product(...)

```python
new_multi_index = MultiIndex.from_product([[0], new_index], names=['a', 'b'])
```

### Step 4: Assign reindexed = df.reindex(...)

```python
reindexed = df.reindex(new_multi_index)
```

### Step 5: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'a': [0] * 4, 'b': new_index, 'c': [np.nan, 'C', 'F', np.nan]}).set_index(['a', 'b'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, reindexed)
```

### Step 7: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'a': [0] * 4, 'b': new_index, 'c': ['B', 'C', 'F', 'G']}).set_index(['a', 'b'])
```

### Step 8: Assign reindexed_with_backfilling = df.reindex(...)

```python
reindexed_with_backfilling = df.reindex(new_multi_index, method='bfill')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, reindexed_with_backfilling)
```

### Step 10: Assign reindexed_with_backfilling = df.reindex(...)

```python
reindexed_with_backfilling = df.reindex(new_multi_index, method='backfill')
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, reindexed_with_backfilling)
```

### Step 12: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'a': [0] * 4, 'b': new_index, 'c': ['A', 'C', 'F', 'F']}).set_index(['a', 'b'])
```

### Step 13: Assign reindexed_with_padding = df.reindex(...)

```python
reindexed_with_padding = df.reindex(new_multi_index, method='pad')
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, reindexed_with_padding)
```

### Step 15: Assign reindexed_with_padding = df.reindex(...)

```python
reindexed_with_padding = df.reindex(new_multi_index, method='ffill')
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, reindexed_with_padding)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [-1] * 7 + [0] * 7 + [1] * 7, 'b': list(range(7)) * 3, 'c': ['A', 'B', 'C', 'D', 'E', 'F', 'G'] * 3}).set_index(['a', 'b'])
new_index = [0.5, 2.0, 5.0, 5.8]
new_multi_index = MultiIndex.from_product([[0], new_index], names=['a', 'b'])
reindexed = df.reindex(new_multi_index)
expected = DataFrame({'a': [0] * 4, 'b': new_index, 'c': [np.nan, 'C', 'F', np.nan]}).set_index(['a', 'b'])
tm.assert_frame_equal(expected, reindexed)
expected = DataFrame({'a': [0] * 4, 'b': new_index, 'c': ['B', 'C', 'F', 'G']}).set_index(['a', 'b'])
reindexed_with_backfilling = df.reindex(new_multi_index, method='bfill')
tm.assert_frame_equal(expected, reindexed_with_backfilling)
reindexed_with_backfilling = df.reindex(new_multi_index, method='backfill')
tm.assert_frame_equal(expected, reindexed_with_backfilling)
expected = DataFrame({'a': [0] * 4, 'b': new_index, 'c': ['A', 'C', 'F', 'F']}).set_index(['a', 'b'])
reindexed_with_padding = df.reindex(new_multi_index, method='pad')
tm.assert_frame_equal(expected, reindexed_with_padding)
reindexed_with_padding = df.reindex(new_multi_index, method='ffill')
tm.assert_frame_equal(expected, reindexed_with_padding)
```

## Next Steps


---

*Source: test_reindex.py:231 | Complexity: Advanced | Last updated: 2026-06-02*