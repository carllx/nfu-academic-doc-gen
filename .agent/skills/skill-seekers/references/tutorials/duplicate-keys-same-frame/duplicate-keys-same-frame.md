# How To: Duplicate Keys Same Frame

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicate keys same frame

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign keys = value

```python
keys = ['e', 'e']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

### Step 3: Assign result = concat(...)

```python
result = concat([df, df], axis=1, keys=keys)
```

### Step 4: Assign expected_values = value

```python
expected_values = [[1, 4, 1, 4], [2, 5, 2, 5], [3, 6, 3, 6]]
```

### Step 5: Assign expected_columns = MultiIndex.from_tuples(...)

```python
expected_columns = MultiIndex.from_tuples([(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'a'), (keys[1], 'b')])
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_values, columns=expected_columns)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
keys = ['e', 'e']
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
result = concat([df, df], axis=1, keys=keys)
expected_values = [[1, 4, 1, 4], [2, 5, 2, 5], [3, 6, 3, 6]]
expected_columns = MultiIndex.from_tuples([(keys[0], 'a'), (keys[0], 'b'), (keys[1], 'a'), (keys[1], 'b')])
expected = DataFrame(expected_values, columns=expected_columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:615 | Complexity: Intermediate | Last updated: 2026-06-02*