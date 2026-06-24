# How To: Astype Mixed Type

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype mixed type

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', 'float32': np.array([1.0] * 10, dtype='float32'), 'int32': np.array([1] * 10, dtype='int32')}, index=np.arange(10))
```

### Step 2: Assign mn = df._get_numeric_data.copy(...)

```python
mn = df._get_numeric_data().copy()
```

### Step 3: Assign unknown = np.array(...)

```python
mn['little_float'] = np.array(12345.0, dtype='float16')
```

### Step 4: Assign unknown = np.array(...)

```python
mn['big_float'] = np.array(123456789101112.0, dtype='float64')
```

### Step 5: Assign casted = mn.astype(...)

```python
casted = mn.astype('float64')
```

### Step 6: Call _check_cast()

```python
_check_cast(casted, 'float64')
```

### Step 7: Assign casted = mn.astype(...)

```python
casted = mn.astype('int64')
```

### Step 8: Call _check_cast()

```python
_check_cast(casted, 'int64')
```

### Step 9: Assign casted = mn.reindex.astype(...)

```python
casted = mn.reindex(columns=['little_float']).astype('float16')
```

### Step 10: Call _check_cast()

```python
_check_cast(casted, 'float16')
```

### Step 11: Assign casted = mn.astype(...)

```python
casted = mn.astype('float32')
```

### Step 12: Call _check_cast()

```python
_check_cast(casted, 'float32')
```

### Step 13: Assign casted = mn.astype(...)

```python
casted = mn.astype('int32')
```

### Step 14: Call _check_cast()

```python
_check_cast(casted, 'int32')
```

### Step 15: Assign casted = mn.astype(...)

```python
casted = mn.astype('O')
```

### Step 16: Call _check_cast()

```python
_check_cast(casted, 'object')
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': 1.0, 'b': 2, 'c': 'foo', 'float32': np.array([1.0] * 10, dtype='float32'), 'int32': np.array([1] * 10, dtype='int32')}, index=np.arange(10))
mn = df._get_numeric_data().copy()
mn['little_float'] = np.array(12345.0, dtype='float16')
mn['big_float'] = np.array(123456789101112.0, dtype='float64')
casted = mn.astype('float64')
_check_cast(casted, 'float64')
casted = mn.astype('int64')
_check_cast(casted, 'int64')
casted = mn.reindex(columns=['little_float']).astype('float16')
_check_cast(casted, 'float16')
casted = mn.astype('float32')
_check_cast(casted, 'float32')
casted = mn.astype('int32')
_check_cast(casted, 'int32')
casted = mn.astype('O')
_check_cast(casted, 'object')
```

## Next Steps


---

*Source: test_astype.py:72 | Complexity: Advanced | Last updated: 2026-06-02*