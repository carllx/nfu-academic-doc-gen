# How To: Expanding Indexer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test expanding indexer

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(range(10))
```

### Step 2: Assign indexer = ExpandingIndexer(...)

```python
indexer = ExpandingIndexer()
```

### Step 3: Assign result = s.rolling.mean(...)

```python
result = s.rolling(indexer).mean()
```

### Step 4: Assign expected = s.expanding.mean(...)

```python
expected = s.expanding().mean()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series(range(10))
indexer = ExpandingIndexer()
result = s.rolling(indexer).mean()
expected = s.expanding().mean()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_base_indexer.py:35 | Complexity: Intermediate | Last updated: 2026-06-02*