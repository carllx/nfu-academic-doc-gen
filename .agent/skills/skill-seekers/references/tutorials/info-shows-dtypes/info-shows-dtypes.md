# How To: Info Shows Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info shows dtypes

## Prerequisites

**Required Modules:**
- `io`
- `string`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign dtypes = value

```python
dtypes = ['int64', 'float64', 'datetime64[ns]', 'timedelta64[ns]', 'complex128', 'object', 'bool']
```

**Verification:**
```python
assert name in res
```

### Step 2: Assign n = 10

```python
n = 10
```

### Step 3: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).integers(2, size=n).astype(dtype))
```

### Step 4: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 5: Call s.info()

```python
s.info(buf=buf)
```

### Step 6: Assign res = buf.getvalue(...)

```python
res = buf.getvalue()
```

### Step 7: Assign name = value

```python
name = f'{n:d} non-null     {dtype}'
```

**Verification:**
```python
assert name in res
```


## Complete Example

```python
# Workflow
dtypes = ['int64', 'float64', 'datetime64[ns]', 'timedelta64[ns]', 'complex128', 'object', 'bool']
n = 10
for dtype in dtypes:
    s = Series(np.random.default_rng(2).integers(2, size=n).astype(dtype))
    buf = StringIO()
    s.info(buf=buf)
    res = buf.getvalue()
    name = f'{n:d} non-null     {dtype}'
    assert name in res
```

## Next Steps


---

*Source: test_info.py:110 | Complexity: Intermediate | Last updated: 2026-06-02*