# How To: Na Treated As False

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test na treated as false

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series, indexer_sli
```

## Step-by-Step Guide

### Step 1: Assign obj = frame_or_series(...)

```python
obj = frame_or_series([1, 2, 3])
```

### Step 2: Assign mask = pd.array(...)

```python
mask = pd.array([True, False, None], dtype='boolean')
```

### Step 3: Assign result = value

```python
result = indexer_sli(obj)[mask]
```

### Step 4: Assign expected = value

```python
expected = indexer_sli(obj)[mask.fillna(False)]
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, indexer_sli

# Workflow
obj = frame_or_series([1, 2, 3])
mask = pd.array([True, False, None], dtype='boolean')
result = indexer_sli(obj)[mask]
expected = indexer_sli(obj)[mask.fillna(False)]
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_na_indexing.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*