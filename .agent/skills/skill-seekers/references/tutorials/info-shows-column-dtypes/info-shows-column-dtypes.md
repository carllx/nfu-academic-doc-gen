# How To: Info Shows Column Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info shows column dtypes

## Prerequisites

**Required Modules:**
- `io`
- `re`
- `string`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign dtypes = value

```python
dtypes = ['int64', 'float64', 'datetime64[ns]', 'timedelta64[ns]', 'complex128', 'object', 'bool']
```

**Verification:**
```python
assert header in res
```

### Step 2: Assign data = value

```python
data = {}
```

**Verification:**
```python
assert name in res
```

### Step 3: Assign n = 10

```python
n = 10
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

### Step 5: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 6: Call df.info()

```python
df.info(buf=buf)
```

### Step 7: Assign res = buf.getvalue(...)

```python
res = buf.getvalue()
```

### Step 8: Assign header = ' #   Column  Non-Null Count  Dtype          \n---  ------  --------------  -----          '

```python
header = ' #   Column  Non-Null Count  Dtype          \n---  ------  --------------  -----          '
```

**Verification:**
```python
assert header in res
```

### Step 9: Assign unknown = np.random.default_rng.integers.astype(...)

```python
data[i] = np.random.default_rng(2).integers(2, size=n).astype(dtype)
```

### Step 10: Assign name = value

```python
name = f' {i:d}   {i:d}       {n:d} non-null     {dtype}'
```

**Verification:**
```python
assert name in res
```


## Complete Example

```python
# Workflow
dtypes = ['int64', 'float64', 'datetime64[ns]', 'timedelta64[ns]', 'complex128', 'object', 'bool']
data = {}
n = 10
for i, dtype in enumerate(dtypes):
    data[i] = np.random.default_rng(2).integers(2, size=n).astype(dtype)
df = DataFrame(data)
buf = StringIO()
df.info(buf=buf)
res = buf.getvalue()
header = ' #   Column  Non-Null Count  Dtype          \n---  ------  --------------  -----          '
assert header in res
for i, dtype in enumerate(dtypes):
    name = f' {i:d}   {i:d}       {n:d} non-null     {dtype}'
    assert name in res
```

## Next Steps


---

*Source: test_info.py:258 | Complexity: Advanced | Last updated: 2026-06-02*