# How To: Getitem Str Slice Millisecond Resolution

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem str slice millisecond resolution

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign keys = value

```python
keys = ['2017-10-25T16:25:04.151', '2017-10-25T16:25:04.252', '2017-10-25T16:50:05.237', '2017-10-25T16:50:05.238']
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series([1, 2, 3, 4], index=[Timestamp(x) for x in keys])
```

### Step 3: Assign result = value

```python
result = obj[keys[1]:keys[2]]
```

### Step 4: Assign expected = frame_or_series(...)

```python
expected = frame_or_series([2, 3], index=[Timestamp(keys[1]), Timestamp(keys[2])])
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
keys = ['2017-10-25T16:25:04.151', '2017-10-25T16:25:04.252', '2017-10-25T16:50:05.237', '2017-10-25T16:50:05.238']
obj = frame_or_series([1, 2, 3, 4], index=[Timestamp(x) for x in keys])
result = obj[keys[1]:keys[2]]
expected = frame_or_series([2, 3], index=[Timestamp(keys[1]), Timestamp(keys[2])])
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*