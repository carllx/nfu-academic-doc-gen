# How To: Unobserved In Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unobserved in index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.typing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: keys, expected_values, expected_index_levels, test_series
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index(...)

```python
df = DataFrame({'a': Categorical([1, 1, 2], categories=[1, 2, 3]), 'a2': Categorical([1, 1, 2], categories=[1, 2, 3]), 'b': [4, 5, 6], 'c': [7, 8, 9]}).set_index(['a', 'a2'])
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby(keys, observed=False)
```

### Step 3: Assign result = gb.sum(...)

```python
result = gb.sum()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'c': expected_values}, index=index)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign df = df.drop(...)

```python
df = df.drop(columns='b')
```

### Step 7: Assign gb = value

```python
gb = gb['c']
```

### Step 8: Assign index = expected_index_levels

```python
index = expected_index_levels
```

### Step 9: Assign codes = value

```python
codes = [[0, 0, 0, 1, 1, 1, 2, 2, 2], 3 * [0, 1, 2]]
```

### Step 10: Assign index = MultiIndex(...)

```python
index = MultiIndex(expected_index_levels, codes=codes, names=keys)
```

### Step 11: Assign expected = value

```python
expected = expected['c']
```


## Complete Example

```python
# Setup
# Fixtures: keys, expected_values, expected_index_levels, test_series

# Workflow
df = DataFrame({'a': Categorical([1, 1, 2], categories=[1, 2, 3]), 'a2': Categorical([1, 1, 2], categories=[1, 2, 3]), 'b': [4, 5, 6], 'c': [7, 8, 9]}).set_index(['a', 'a2'])
if 'b' not in keys:
    df = df.drop(columns='b')
gb = df.groupby(keys, observed=False)
if test_series:
    gb = gb['c']
result = gb.sum()
if len(keys) == 1:
    index = expected_index_levels
else:
    codes = [[0, 0, 0, 1, 1, 1, 2, 2, 2], 3 * [0, 1, 2]]
    index = MultiIndex(expected_index_levels, codes=codes, names=keys)
expected = DataFrame({'c': expected_values}, index=index)
if test_series:
    expected = expected['c']
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:550 | Complexity: Advanced | Last updated: 2026-06-02*