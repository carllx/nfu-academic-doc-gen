# How To: Insert Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test insert nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz, null
```

## Step-by-Step Guide

### Step 1: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(['2017-01-01'], tz=tz)
```

### Step 2: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['NaT', '2017-01-01'], tz=tz)
```

### Step 3: Assign res = idx.insert(...)

```python
res = idx.insert(0, null)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, expected)
```

### Step 5: Assign expected = Index(...)

```python
expected = Index([null, idx[0]], dtype=object)
```


## Complete Example

```python
# Setup
# Fixtures: tz, null

# Workflow
idx = DatetimeIndex(['2017-01-01'], tz=tz)
expected = DatetimeIndex(['NaT', '2017-01-01'], tz=tz)
if tz is not None and isinstance(null, np.datetime64):
    expected = Index([null, idx[0]], dtype=object)
res = idx.insert(0, null)
tm.assert_index_equal(res, expected)
```

## Next Steps


---

*Source: test_insert.py:21 | Complexity: Intermediate | Last updated: 2026-06-02*