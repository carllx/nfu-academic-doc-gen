# How To: Sort Values Multicolumn

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values multicolumn

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign A = np.arange.repeat(...)

```python
A = np.arange(5).repeat(20)
```

### Step 2: Assign B = np.tile(...)

```python
B = np.tile(np.arange(5), 20)
```

### Step 3: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(A)
```

### Step 4: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(B)
```

### Step 5: Assign frame = DataFrame(...)

```python
frame = DataFrame({'A': A, 'B': B, 'C': np.random.default_rng(2).standard_normal(100)})
```

### Step 6: Assign result = frame.sort_values(...)

```python
result = frame.sort_values(by=['A', 'B'])
```

### Step 7: Assign indexer = np.lexsort(...)

```python
indexer = np.lexsort((frame['B'], frame['A']))
```

### Step 8: Assign expected = frame.take(...)

```python
expected = frame.take(indexer)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = frame.sort_values(...)

```python
result = frame.sort_values(by=['A', 'B'], ascending=False)
```

### Step 11: Assign indexer = np.lexsort(...)

```python
indexer = np.lexsort((frame['B'].rank(ascending=False), frame['A'].rank(ascending=False)))
```

### Step 12: Assign expected = frame.take(...)

```python
expected = frame.take(indexer)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign result = frame.sort_values(...)

```python
result = frame.sort_values(by=['B', 'A'])
```

### Step 15: Assign indexer = np.lexsort(...)

```python
indexer = np.lexsort((frame['A'], frame['B']))
```

### Step 16: Assign expected = frame.take(...)

```python
expected = frame.take(indexer)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
A = np.arange(5).repeat(20)
B = np.tile(np.arange(5), 20)
np.random.default_rng(2).shuffle(A)
np.random.default_rng(2).shuffle(B)
frame = DataFrame({'A': A, 'B': B, 'C': np.random.default_rng(2).standard_normal(100)})
result = frame.sort_values(by=['A', 'B'])
indexer = np.lexsort((frame['B'], frame['A']))
expected = frame.take(indexer)
tm.assert_frame_equal(result, expected)
result = frame.sort_values(by=['A', 'B'], ascending=False)
indexer = np.lexsort((frame['B'].rank(ascending=False), frame['A'].rank(ascending=False)))
expected = frame.take(indexer)
tm.assert_frame_equal(result, expected)
result = frame.sort_values(by=['B', 'A'])
indexer = np.lexsort((frame['A'], frame['B']))
expected = frame.take(indexer)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_values.py:129 | Complexity: Advanced | Last updated: 2026-06-02*