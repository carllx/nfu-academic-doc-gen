# How To: Set Index Append To Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set index append to multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_of_index_cols, drop, keys
```

## Step-by-Step Guide

### Step 1: Assign df = frame_of_index_cols.set_index(...)

```python
df = frame_of_index_cols.set_index(['D'], drop=drop, append=True)
```

### Step 2: Assign keys = value

```python
keys = keys if isinstance(keys, list) else [keys]
```

### Step 3: Assign expected = frame_of_index_cols.set_index(...)

```python
expected = frame_of_index_cols.set_index(['D'] + keys, drop=drop, append=True)
```

### Step 4: Assign result = df.set_index(...)

```python
result = df.set_index(keys, drop=drop, append=True)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_of_index_cols, drop, keys

# Workflow
df = frame_of_index_cols.set_index(['D'], drop=drop, append=True)
keys = keys if isinstance(keys, list) else [keys]
expected = frame_of_index_cols.set_index(['D'] + keys, drop=drop, append=True)
result = df.set_index(keys, drop=drop, append=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_set_index.py:235 | Complexity: Intermediate | Last updated: 2026-06-02*