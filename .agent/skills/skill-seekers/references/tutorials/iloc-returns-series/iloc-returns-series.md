# How To: Iloc Returns Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test iloc returns series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: indexer, expected, simple_multiindex_dataframe
```

## Step-by-Step Guide

### Step 1: Assign df = simple_multiindex_dataframe

```python
df = simple_multiindex_dataframe
```

### Step 2: Assign arr = value

```python
arr = df.values
```

### Step 3: Assign result = indexer(...)

```python
result = indexer(df)
```

### Step 4: Assign expected = expected(...)

```python
expected = expected(arr)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: indexer, expected, simple_multiindex_dataframe

# Workflow
df = simple_multiindex_dataframe
arr = df.values
result = indexer(df)
expected = expected(arr)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_iloc.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*