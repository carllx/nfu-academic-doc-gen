# How To: Describe Categorical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe categorical

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
df = DataFrame({'value': np.random.default_rng(2).integers(0, 10000, 100)})
```

**Verification:**
```python
assert len(result.columns) == 1
```

### Step 2: Assign labels = value

```python
labels = [f'{i} - {i + 499}' for i in range(0, 10000, 500)]
```

### Step 3: Assign cat_labels = Categorical(...)

```python
cat_labels = Categorical(labels, labels)
```

### Step 4: Assign df = df.sort_values(...)

```python
df = df.sort_values(by=['value'], ascending=True)
```

### Step 5: Assign unknown = pd.cut(...)

```python
df['value_group'] = pd.cut(df.value, range(0, 10500, 500), right=False, labels=cat_labels)
```

### Step 6: Assign cat = df

```python
cat = df
```

### Step 7: Assign result = cat.describe(...)

```python
result = cat.describe()
```

**Verification:**
```python
assert len(result.columns) == 1
```

### Step 8: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'b', 'b'], categories=['a', 'b', 'c'], ordered=True)
```

### Step 9: Assign s = Series(...)

```python
s = Series(cat)
```

### Step 10: Assign result = s.describe(...)

```python
result = s.describe()
```

### Step 11: Assign expected = Series(...)

```python
expected = Series([4, 2, 'b', 3], index=['count', 'unique', 'top', 'freq'])
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 13: Assign cat = Series(...)

```python
cat = Series(Categorical(['a', 'b', 'c', 'c']))
```

### Step 14: Assign df3 = DataFrame(...)

```python
df3 = DataFrame({'cat': cat, 's': ['a', 'b', 'c', 'c']})
```

### Step 15: Assign result = df3.describe(...)

```python
result = df3.describe()
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result['cat'].values, result['s'].values)
```


## Complete Example

```python
# Workflow
df = DataFrame({'value': np.random.default_rng(2).integers(0, 10000, 100)})
labels = [f'{i} - {i + 499}' for i in range(0, 10000, 500)]
cat_labels = Categorical(labels, labels)
df = df.sort_values(by=['value'], ascending=True)
df['value_group'] = pd.cut(df.value, range(0, 10500, 500), right=False, labels=cat_labels)
cat = df
result = cat.describe()
assert len(result.columns) == 1
cat = Categorical(['a', 'b', 'b', 'b'], categories=['a', 'b', 'c'], ordered=True)
s = Series(cat)
result = s.describe()
expected = Series([4, 2, 'b', 3], index=['count', 'unique', 'top', 'freq'])
tm.assert_series_equal(result, expected)
cat = Series(Categorical(['a', 'b', 'c', 'c']))
df3 = DataFrame({'cat': cat, 's': ['a', 'b', 'c', 'c']})
result = df3.describe()
tm.assert_numpy_array_equal(result['cat'].values, result['s'].values)
```

## Next Steps


---

*Source: test_describe.py:94 | Complexity: Advanced | Last updated: 2026-06-02*