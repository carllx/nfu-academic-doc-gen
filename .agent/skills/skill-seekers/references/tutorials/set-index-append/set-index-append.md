# How To: Set Index Append

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set index append

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

### Step 1: Assign df = frame_of_index_cols

```python
df = frame_of_index_cols
```

### Step 2: Assign keys = value

```python
keys = keys if isinstance(keys, list) else [keys]
```

### Step 3: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([df.index] + [df[x] for x in keys], names=[None] + keys)
```

### Step 4: Assign expected = value

```python
expected = df.drop(keys, axis=1) if drop else df.copy()
```

### Step 5: Assign expected.index = idx

```python
expected.index = idx
```

### Step 6: Assign result = df.set_index(...)

```python
result = df.set_index(keys, drop=drop, append=True)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_of_index_cols, drop, keys

# Workflow
df = frame_of_index_cols
keys = keys if isinstance(keys, list) else [keys]
idx = MultiIndex.from_arrays([df.index] + [df[x] for x in keys], names=[None] + keys)
expected = df.drop(keys, axis=1) if drop else df.copy()
expected.index = idx
result = df.set_index(keys, drop=drop, append=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_set_index.py:218 | Complexity: Intermediate | Last updated: 2026-06-02*