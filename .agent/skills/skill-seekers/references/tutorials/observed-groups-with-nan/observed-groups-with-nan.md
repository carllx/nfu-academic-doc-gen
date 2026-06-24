# How To: Observed Groups With Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test observed groups with nan

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
# Fixtures: observed
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'cat': Categorical(['a', np.nan, 'a'], categories=['a', 'b', 'd']), 'vals': [1, 2, 3]})
```

### Step 2: Assign g = df.groupby(...)

```python
g = df.groupby('cat', observed=observed)
```

### Step 3: Assign result = value

```python
result = g.groups
```

### Step 4: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(result, expected)
```

### Step 5: Assign expected = value

```python
expected = {'a': Index([0, 2], dtype='int64')}
```

### Step 6: Assign expected = value

```python
expected = {'a': Index([0, 2], dtype='int64'), 'b': Index([], dtype='int64'), 'd': Index([], dtype='int64')}
```


## Complete Example

```python
# Setup
# Fixtures: observed

# Workflow
df = DataFrame({'cat': Categorical(['a', np.nan, 'a'], categories=['a', 'b', 'd']), 'vals': [1, 2, 3]})
g = df.groupby('cat', observed=observed)
result = g.groups
if observed:
    expected = {'a': Index([0, 2], dtype='int64')}
else:
    expected = {'a': Index([0, 2], dtype='int64'), 'b': Index([], dtype='int64'), 'd': Index([], dtype='int64')}
tm.assert_dict_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:584 | Complexity: Intermediate | Last updated: 2026-06-02*