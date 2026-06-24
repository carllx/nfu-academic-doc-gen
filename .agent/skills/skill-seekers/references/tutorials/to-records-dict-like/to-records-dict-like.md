# How To: To Records Dict Like

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records dict like

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
df = DataFrame({'A': [1, 2], 'B': [0.2, 1.5], 'C': ['a', 'bc']})
```

### Step 2: Assign dtype_mappings = value

```python
dtype_mappings = {'column_dtypes': DictLike(A=np.int8, B=np.float32), 'index_dtypes': f'{tm.ENDIAN}U2'}
```

### Step 3: Assign result = df.to_records(...)

```python
result = df.to_records(**dtype_mappings)
```

### Step 4: Assign expected = np.rec.array(...)

```python
expected = np.rec.array([('0', '1', '0.2', 'a'), ('1', '2', '1.5', 'bc')], dtype=[('index', f'{tm.ENDIAN}U2'), ('A', 'i1'), ('B', f'{tm.ENDIAN}f4'), ('C', 'O')])
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 6: Assign self.d = kwargs.copy(...)

```python
self.d = kwargs.copy()
```


## Complete Example

```python
# Workflow
class DictLike:

    def __init__(self, **kwargs) -> None:
        self.d = kwargs.copy()

    def __getitem__(self, key):
        return self.d.__getitem__(key)

    def __contains__(self, key) -> bool:
        return key in self.d

    def keys(self):
        return self.d.keys()
df = DataFrame({'A': [1, 2], 'B': [0.2, 1.5], 'C': ['a', 'bc']})
dtype_mappings = {'column_dtypes': DictLike(A=np.int8, B=np.float32), 'index_dtypes': f'{tm.ENDIAN}U2'}
result = df.to_records(**dtype_mappings)
expected = np.rec.array([('0', '1', '0.2', 'a'), ('1', '2', '1.5', 'bc')], dtype=[('index', f'{tm.ENDIAN}U2'), ('A', 'i1'), ('B', f'{tm.ENDIAN}f4'), ('C', 'O')])
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_to_records.py:478 | Complexity: Intermediate | Last updated: 2026-06-02*