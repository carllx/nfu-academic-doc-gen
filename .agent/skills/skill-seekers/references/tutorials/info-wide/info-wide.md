# How To: Info Wide

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info wide

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

### Step 1: Assign io = StringIO(...)

```python
io = StringIO()
```

**Verification:**
```python
assert len(result.splitlines()) > 100
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 101)))
```

**Verification:**
```python
assert result == expected
```

### Step 3: Call df.info()

```python
df.info(buf=io)
```

### Step 4: Assign io = StringIO(...)

```python
io = StringIO()
```

### Step 5: Call df.info()

```python
df.info(buf=io, max_cols=101)
```

### Step 6: Assign result = io.getvalue(...)

```python
result = io.getvalue()
```

**Verification:**
```python
assert len(result.splitlines()) > 100
```

### Step 7: Assign expected = result

```python
expected = result
```

### Step 8: Assign io = StringIO(...)

```python
io = StringIO()
```

### Step 9: Call df.info()

```python
df.info(buf=io)
```

### Step 10: Assign result = io.getvalue(...)

```python
result = io.getvalue()
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
io = StringIO()
df = DataFrame(np.random.default_rng(2).standard_normal((5, 101)))
df.info(buf=io)
io = StringIO()
df.info(buf=io, max_cols=101)
result = io.getvalue()
assert len(result.splitlines()) > 100
expected = result
with option_context('display.max_info_columns', 101):
    io = StringIO()
    df.info(buf=io)
    result = io.getvalue()
    assert result == expected
```

## Next Steps


---

*Source: test_info.py:230 | Complexity: Advanced | Last updated: 2026-06-02*