# How To: Slicing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slicing

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = Series(...)

```python
cat = Series(Categorical([1, 2, 3, 4]))
```

### Step 2: Assign reverse = value

```python
reverse = cat[::-1]
```

### Step 3: Assign exp = np.array(...)

```python
exp = np.array([4, 3, 2, 1], dtype=np.int64)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(reverse.__array__(), exp)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'value': (np.arange(100) + 1).astype('int64')})
```

### Step 6: Assign unknown = pd.cut(...)

```python
df['D'] = pd.cut(df.value, bins=[0, 25, 50, 75, 100])
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([11, Interval(0, 25)], index=['value', 'D'], name=10)
```

### Step 8: Assign result = value

```python
result = df.iloc[10]
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': np.arange(11, 21).astype('int64')}, index=np.arange(10, 20).astype('int64'))
```

### Step 11: Assign unknown = pd.cut(...)

```python
expected['D'] = pd.cut(expected.value, bins=[0, 25, 50, 75, 100])
```

### Step 12: Assign result = value

```python
result = df.iloc[10:20]
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign expected = Series(...)

```python
expected = Series([9, Interval(0, 25)], index=['value', 'D'], name=8)
```

### Step 15: Assign result = value

```python
result = df.loc[8]
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
cat = Series(Categorical([1, 2, 3, 4]))
reverse = cat[::-1]
exp = np.array([4, 3, 2, 1], dtype=np.int64)
tm.assert_numpy_array_equal(reverse.__array__(), exp)
df = DataFrame({'value': (np.arange(100) + 1).astype('int64')})
df['D'] = pd.cut(df.value, bins=[0, 25, 50, 75, 100])
expected = Series([11, Interval(0, 25)], index=['value', 'D'], name=10)
result = df.iloc[10]
tm.assert_series_equal(result, expected)
expected = DataFrame({'value': np.arange(11, 21).astype('int64')}, index=np.arange(10, 20).astype('int64'))
expected['D'] = pd.cut(expected.value, bins=[0, 25, 50, 75, 100])
result = df.iloc[10:20]
tm.assert_frame_equal(result, expected)
expected = Series([9, Interval(0, 25)], index=['value', 'D'], name=8)
result = df.loc[8]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:113 | Complexity: Advanced | Last updated: 2026-06-02*