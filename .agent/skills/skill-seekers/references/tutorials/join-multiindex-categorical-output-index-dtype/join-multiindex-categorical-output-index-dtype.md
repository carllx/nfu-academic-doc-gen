# How To: Join Multiindex Categorical Output Index Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join multiindex categorical output index dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: how, values
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame.set_index(...)

```python
df1 = DataFrame({'a': Categorical([0, 1, 2]), 'b': Categorical([0, 1, 2]), 'c': [0, 1, 2]}).set_index(['a', 'b'])
```

### Step 2: Assign df2 = DataFrame.set_index(...)

```python
df2 = DataFrame({'a': Categorical([0, 2, 1]), 'b': Categorical([0, 2, 1]), 'd': [0, 2, 1]}).set_index(['a', 'b'])
```

### Step 3: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'a': Categorical(values), 'b': Categorical(values), 'c': values, 'd': values}).set_index(['a', 'b'])
```

### Step 4: Assign result = df1.join(...)

```python
result = df1.join(df2, how=how)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: how, values

# Workflow
df1 = DataFrame({'a': Categorical([0, 1, 2]), 'b': Categorical([0, 1, 2]), 'c': [0, 1, 2]}).set_index(['a', 'b'])
df2 = DataFrame({'a': Categorical([0, 2, 1]), 'b': Categorical([0, 2, 1]), 'd': [0, 2, 1]}).set_index(['a', 'b'])
expected = DataFrame({'a': Categorical(values), 'b': Categorical(values), 'c': values, 'd': values}).set_index(['a', 'b'])
result = df1.join(df2, how=how)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:1079 | Complexity: Intermediate | Last updated: 2026-06-02*