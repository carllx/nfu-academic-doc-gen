# How To: Outer Sort Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test outer sort columns

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
df1 = DataFrame({'A': [0], 'B': [1], 0: 1})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [100]})
```

### Step 3: Assign result = concat(...)

```python
result = concat([df1, df2], ignore_index=True, join='outer', sort=True)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: [1.0, np.nan], 'A': [0, 100], 'B': [1.0, np.nan]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'A': [0], 'B': [1], 0: 1})
df2 = DataFrame({'A': [100]})
result = concat([df1, df2], ignore_index=True, join='outer', sort=True)
expected = DataFrame({0: [1.0, np.nan], 'A': [0, 100], 'B': [1.0, np.nan]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dataframe.py:209 | Complexity: Intermediate | Last updated: 2026-06-02*