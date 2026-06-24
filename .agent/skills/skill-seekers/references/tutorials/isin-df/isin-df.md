# How To: Isin Df

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin df

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
df1 = DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]})
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A': [0, 2, 12, 4], 'B': [2, np.nan, 4, 5]})
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(False, df1.index, df1.columns)
```

### Step 4: Assign result = df1.isin(...)

```python
result = df1.isin(df2)
```

### Step 5: Assign unknown = True

```python
expected.loc[[1, 3], 'A'] = True
```

### Step 6: Assign unknown = True

```python
expected.loc[[0, 2], 'B'] = True
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign df2.columns = value

```python
df2.columns = ['A', 'C']
```

### Step 9: Assign result = df1.isin(...)

```python
result = df1.isin(df2)
```

### Step 10: Assign unknown = False

```python
expected['B'] = False
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'A': [1, 2, 3, 4], 'B': [2, np.nan, 4, 4]})
df2 = DataFrame({'A': [0, 2, 12, 4], 'B': [2, np.nan, 4, 5]})
expected = DataFrame(False, df1.index, df1.columns)
result = df1.isin(df2)
expected.loc[[1, 3], 'A'] = True
expected.loc[[0, 2], 'B'] = True
tm.assert_frame_equal(result, expected)
df2.columns = ['A', 'C']
result = df1.isin(df2)
expected['B'] = False
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:77 | Complexity: Advanced | Last updated: 2026-06-02*