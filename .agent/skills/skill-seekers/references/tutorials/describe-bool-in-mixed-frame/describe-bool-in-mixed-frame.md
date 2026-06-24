# How To: Describe Bool In Mixed Frame

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe bool in mixed frame

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'string_data': ['a', 'b', 'c', 'd', 'e'], 'bool_data': [True, True, False, False, False], 'int_data': [10, 20, 30, 40, 50]})
```

### Step 2: Assign result = df.describe(...)

```python
result = df.describe()
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'int_data': [5, 30, df.int_data.std(), 10, 20, 30, 40, 50]}, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.describe(...)

```python
result = df.describe(include=['bool'])
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'bool_data': [5, 2, False, 3]}, index=['count', 'unique', 'top', 'freq'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'string_data': ['a', 'b', 'c', 'd', 'e'], 'bool_data': [True, True, False, False, False], 'int_data': [10, 20, 30, 40, 50]})
result = df.describe()
expected = DataFrame({'int_data': [5, 30, df.int_data.std(), 10, 20, 30, 40, 50]}, index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
tm.assert_frame_equal(result, expected)
result = df.describe(include=['bool'])
expected = DataFrame({'bool_data': [5, 2, False, 3]}, index=['count', 'unique', 'top', 'freq'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:16 | Complexity: Intermediate | Last updated: 2026-06-02*