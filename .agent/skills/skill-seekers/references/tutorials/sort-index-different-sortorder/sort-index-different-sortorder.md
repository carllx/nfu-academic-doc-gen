# How To: Sort Index Different Sortorder

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index different sortorder

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign A = np.arange.repeat(...)

```python
A = np.arange(20).repeat(5)
```

### Step 2: Assign B = np.tile(...)

```python
B = np.tile(np.arange(5), 20)
```

### Step 3: Assign indexer = np.random.default_rng.permutation(...)

```python
indexer = np.random.default_rng(2).permutation(100)
```

### Step 4: Assign A = A.take(...)

```python
A = A.take(indexer)
```

### Step 5: Assign B = B.take(...)

```python
B = B.take(indexer)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'A': A, 'B': B, 'C': np.random.default_rng(2).standard_normal(100)})
```

### Step 7: Assign ex_indexer = np.lexsort(...)

```python
ex_indexer = np.lexsort((df.B.max() - df.B, df.A))
```

### Step 8: Assign expected = df.take(...)

```python
expected = df.take(ex_indexer)
```

### Step 9: Assign idf = df.set_index(...)

```python
idf = df.set_index(['A', 'B'])
```

### Step 10: Assign result = idf.sort_index(...)

```python
result = idf.sort_index(ascending=[1, 0])
```

### Step 11: Assign expected = idf.take(...)

```python
expected = idf.take(ex_indexer)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = unknown.sort_index(...)

```python
result = idf['C'].sort_index(ascending=[1, 0])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected['C'])
```


## Complete Example

```python
# Workflow
A = np.arange(20).repeat(5)
B = np.tile(np.arange(5), 20)
indexer = np.random.default_rng(2).permutation(100)
A = A.take(indexer)
B = B.take(indexer)
df = DataFrame({'A': A, 'B': B, 'C': np.random.default_rng(2).standard_normal(100)})
ex_indexer = np.lexsort((df.B.max() - df.B, df.A))
expected = df.take(ex_indexer)
idf = df.set_index(['A', 'B'])
result = idf.sort_index(ascending=[1, 0])
expected = idf.take(ex_indexer)
tm.assert_frame_equal(result, expected)
result = idf['C'].sort_index(ascending=[1, 0])
tm.assert_series_equal(result, expected['C'])
```

## Next Steps


---

*Source: test_sort_index.py:257 | Complexity: Advanced | Last updated: 2026-06-02*