# How To: Concat Inner Join Empty

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat inner join empty

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df_empty = DataFrame(...)

```python
df_empty = DataFrame()
```

### Step 2: Assign df_a = DataFrame(...)

```python
df_a = DataFrame({'a': [1, 2]}, index=[0, 1], dtype='int64')
```

### Step 3: Assign df_expected = DataFrame(...)

```python
df_expected = DataFrame({'a': []}, index=RangeIndex(0), dtype='int64')
```

### Step 4: Assign result = concat(...)

```python
result = concat([df_a, df_empty], axis=1, join='inner')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df_expected)
```

### Step 6: Assign result = concat(...)

```python
result = concat([df_a, df_empty], axis=1, join='outer')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df_a)
```


## Complete Example

```python
# Workflow
df_empty = DataFrame()
df_a = DataFrame({'a': [1, 2]}, index=[0, 1], dtype='int64')
df_expected = DataFrame({'a': []}, index=RangeIndex(0), dtype='int64')
result = concat([df_a, df_empty], axis=1, join='inner')
tm.assert_frame_equal(result, df_expected)
result = concat([df_a, df_empty], axis=1, join='outer')
tm.assert_frame_equal(result, df_a)
```

## Next Steps


---

*Source: test_empty.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*