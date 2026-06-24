# How To: Dti Set Index Reindex Datetimeindex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti set index reindex datetimeindex

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random(6))
```

### Step 2: Assign idx1 = date_range(...)

```python
idx1 = date_range('2011/01/01', periods=6, freq='ME', tz='US/Eastern')
```

### Step 3: Assign idx2 = date_range(...)

```python
idx2 = date_range('2013', periods=6, freq='YE', tz='Asia/Tokyo')
```

### Step 4: Assign df = df.set_index(...)

```python
df = df.set_index(idx1)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, idx1)
```

### Step 6: Assign df = df.reindex(...)

```python
df = df.reindex(idx2)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, idx2)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).random(6))
idx1 = date_range('2011/01/01', periods=6, freq='ME', tz='US/Eastern')
idx2 = date_range('2013', periods=6, freq='YE', tz='Asia/Tokyo')
df = df.set_index(idx1)
tm.assert_index_equal(df.index, idx1)
df = df.reindex(idx2)
tm.assert_index_equal(df.index, idx2)
```

## Next Steps


---

*Source: test_reindex.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*