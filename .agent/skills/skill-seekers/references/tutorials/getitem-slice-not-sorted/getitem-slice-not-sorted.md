# How To: Getitem Slice Not Sorted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem slice not sorted

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign frame = multiindex_dataframe_random_data

```python
frame = multiindex_dataframe_random_data
```

### Step 2: Assign df = value

```python
df = frame.sort_index(level=1).T
```

### Step 3: Assign result = value

```python
result = df.iloc[:, :np.int32(3)]
```

### Step 4: Assign expected = df.reindex(...)

```python
expected = df.reindex(columns=df.columns[:3])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
df = frame.sort_index(level=1).T
result = df.iloc[:, :np.int32(3)]
expected = df.reindex(columns=df.columns[:3])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sorted.py:28 | Complexity: Intermediate | Last updated: 2026-06-02*