# How To: Pass Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pass dtype

## Prerequisites

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas._libs.parsers`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`


## Step-by-Step Guide

### Step 1: Assign data = 'one,two\n1,a\n2,b\n3,c\n4,d'

```python
data = 'one,two\n1,a\n2,b\n3,c\n4,d'
```

**Verification:**
```python
assert result[0].dtype == 'u1'
```

### Step 2: Assign reader = _make_reader(...)

```python
reader = _make_reader(dtype={'one': 'u1', 1: 'S1'})
```

**Verification:**
```python
assert result[1].dtype == 'S1'
```

### Step 3: Assign result = reader.read(...)

```python
result = reader.read()
```

**Verification:**
```python
assert result[0].dtype == 'u1'
```

### Step 4: Assign reader = _make_reader(...)

```python
reader = _make_reader(dtype={'one': np.uint8, 1: object})
```

**Verification:**
```python
assert result[1].dtype == 'O'
```

### Step 5: Assign result = reader.read(...)

```python
result = reader.read()
```

**Verification:**
```python
assert result[0].dtype == 'u1'
```

### Step 6: Assign reader = _make_reader(...)

```python
reader = _make_reader(dtype={'one': np.dtype('u1'), 1: np.dtype('O')})
```

**Verification:**
```python
assert result[1].dtype == 'O'
```

### Step 7: Assign result = reader.read(...)

```python
result = reader.read()
```

**Verification:**
```python
assert result[0].dtype == 'u1'
```

### Step 8: Assign unknown = ensure_dtype_objs(...)

```python
kwds['dtype'] = ensure_dtype_objs(kwds['dtype'])
```


## Complete Example

```python
# Workflow
data = 'one,two\n1,a\n2,b\n3,c\n4,d'

def _make_reader(**kwds):
    if 'dtype' in kwds:
        kwds['dtype'] = ensure_dtype_objs(kwds['dtype'])
    return TextReader(StringIO(data), delimiter=',', **kwds)
reader = _make_reader(dtype={'one': 'u1', 1: 'S1'})
result = reader.read()
assert result[0].dtype == 'u1'
assert result[1].dtype == 'S1'
reader = _make_reader(dtype={'one': np.uint8, 1: object})
result = reader.read()
assert result[0].dtype == 'u1'
assert result[1].dtype == 'O'
reader = _make_reader(dtype={'one': np.dtype('u1'), 1: np.dtype('O')})
result = reader.read()
assert result[0].dtype == 'u1'
assert result[1].dtype == 'O'
```

## Next Steps


---

*Source: test_textreader.py:215 | Complexity: Advanced | Last updated: 2026-06-02*