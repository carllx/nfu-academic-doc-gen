# How To: Series Groupby Value Counts No Sort

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series groupby value counts no sort

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'gender': ['male', 'male', 'female', 'male', 'female', 'male'], 'education': ['low', 'medium', 'high', 'low', 'high', 'low'], 'country': ['US', 'FR', 'US', 'FR', 'FR', 'FR']})
```

### Step 2: Assign gb = value

```python
gb = df.groupby(['country', 'gender'], sort=False)['education']
```

### Step 3: Assign result = gb.value_counts(...)

```python
result = gb.value_counts(sort=False)
```

### Step 4: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[['US', 'FR'], ['male', 'female'], ['low', 'medium', 'high']], codes=[[0, 1, 0, 1, 1], [0, 0, 1, 0, 1], [0, 1, 2, 0, 2]], names=['country', 'gender', 'education'])
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([1, 1, 1, 2, 1], index=index, name='count')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'gender': ['male', 'male', 'female', 'male', 'female', 'male'], 'education': ['low', 'medium', 'high', 'low', 'high', 'low'], 'country': ['US', 'FR', 'US', 'FR', 'FR', 'FR']})
gb = df.groupby(['country', 'gender'], sort=False)['education']
result = gb.value_counts(sort=False)
index = MultiIndex(levels=[['US', 'FR'], ['male', 'female'], ['low', 'medium', 'high']], codes=[[0, 1, 0, 1, 1], [0, 0, 1, 0, 1], [0, 1, 2, 0, 2]], names=['country', 'gender', 'education'])
expected = Series([1, 1, 1, 2, 1], index=index, name='count')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:205 | Complexity: Advanced | Last updated: 2026-06-02*