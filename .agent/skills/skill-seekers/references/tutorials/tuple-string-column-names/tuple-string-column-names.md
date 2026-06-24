# How To: Tuple String Column Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tuple string column names

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('a', 'aa'), ('a', 'ab'), ('b', 'ba'), ('b', 'bb')])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([range(4), range(1, 5), range(2, 6)], columns=mi)
```

### Step 3: Assign unknown = 0

```python
df['single_index'] = 0
```

### Step 4: Assign df_flat = df.copy(...)

```python
df_flat = df.copy()
```

### Step 5: Assign df_flat.columns = df_flat.columns.to_flat_index(...)

```python
df_flat.columns = df_flat.columns.to_flat_index()
```

### Step 6: Assign unknown = 0

```python
df_flat['new_single_index'] = 0
```

### Step 7: Assign result = value

```python
result = df_flat[[('a', 'aa'), 'new_single_index']]
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0, 0], [1, 0], [2, 0]], columns=Index([('a', 'aa'), 'new_single_index']))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([('a', 'aa'), ('a', 'ab'), ('b', 'ba'), ('b', 'bb')])
df = DataFrame([range(4), range(1, 5), range(2, 6)], columns=mi)
df['single_index'] = 0
df_flat = df.copy()
df_flat.columns = df_flat.columns.to_flat_index()
df_flat['new_single_index'] = 0
result = df_flat[[('a', 'aa'), 'new_single_index']]
expected = DataFrame([[0, 0], [1, 0], [2, 0]], columns=Index([('a', 'aa'), 'new_single_index']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:148 | Complexity: Advanced | Last updated: 2026-06-02*