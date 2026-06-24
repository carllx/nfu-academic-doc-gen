# How To: Append Length0 Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append length0 frame

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
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(columns=['A', 'B', 'C'])
```

### Step 2: Assign df3 = DataFrame(...)

```python
df3 = DataFrame(index=[0, 1], columns=['A', 'B'])
```

### Step 3: Assign df5 = df._append(...)

```python
df5 = df._append(df3, sort=sort)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(index=[0, 1], columns=['A', 'B', 'C'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df5, expected)
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
df = DataFrame(columns=['A', 'B', 'C'])
df3 = DataFrame(index=[0, 1], columns=['A', 'B'])
df5 = df._append(df3, sort=sort)
expected = DataFrame(index=[0, 1], columns=['A', 'B', 'C'])
tm.assert_frame_equal(df5, expected)
```

## Next Steps


---

*Source: test_append.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*