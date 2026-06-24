# How To: Join Left Sequence Non Unique Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join left sequence non unique index

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [0, 10, 20]}, index=[1, 2, 3])
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'b': [100, 200, 300]}, index=[4, 3, 2])
```

### Step 3: Assign df3 = DataFrame(...)

```python
df3 = DataFrame({'c': [400, 500, 600]}, index=[2, 2, 4])
```

### Step 4: Assign joined = df1.join(...)

```python
joined = df1.join([df2, df3], how='left')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [0, 10, 10, 20], 'b': [np.nan, 300, 300, 200], 'c': [np.nan, 400, 500, np.nan]}, index=[1, 2, 2, 3])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(joined, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'a': [0, 10, 20]}, index=[1, 2, 3])
df2 = DataFrame({'b': [100, 200, 300]}, index=[4, 3, 2])
df3 = DataFrame({'c': [400, 500, 600]}, index=[2, 2, 4])
joined = df1.join([df2, df3], how='left')
expected = DataFrame({'a': [0, 10, 10, 20], 'b': [np.nan, 300, 300, 200], 'c': [np.nan, 400, 500, np.nan]}, index=[1, 2, 2, 3])
tm.assert_frame_equal(joined, expected)
```

## Next Steps


---

*Source: test_join.py:365 | Complexity: Intermediate | Last updated: 2026-06-02*