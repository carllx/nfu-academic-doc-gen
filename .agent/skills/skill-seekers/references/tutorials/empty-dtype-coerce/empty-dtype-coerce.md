# How To: Empty Dtype Coerce

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test empty dtype coerce

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
df1 = DataFrame(data=[[1, None], [2, None]], columns=['a', 'b'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(data=[[3, None], [4, None]], columns=['a', 'b'])
```

### Step 3: Assign result = concat(...)

```python
result = concat([df1, df2])
```

### Step 4: Assign expected = value

```python
expected = df1.dtypes
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result.dtypes, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(data=[[1, None], [2, None]], columns=['a', 'b'])
df2 = DataFrame(data=[[3, None], [4, None]], columns=['a', 'b'])
result = concat([df1, df2])
expected = df1.dtypes
tm.assert_series_equal(result.dtypes, expected)
```

## Next Steps


---

*Source: test_empty.py:257 | Complexity: Intermediate | Last updated: 2026-06-02*