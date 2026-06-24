# How To: Categorical Concat Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical concat dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign index = value

```python
index = ['cat', 'obj', 'num']
```

### Step 2: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c'])
```

### Step 3: Assign obj = Series(...)

```python
obj = Series(['a', 'b', 'c'])
```

### Step 4: Assign num = Series(...)

```python
num = Series([1, 2, 3])
```

### Step 5: Assign df = pd.concat(...)

```python
df = pd.concat([Series(cat), obj, num], axis=1, keys=index)
```

### Step 6: Assign result = value

```python
result = df.dtypes == (object if not using_infer_string else 'str')
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([False, True, False], index=index)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = df.dtypes == 'int64'
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([False, False, True], index=index)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign result = value

```python
result = df.dtypes == 'category'
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([True, False, False], index=index)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
index = ['cat', 'obj', 'num']
cat = Categorical(['a', 'b', 'c'])
obj = Series(['a', 'b', 'c'])
num = Series([1, 2, 3])
df = pd.concat([Series(cat), obj, num], axis=1, keys=index)
result = df.dtypes == (object if not using_infer_string else 'str')
expected = Series([False, True, False], index=index)
tm.assert_series_equal(result, expected)
result = df.dtypes == 'int64'
expected = Series([False, False, True], index=index)
tm.assert_series_equal(result, expected)
result = df.dtypes == 'category'
expected = Series([True, False, False], index=index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:54 | Complexity: Advanced | Last updated: 2026-06-02*