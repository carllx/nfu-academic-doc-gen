# How To: Append Many

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append many

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort, float_frame
```

## Step-by-Step Guide

### Step 1: Assign chunks = value

```python
chunks = [float_frame[:5], float_frame[5:10], float_frame[10:15], float_frame[15:]]
```

**Verification:**
```python
assert (result['foo'][15:] == 'bar').all()
```

### Step 2: Assign result = unknown._append(...)

```python
result = chunks[0]._append(chunks[1:])
```

**Verification:**
```python
assert result['foo'][:15].isna().all()
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, float_frame)
```

### Step 4: Assign unknown = unknown.copy(...)

```python
chunks[-1] = chunks[-1].copy()
```

### Step 5: Assign unknown = 'bar'

```python
chunks[-1]['foo'] = 'bar'
```

### Step 6: Assign result = unknown._append(...)

```python
result = chunks[0]._append(chunks[1:], sort=sort)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.loc[:, float_frame.columns], float_frame)
```

**Verification:**
```python
assert (result['foo'][15:] == 'bar').all()
```


## Complete Example

```python
# Setup
# Fixtures: sort, float_frame

# Workflow
chunks = [float_frame[:5], float_frame[5:10], float_frame[10:15], float_frame[15:]]
result = chunks[0]._append(chunks[1:])
tm.assert_frame_equal(result, float_frame)
chunks[-1] = chunks[-1].copy()
chunks[-1]['foo'] = 'bar'
result = chunks[0]._append(chunks[1:], sort=sort)
tm.assert_frame_equal(result.loc[:, float_frame.columns], float_frame)
assert (result['foo'][15:] == 'bar').all()
assert result['foo'][:15].isna().all()
```

## Next Steps


---

*Source: test_append.py:140 | Complexity: Intermediate | Last updated: 2026-06-02*