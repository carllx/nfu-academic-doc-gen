# How To: Duplicate Keys

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test duplicate keys

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`

**Setup Required:**
```python
# Fixtures: keys
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series([7, 8, 9], name='c')
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series([10, 11, 12], name='d')
```

### Step 4: Assign result = concat(...)

```python
result = concat([df, s1, s2], axis=1, keys=keys)
```

### Step 5: Assign expected_values = value

```python
expected_values = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
```

### Step 6: Assign expected_columns = MultiIndex.from_tuples(...)

```python
expected_columns = MultiIndex.from_tuples([(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_values, columns=expected_columns)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: keys

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
s1 = Series([7, 8, 9], name='c')
s2 = Series([10, 11, 12], name='d')
result = concat([df, s1, s2], axis=1, keys=keys)
expected_values = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
expected_columns = MultiIndex.from_tuples([(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'c'), (keys[2], 'd')])
expected = DataFrame(expected_values, columns=expected_columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:601 | Complexity: Advanced | Last updated: 2026-06-02*