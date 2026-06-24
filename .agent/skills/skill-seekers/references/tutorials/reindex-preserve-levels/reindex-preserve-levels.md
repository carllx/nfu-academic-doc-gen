# How To: Reindex Preserve Levels

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex preserve levels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_year_month_day_dataframe_random_data, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ymd = multiindex_year_month_day_dataframe_random_data

```python
ymd = multiindex_year_month_day_dataframe_random_data
```

**Verification:**
```python
assert chunk.index.is_(new_index)
```

### Step 2: Assign new_index = value

```python
new_index = ymd.index[::10]
```

**Verification:**
```python
assert chunk.index is new_index
```

### Step 3: Assign chunk = ymd.reindex(...)

```python
chunk = ymd.reindex(new_index)
```

**Verification:**
```python
assert chunk.index.equals(new_index)
```

### Step 4: Assign chunk = value

```python
chunk = ymd.loc[new_index]
```

**Verification:**
```python
assert chunk.columns.is_(new_index)
```

### Step 5: Assign ymdT = value

```python
ymdT = ymd.T
```

**Verification:**
```python
assert chunk.columns is new_index
```

### Step 6: Assign chunk = ymdT.reindex(...)

```python
chunk = ymdT.reindex(columns=new_index)
```

**Verification:**
```python
assert chunk.columns.equals(new_index)
```

### Step 7: Assign chunk = value

```python
chunk = ymdT.loc[:, new_index]
```

**Verification:**
```python
assert chunk.columns.equals(new_index)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_year_month_day_dataframe_random_data, using_copy_on_write

# Workflow
ymd = multiindex_year_month_day_dataframe_random_data
new_index = ymd.index[::10]
chunk = ymd.reindex(new_index)
if using_copy_on_write:
    assert chunk.index.is_(new_index)
else:
    assert chunk.index is new_index
chunk = ymd.loc[new_index]
assert chunk.index.equals(new_index)
ymdT = ymd.T
chunk = ymdT.reindex(columns=new_index)
if using_copy_on_write:
    assert chunk.columns.is_(new_index)
else:
    assert chunk.columns is new_index
chunk = ymdT.loc[:, new_index]
assert chunk.columns.equals(new_index)
```

## Next Steps


---

*Source: test_multilevel.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*