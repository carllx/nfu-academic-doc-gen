# How To: Categoricals

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categoricals

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: a_dtype, b_dtype
```

## Step-by-Step Guide

### Step 1: Assign g = np.random.default_rng(...)

```python
g = np.random.default_rng(2)
```

**Verification:**
```python
assert not a_is_cat or a.value_counts().loc[1] == 0
```

### Step 2: Assign a = Series.astype(...)

```python
a = Series(g.integers(0, 3, size=100)).astype(a_dtype)
```

### Step 3: Assign b = Series.astype(...)

```python
b = Series(g.integers(0, 2, size=100)).astype(b_dtype)
```

### Step 4: Assign result = crosstab(...)

```python
result = crosstab(a, b, margins=True, dropna=False)
```

### Step 5: Assign columns = Index(...)

```python
columns = Index([0, 1, 'All'], dtype='object', name='col_0')
```

### Step 6: Assign index = Index(...)

```python
index = Index([0, 1, 2, 'All'], dtype='object', name='row_0')
```

### Step 7: Assign values = value

```python
values = [[10, 18, 28], [23, 16, 39], [17, 16, 33], [50, 50, 100]]
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(values, index, columns)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign unknown = 2

```python
a.loc[a == 1] = 2
```

### Step 11: Assign a_is_cat = isinstance(...)

```python
a_is_cat = isinstance(a.dtype, CategoricalDtype)
```

**Verification:**
```python
assert not a_is_cat or a.value_counts().loc[1] == 0
```

### Step 12: Assign result = crosstab(...)

```python
result = crosstab(a, b, margins=True, dropna=False)
```

### Step 13: Assign values = value

```python
values = [[10, 18, 28], [0, 0, 0], [40, 32, 72], [50, 50, 100]]
```

### Step 14: Assign expected = DataFrame(...)

```python
expected = DataFrame(values, index, columns)
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign expected = value

```python
expected = expected.loc[[0, 2, 'All']]
```

### Step 17: Assign unknown = unknown.astype(...)

```python
expected['All'] = expected['All'].astype('int64')
```


## Complete Example

```python
# Setup
# Fixtures: a_dtype, b_dtype

# Workflow
g = np.random.default_rng(2)
a = Series(g.integers(0, 3, size=100)).astype(a_dtype)
b = Series(g.integers(0, 2, size=100)).astype(b_dtype)
result = crosstab(a, b, margins=True, dropna=False)
columns = Index([0, 1, 'All'], dtype='object', name='col_0')
index = Index([0, 1, 2, 'All'], dtype='object', name='row_0')
values = [[10, 18, 28], [23, 16, 39], [17, 16, 33], [50, 50, 100]]
expected = DataFrame(values, index, columns)
tm.assert_frame_equal(result, expected)
a.loc[a == 1] = 2
a_is_cat = isinstance(a.dtype, CategoricalDtype)
assert not a_is_cat or a.value_counts().loc[1] == 0
result = crosstab(a, b, margins=True, dropna=False)
values = [[10, 18, 28], [0, 0, 0], [40, 32, 72], [50, 50, 100]]
expected = DataFrame(values, index, columns)
if not a_is_cat:
    expected = expected.loc[[0, 2, 'All']]
    expected['All'] = expected['All'].astype('int64')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_crosstab.py:864 | Complexity: Advanced | Last updated: 2026-06-02*