# How To: Fixed Forward Indexer Count

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fixed forward indexer count

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: step
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'b': [None, None, None, 7]})
```

### Step 2: Assign indexer = FixedForwardWindowIndexer(...)

```python
indexer = FixedForwardWindowIndexer(window_size=2)
```

### Step 3: Assign result = df.rolling.count(...)

```python
result = df.rolling(window=indexer, min_periods=0, step=step).count()
```

### Step 4: Assign expected = value

```python
expected = DataFrame({'b': [0.0, 0.0, 1.0, 1.0]})[::step]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: step

# Workflow
df = DataFrame({'b': [None, None, None, 7]})
indexer = FixedForwardWindowIndexer(window_size=2)
result = df.rolling(window=indexer, min_periods=0, step=step).count()
expected = DataFrame({'b': [0.0, 0.0, 1.0, 1.0]})[::step]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_base_indexer.py:284 | Complexity: Intermediate | Last updated: 2026-06-02*