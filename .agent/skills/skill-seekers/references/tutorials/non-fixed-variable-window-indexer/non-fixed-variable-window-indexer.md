# How To: Non Fixed Variable Window Indexer

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test non fixed variable window indexer

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
# Fixtures: closed, expected_data
```

## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('2020', periods=10)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(range(10), index=index)
```

### Step 3: Assign offset = BusinessDay(...)

```python
offset = BusinessDay(1)
```

### Step 4: Assign indexer = VariableOffsetWindowIndexer(...)

```python
indexer = VariableOffsetWindowIndexer(index=index, offset=offset)
```

### Step 5: Assign result = df.rolling.sum(...)

```python
result = df.rolling(indexer, closed=closed).sum()
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_data, index=index)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, expected_data

# Workflow
index = date_range('2020', periods=10)
df = DataFrame(range(10), index=index)
offset = BusinessDay(1)
indexer = VariableOffsetWindowIndexer(index=index, offset=offset)
result = df.rolling(indexer, closed=closed).sum()
expected = DataFrame(expected_data, index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_base_indexer.py:261 | Complexity: Intermediate | Last updated: 2026-06-02*