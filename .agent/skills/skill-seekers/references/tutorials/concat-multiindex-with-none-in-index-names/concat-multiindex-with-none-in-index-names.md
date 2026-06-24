# How To: Concat Multiindex With None In Index Names

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat multiindex with none in index names

## Prerequisites

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([[1], range(5)], names=['level1', None])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'col': range(5)}, index=index, dtype=np.int32)
```

### Step 3: Assign result = concat(...)

```python
result = concat([df, df], keys=[1, 2], names=['level2'])
```

### Step 4: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([[1, 2], [1], range(5)], names=['level2', 'level1', None])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col': list(range(5)) * 2}, index=index, dtype=np.int32)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = concat(...)

```python
result = concat([df, df[:2]], keys=[1, 2], names=['level2'])
```

### Step 8: Assign level2 = value

```python
level2 = [1] * 5 + [2] * 2
```

### Step 9: Assign level1 = value

```python
level1 = [1] * 7
```

### Step 10: Assign no_name = value

```python
no_name = list(range(5)) + list(range(2))
```

### Step 11: Assign tuples = list(...)

```python
tuples = list(zip(level2, level1, no_name))
```

### Step 12: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples, names=['level2', 'level1', None])
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame({'col': no_name}, index=index, dtype=np.int32)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
index = MultiIndex.from_product([[1], range(5)], names=['level1', None])
df = DataFrame({'col': range(5)}, index=index, dtype=np.int32)
result = concat([df, df], keys=[1, 2], names=['level2'])
index = MultiIndex.from_product([[1, 2], [1], range(5)], names=['level2', 'level1', None])
expected = DataFrame({'col': list(range(5)) * 2}, index=index, dtype=np.int32)
tm.assert_frame_equal(result, expected)
result = concat([df, df[:2]], keys=[1, 2], names=['level2'])
level2 = [1] * 5 + [2] * 2
level1 = [1] * 7
no_name = list(range(5)) + list(range(2))
tuples = list(zip(level2, level1, no_name))
index = MultiIndex.from_tuples(tuples, names=['level2', 'level1', None])
expected = DataFrame({'col': no_name}, index=index, dtype=np.int32)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_index.py:221 | Complexity: Advanced | Last updated: 2026-06-02*