# How To: Arith Reindex With Duplicates

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arith reindex with duplicates

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `enum`
- `functools`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(data=[[0]], columns=['second'])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(data=[[0, 0, 0]], columns=['first', 'second', 'second'])
```

### Step 3: Assign result = value

```python
result = df1 + df2
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[np.nan, 0, 0]], columns=['first', 'second', 'second'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(data=[[0]], columns=['second'])
df2 = DataFrame(data=[[0, 0, 0]], columns=['first', 'second', 'second'])
result = df1 + df2
expected = DataFrame([[np.nan, 0, 0]], columns=['first', 'second', 'second'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:2003 | Complexity: Intermediate | Last updated: 2026-06-02*