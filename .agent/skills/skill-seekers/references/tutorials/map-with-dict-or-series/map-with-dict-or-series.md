# How To: Map With Dict Or Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map with dict or series

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign orig_values = value

```python
orig_values = ['a', 'B', 1, 'a']
```

### Step 2: Assign new_values = value

```python
new_values = ['one', 2, 3.0, 'one']
```

### Step 3: Assign cur_index = CategoricalIndex(...)

```python
cur_index = CategoricalIndex(orig_values, name='XXX')
```

### Step 4: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(new_values, name='XXX', categories=[3.0, 2, 'one'])
```

### Step 5: Assign mapper = Series(...)

```python
mapper = Series(new_values[:-1], index=orig_values[:-1])
```

### Step 6: Assign result = cur_index.map(...)

```python
result = cur_index.map(mapper)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign mapper = dict(...)

```python
mapper = dict(zip(orig_values[:-1], new_values[:-1]))
```

### Step 9: Assign result = cur_index.map(...)

```python
result = cur_index.map(mapper)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
orig_values = ['a', 'B', 1, 'a']
new_values = ['one', 2, 3.0, 'one']
cur_index = CategoricalIndex(orig_values, name='XXX')
expected = CategoricalIndex(new_values, name='XXX', categories=[3.0, 2, 'one'])
mapper = Series(new_values[:-1], index=orig_values[:-1])
result = cur_index.map(mapper)
tm.assert_index_equal(result, expected)
mapper = dict(zip(orig_values[:-1], new_values[:-1]))
result = cur_index.map(mapper)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_map.py:130 | Complexity: Advanced | Last updated: 2026-06-02*