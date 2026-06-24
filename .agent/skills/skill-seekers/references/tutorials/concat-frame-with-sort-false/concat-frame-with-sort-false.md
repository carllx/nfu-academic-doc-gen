# How To: Concat Frame With Sort False

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat frame with sort false

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = pd.concat(...)

```python
result = pd.concat([DataFrame({i: i}, index=[i]) for i in range(2, 0, -1)], sort=False)
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([[2, np.nan], [np.nan, 1]], index=[2, 1], columns=[2, 1])
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=[1, 2, 3])
```

### Step 5: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'c': [7, 8, 9], 'd': [10, 11, 12]}, index=[3, 1, 6])
```

### Step 6: Assign result = pd.concat(...)

```python
result = pd.concat([df2, df1], axis=1, sort=False)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[7.0, 10.0, 3.0, 6.0], [8.0, 11.0, 1.0, 4.0], [9.0, 12.0, np.nan, np.nan], [np.nan, np.nan, 2.0, 5.0]], index=[3, 1, 6, 2], columns=['c', 'd', 'a', 'b'])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
result = pd.concat([DataFrame({i: i}, index=[i]) for i in range(2, 0, -1)], sort=False)
expected = DataFrame([[2, np.nan], [np.nan, 1]], index=[2, 1], columns=[2, 1])
tm.assert_frame_equal(result, expected)
df1 = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=[1, 2, 3])
df2 = DataFrame({'c': [7, 8, 9], 'd': [10, 11, 12]}, index=[3, 1, 6])
result = pd.concat([df2, df1], axis=1, sort=False)
expected = DataFrame([[7.0, 10.0, 3.0, 6.0], [8.0, 11.0, 1.0, 4.0], [9.0, 12.0, np.nan, np.nan], [np.nan, np.nan, 2.0, 5.0]], index=[3, 1, 6, 2], columns=['c', 'd', 'a', 'b'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort.py:88 | Complexity: Advanced | Last updated: 2026-06-02*