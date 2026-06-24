# How To: Concat Bool With Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat bool with int

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(Series([True, False, True, True], dtype='bool'))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(Series([1, 0, 1], dtype='int64'))
```

### Step 3: Assign result = concat(...)

```python
result = concat([df1, df2])
```

### Step 4: Assign expected = concat(...)

```python
expected = concat([df1.astype('int64'), df2])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(Series([True, False, True, True], dtype='bool'))
df2 = DataFrame(Series([1, 0, 1], dtype='int64'))
result = concat([df1, df2])
expected = concat([df1.astype('int64'), df2])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dataframe.py:173 | Complexity: Intermediate | Last updated: 2026-06-02*