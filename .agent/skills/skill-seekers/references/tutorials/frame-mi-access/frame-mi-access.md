# How To: Frame Mi Access

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test frame mi access

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
# Fixtures: dataframe_with_duplicate_index, indexer
```

## Step-by-Step Guide

### Step 1: Assign df = dataframe_with_duplicate_index

```python
df = dataframe_with_duplicate_index
```

### Step 2: Assign index = Index(...)

```python
index = Index(['h1', 'h3', 'h5'])
```

### Step 3: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('A', 'A1')], names=['main', 'sub'])
```

### Step 4: Assign expected = value

```python
expected = DataFrame([['a', 1, 1]], index=columns, columns=index).T
```

### Step 5: Assign result = indexer(...)

```python
result = indexer(df)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dataframe_with_duplicate_index, indexer

# Workflow
df = dataframe_with_duplicate_index
index = Index(['h1', 'h3', 'h5'])
columns = MultiIndex.from_tuples([('A', 'A1')], names=['main', 'sub'])
expected = DataFrame([['a', 1, 1]], index=columns, columns=index).T
result = indexer(df)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:350 | Complexity: Intermediate | Last updated: 2026-06-02*