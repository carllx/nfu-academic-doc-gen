# How To: Concat Empty Dataframe

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat empty dataframe

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(columns=['a', 'b'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(columns=['b', 'c'])
```

### Step 3: Assign result = concat(...)

```python
result = concat([df1, df2, df1])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign df3 = DataFrame(...)

```python
df3 = DataFrame(columns=['a', 'b'])
```

### Step 7: Assign df4 = DataFrame(...)

```python
df4 = DataFrame(columns=['b'])
```

### Step 8: Assign result = concat(...)

```python
result = concat([df3, df4])
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['a', 'b'])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(columns=['a', 'b'])
df2 = DataFrame(columns=['b', 'c'])
result = concat([df1, df2, df1])
expected = DataFrame(columns=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
df3 = DataFrame(columns=['a', 'b'])
df4 = DataFrame(columns=['b'])
result = concat([df3, df4])
expected = DataFrame(columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_empty.py:270 | Complexity: Advanced | Last updated: 2026-06-02*