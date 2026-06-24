# How To: Selection Methods Of Assigned Col

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test selection methods of assigned col

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(data={'a': [1, 2, 3], 'b': [4, 5, 6]})
```

**Verification:**
```python
assert result == 11
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(data={'c': [7, 8, 9]}, index=[2, 1, 0])
```

### Step 3: Assign unknown = value

```python
df['c'] = df2['c']
```

### Step 4: Assign unknown = 11

```python
df.at[1, 'c'] = 11
```

### Step 5: Assign result = df

```python
result = df
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [9, 11, 7]})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df.at[1, 'c']
```

**Verification:**
```python
assert result == 11
```

### Step 9: Assign result = value

```python
result = df['c']
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([9, 11, 7], name='c')
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign result = value

```python
result = df[['c']]
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame({'c': [9, 11, 7]})
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(data={'a': [1, 2, 3], 'b': [4, 5, 6]})
df2 = DataFrame(data={'c': [7, 8, 9]}, index=[2, 1, 0])
df['c'] = df2['c']
df.at[1, 'c'] = 11
result = df
expected = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [9, 11, 7]})
tm.assert_frame_equal(result, expected)
result = df.at[1, 'c']
assert result == 11
result = df['c']
expected = Series([9, 11, 7], name='c')
tm.assert_series_equal(result, expected)
result = df[['c']]
expected = DataFrame({'c': [9, 11, 7]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_at.py:34 | Complexity: Advanced | Last updated: 2026-06-02*