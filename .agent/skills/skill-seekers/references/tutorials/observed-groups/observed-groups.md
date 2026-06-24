# How To: Observed Groups

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test observed groups

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

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'c', 'a'], categories=['a', 'b', 'c'])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'cat': cat, 'vals': [1, 2, 3]})
```

### Step 3: Assign g = df.groupby(...)

```python
g = df.groupby('cat', observed=observed)
```

### Step 4: Assign result = value

```python
result = g.groups
```

### Step 5: Call tm.assert_dict_equal()

```python
tm.assert_dict_equal(result, expected)
```

### Step 6: Assign expected = value

```python
expected = {'a': Index([0, 2], dtype='int64'), 'c': Index([1], dtype='int64')}
```

### Step 7: Assign expected = value

```python
expected = {'a': Index([0, 2], dtype='int64'), 'b': Index([], dtype='int64'), 'c': Index([1], dtype='int64')}
```


## Complete Example

```python
# Setup
# Fixtures: observed

# Workflow
cat = Categorical(['a', 'c', 'a'], categories=['a', 'b', 'c'])
df = DataFrame({'cat': cat, 'vals': [1, 2, 3]})
g = df.groupby('cat', observed=observed)
result = g.groups
if observed:
    expected = {'a': Index([0, 2], dtype='int64'), 'c': Index([1], dtype='int64')}
else:
    expected = {'a': Index([0, 2], dtype='int64'), 'b': Index([], dtype='int64'), 'c': Index([1], dtype='int64')}
tm.assert_dict_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:509 | Complexity: Intermediate | Last updated: 2026-06-02*