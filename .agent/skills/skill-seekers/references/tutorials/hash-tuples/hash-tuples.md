# How To: Hash Tuples

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hash tuples

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.util.hashing`
- `pandas.util`


## Step-by-Step Guide

### Step 1: Assign tuples = value

```python
tuples = [(1, 'one'), (1, 'two'), (2, 'one')]
```

### Step 2: Assign result = hash_tuples(...)

```python
result = hash_tuples(tuples)
```

### Step 3: Assign expected = value

```python
expected = hash_pandas_object(MultiIndex.from_tuples(tuples)).values
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign msg = unknown.join(...)

```python
msg = '|'.join(['object is not iterable', 'zip argument #1 must support iteration'])
```

### Step 6: Call hash_tuples()

```python
hash_tuples(tuples[0])
```


## Complete Example

```python
# Workflow
tuples = [(1, 'one'), (1, 'two'), (2, 'one')]
result = hash_tuples(tuples)
expected = hash_pandas_object(MultiIndex.from_tuples(tuples)).values
tm.assert_numpy_array_equal(result, expected)
msg = '|'.join(['object is not iterable', 'zip argument #1 must support iteration'])
with pytest.raises(TypeError, match=msg):
    hash_tuples(tuples[0])
```

## Next Steps


---

*Source: test_hashing.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*