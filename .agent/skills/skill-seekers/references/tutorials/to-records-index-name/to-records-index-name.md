# How To: To Records Index Name

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records index name

## Prerequisites

**Required Modules:**
- `collections`
- `email`
- `email.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)))
```

**Verification:**
```python
assert 'X' in rs.dtype.fields
```

### Step 2: Assign df.index.name = 'X'

```python
df.index.name = 'X'
```

**Verification:**
```python
assert 'index' in rs.dtype.fields
```

### Step 3: Assign rs = df.to_records(...)

```python
rs = df.to_records()
```

**Verification:**
```python
assert 'X' in rs.dtype.fields
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)))
```

### Step 5: Assign rs = df.to_records(...)

```python
rs = df.to_records()
```

**Verification:**
```python
assert 'index' in rs.dtype.fields
```

### Step 6: Assign df.index = MultiIndex.from_tuples(...)

```python
df.index = MultiIndex.from_tuples([('a', 'x'), ('a', 'y'), ('b', 'z')])
```

### Step 7: Assign df.index.names = value

```python
df.index.names = ['A', None]
```

### Step 8: Assign result = df.to_records(...)

```python
result = df.to_records()
```

### Step 9: Assign expected = np.rec.fromarrays(...)

```python
expected = np.rec.fromarrays([np.array(['a', 'a', 'b']), np.array(['x', 'y', 'z'])] + [np.asarray(df.iloc[:, i]) for i in range(3)], dtype={'names': ['A', 'level_1', '0', '1', '2'], 'formats': ['O', 'O', f'{tm.ENDIAN}f8', f'{tm.ENDIAN}f8', f'{tm.ENDIAN}f8']})
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)))
df.index.name = 'X'
rs = df.to_records()
assert 'X' in rs.dtype.fields
df = DataFrame(np.random.default_rng(2).standard_normal((3, 3)))
rs = df.to_records()
assert 'index' in rs.dtype.fields
df.index = MultiIndex.from_tuples([('a', 'x'), ('a', 'y'), ('b', 'z')])
df.index.names = ['A', None]
result = df.to_records()
expected = np.rec.fromarrays([np.array(['a', 'a', 'b']), np.array(['x', 'y', 'z'])] + [np.asarray(df.iloc[:, i]) for i in range(3)], dtype={'names': ['A', 'level_1', '0', '1', '2'], 'formats': ['O', 'O', f'{tm.ENDIAN}f8', f'{tm.ENDIAN}f8', f'{tm.ENDIAN}f8']})
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_to_records.py:84 | Complexity: Advanced | Last updated: 2026-06-02*