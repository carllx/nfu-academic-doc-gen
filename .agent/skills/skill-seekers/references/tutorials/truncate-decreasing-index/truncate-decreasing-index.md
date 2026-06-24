# How To: Truncate Decreasing Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test truncate decreasing index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: before, after, indices, dtyp, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([3, 2, 1, 0], dtype=dtyp)
```

### Step 2: Assign values = frame_or_series(...)

```python
values = frame_or_series(range(len(idx)), index=idx)
```

### Step 3: Assign result = values.truncate(...)

```python
result = values.truncate(before=before, after=after)
```

### Step 4: Assign expected = value

```python
expected = values.loc[indices]
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign before = value

```python
before = pd.Timestamp(before) if before is not None else None
```

### Step 7: Assign after = value

```python
after = pd.Timestamp(after) if after is not None else None
```

### Step 8: Assign indices = value

```python
indices = [pd.Timestamp(i) for i in indices]
```


## Complete Example

```python
# Setup
# Fixtures: before, after, indices, dtyp, frame_or_series

# Workflow
idx = Index([3, 2, 1, 0], dtype=dtyp)
if isinstance(idx, DatetimeIndex):
    before = pd.Timestamp(before) if before is not None else None
    after = pd.Timestamp(after) if after is not None else None
    indices = [pd.Timestamp(i) for i in indices]
values = frame_or_series(range(len(idx)), index=idx)
result = values.truncate(before=before, after=after)
expected = values.loc[indices]
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_truncate.py:116 | Complexity: Advanced | Last updated: 2026-06-02*