# How To: Sorting With Different Categoricals

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sorting with different categoricals

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.typing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'group': ['A'] * 6 + ['B'] * 6, 'dose': ['high', 'med', 'low'] * 4, 'outcomes': np.arange(12.0)})
```

### Step 2: Assign df.dose = Categorical(...)

```python
df.dose = Categorical(df.dose, categories=['low', 'med', 'high'], ordered=True)
```

### Step 3: Assign result = unknown.value_counts(...)

```python
result = df.groupby('group')['dose'].value_counts()
```

### Step 4: Assign result = result.sort_index(...)

```python
result = result.sort_index(level=0, sort_remaining=True)
```

### Step 5: Assign index = value

```python
index = ['low', 'med', 'high', 'low', 'med', 'high']
```

### Step 6: Assign index = Categorical(...)

```python
index = Categorical(index, categories=['low', 'med', 'high'], ordered=True)
```

### Step 7: Assign index = value

```python
index = [['A', 'A', 'A', 'B', 'B', 'B'], CategoricalIndex(index)]
```

### Step 8: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(index, names=['group', 'dose'])
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([2] * 6, index=index, name='count')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'group': ['A'] * 6 + ['B'] * 6, 'dose': ['high', 'med', 'low'] * 4, 'outcomes': np.arange(12.0)})
df.dose = Categorical(df.dose, categories=['low', 'med', 'high'], ordered=True)
result = df.groupby('group')['dose'].value_counts()
result = result.sort_index(level=0, sort_remaining=True)
index = ['low', 'med', 'high', 'low', 'med', 'high']
index = Categorical(index, categories=['low', 'med', 'high'], ordered=True)
index = [['A', 'A', 'A', 'B', 'B', 'B'], CategoricalIndex(index)]
index = MultiIndex.from_arrays(index, names=['group', 'dose'])
expected = Series([2] * 6, index=index, name='count')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:291 | Complexity: Advanced | Last updated: 2026-06-02*