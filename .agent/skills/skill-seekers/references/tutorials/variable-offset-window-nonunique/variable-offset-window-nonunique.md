# How To: Variable Offset Window Nonunique

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test variable offset window nonunique

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: closed, expected, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign index = DatetimeIndex(...)

```python
index = DatetimeIndex(['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-02', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-04', '2011-01-05', '2011-01-06'])
```

### Step 2: Assign df = frame_or_series(...)

```python
df = frame_or_series(range(10), index=index, dtype=float)
```

### Step 3: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(expected, index=index, dtype=float)
```

### Step 4: Assign offset = BusinessDay(...)

```python
offset = BusinessDay(2)
```

### Step 5: Assign indexer = VariableOffsetWindowIndexer(...)

```python
indexer = VariableOffsetWindowIndexer(index=index, offset=offset)
```

### Step 6: Assign result = df.rolling.sum(...)

```python
result = df.rolling(indexer, closed=closed, min_periods=1).sum()
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, expected, frame_or_series

# Workflow
index = DatetimeIndex(['2011-01-01', '2011-01-01', '2011-01-02', '2011-01-02', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-04', '2011-01-05', '2011-01-06'])
df = frame_or_series(range(10), index=index, dtype=float)
expected = frame_or_series(expected, index=index, dtype=float)
offset = BusinessDay(2)
indexer = VariableOffsetWindowIndexer(index=index, offset=offset)
result = df.rolling(indexer, closed=closed, min_periods=1).sum()
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling.py:350 | Complexity: Intermediate | Last updated: 2026-06-02*