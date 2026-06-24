# How To: Frame Getitem Toplevel

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test frame getitem toplevel

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data, indexer, expected_slice
```

## Step-by-Step Guide

### Step 1: Assign df = value

```python
df = multiindex_dataframe_random_data.T
```

### Step 2: Assign expected = df.reindex(...)

```python
expected = df.reindex(columns=df.columns[expected_slice])
```

### Step 3: Assign expected.columns = expected.columns.droplevel(...)

```python
expected.columns = expected.columns.droplevel(0)
```

### Step 4: Assign result = indexer(...)

```python
result = indexer(df)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data, indexer, expected_slice

# Workflow
df = multiindex_dataframe_random_data.T
expected = df.reindex(columns=df.columns[expected_slice])
expected.columns = expected.columns.droplevel(0)
result = indexer(df)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*