# How To: Drop Duplicates With Duplicate Column Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop duplicates with duplicate column names

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 5], [3, 4, 6], [3, 4, 7]], columns=['a', 'a', 'b'])
```

### Step 2: Assign result0 = df.drop_duplicates(...)

```python
result0 = df.drop_duplicates()
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result0, df)
```

### Step 4: Assign result1 = df.drop_duplicates(...)

```python
result1 = df.drop_duplicates('a')
```

### Step 5: Assign expected1 = value

```python
expected1 = df[:2]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result1, expected1)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 5], [3, 4, 6], [3, 4, 7]], columns=['a', 'a', 'b'])
result0 = df.drop_duplicates()
tm.assert_frame_equal(result0, df)
result1 = df.drop_duplicates('a')
expected1 = df[:2]
tm.assert_frame_equal(result1, expected1)
```

## Next Steps


---

*Source: test_drop_duplicates.py:121 | Complexity: Intermediate | Last updated: 2026-06-02*