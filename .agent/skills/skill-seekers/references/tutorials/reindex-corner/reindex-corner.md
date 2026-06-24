# How To: Reindex Corner

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex corner

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign empty = Series(...)

```python
empty = Series(index=[])
```

### Step 2: Call empty.reindex()

```python
empty.reindex(datetime_series.index, method='pad')
```

### Step 3: Assign reindexed = empty.reindex(...)

```python
reindexed = empty.reindex(datetime_series.index, method='pad')
```

### Step 4: Assign reindexed = datetime_series.reindex(...)

```python
reindexed = datetime_series.reindex(list(datetime_series.index))
```

### Step 5: Assign datetime_series.index = datetime_series.index._with_freq(...)

```python
datetime_series.index = datetime_series.index._with_freq(None)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(datetime_series, reindexed)
```

### Step 7: Assign ts = value

```python
ts = datetime_series[::2]
```

### Step 8: Assign msg = 'Invalid fill method\\. Expecting pad \\(ffill\\), backfill \\(bfill\\) or nearest\\. Got foo'

```python
msg = 'Invalid fill method\\. Expecting pad \\(ffill\\), backfill \\(bfill\\) or nearest\\. Got foo'
```

### Step 9: Call ts.reindex()

```python
ts.reindex(datetime_series.index, method='foo')
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
empty = Series(index=[])
empty.reindex(datetime_series.index, method='pad')
reindexed = empty.reindex(datetime_series.index, method='pad')
reindexed = datetime_series.reindex(list(datetime_series.index))
datetime_series.index = datetime_series.index._with_freq(None)
tm.assert_series_equal(datetime_series, reindexed)
ts = datetime_series[::2]
msg = 'Invalid fill method\\. Expecting pad \\(ffill\\), backfill \\(bfill\\) or nearest\\. Got foo'
with pytest.raises(ValueError, match=msg):
    ts.reindex(datetime_series.index, method='foo')
```

## Next Steps


---

*Source: test_reindex.py:96 | Complexity: Advanced | Last updated: 2026-06-02*