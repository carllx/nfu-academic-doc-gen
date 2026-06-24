# How To: Pivot Table Dropna Categoricals

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot table dropna categoricals

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`

**Setup Required:**
```python
# Fixtures: dropna
```

## Step-by-Step Guide

### Step 1: Assign categories = value

```python
categories = ['a', 'b', 'c', 'd']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], 'B': [1, 2, 3, 1, 2, 3, 1, 2, 3], 'C': range(9)})
```

### Step 3: Assign unknown = unknown.astype(...)

```python
df['A'] = df['A'].astype(CategoricalDtype(categories, ordered=False))
```

### Step 4: Assign msg = 'The default value of observed=False is deprecated'

```python
msg = 'The default value of observed=False is deprecated'
```

### Step 5: Assign expected_columns = Series(...)

```python
expected_columns = Series(['a', 'b', 'c'], name='A')
```

### Step 6: Assign expected_columns = expected_columns.astype(...)

```python
expected_columns = expected_columns.astype(CategoricalDtype(categories, ordered=False))
```

### Step 7: Assign expected_index = Series(...)

```python
expected_index = Series([1, 2, 3], name='B')
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0.0, 3.0, 6.0], [1.0, 4.0, 7.0], [2.0, 5.0, 8.0]], index=expected_index, columns=expected_columns)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = df.pivot_table(...)

```python
result = df.pivot_table(index='B', columns='A', values='C', dropna=dropna)
```

### Step 11: Assign expected = expected.reindex.astype(...)

```python
expected = expected.reindex(columns=Categorical(categories)).astype('float')
```


## Complete Example

```python
# Setup
# Fixtures: dropna

# Workflow
categories = ['a', 'b', 'c', 'd']
df = DataFrame({'A': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], 'B': [1, 2, 3, 1, 2, 3, 1, 2, 3], 'C': range(9)})
df['A'] = df['A'].astype(CategoricalDtype(categories, ordered=False))
msg = 'The default value of observed=False is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.pivot_table(index='B', columns='A', values='C', dropna=dropna)
expected_columns = Series(['a', 'b', 'c'], name='A')
expected_columns = expected_columns.astype(CategoricalDtype(categories, ordered=False))
expected_index = Series([1, 2, 3], name='B')
expected = DataFrame([[0.0, 3.0, 6.0], [1.0, 4.0, 7.0], [2.0, 5.0, 8.0]], index=expected_index, columns=expected_columns)
if not dropna:
    expected = expected.reindex(columns=Categorical(categories)).astype('float')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot.py:214 | Complexity: Advanced | Last updated: 2026-06-02*