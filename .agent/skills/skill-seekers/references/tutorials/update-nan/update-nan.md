# How To: Update Nan

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test update nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': [1.0, 2, 3], 'B': date_range('2000', periods=3)})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [None, 2, 3]})
```

### Step 3: Assign expected = df1.copy(...)

```python
expected = df1.copy()
```

### Step 4: Call df1.update()

```python
df1.update(df2, overwrite=False)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, expected)
```

### Step 6: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'A': [1.0, None, 3], 'B': date_range('2000', periods=3)})
```

### Step 7: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [None, 2, 3]})
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1.0, 2, 3], 'B': date_range('2000', periods=3)})
```

### Step 9: Call df1.update()

```python
df1.update(df2, overwrite=False)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'A': [1.0, 2, 3], 'B': date_range('2000', periods=3)})
df2 = DataFrame({'A': [None, 2, 3]})
expected = df1.copy()
df1.update(df2, overwrite=False)
tm.assert_frame_equal(df1, expected)
df1 = DataFrame({'A': [1.0, None, 3], 'B': date_range('2000', periods=3)})
df2 = DataFrame({'A': [None, 2, 3]})
expected = DataFrame({'A': [1.0, 2, 3], 'B': date_range('2000', periods=3)})
df1.update(df2, overwrite=False)
tm.assert_frame_equal(df1, expected)
```

## Next Steps


---

*Source: test_update.py:16 | Complexity: Advanced | Last updated: 2026-06-02*