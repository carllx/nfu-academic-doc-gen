# How To: Info Max Cols

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info max cols

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((10, 5)))
```

**Verification:**
```python
assert len(res.strip().split('\n')) == len_
```

### Step 2: Assign buf = StringIO(...)

```python
buf = StringIO()
```

**Verification:**
```python
assert len(res.strip().split('\n')) == len_
```

### Step 3: Call df.info()

```python
df.info(buf=buf, verbose=verbose)
```

**Verification:**
```python
assert len(res.strip().split('\n')) == len_
```

### Step 4: Assign res = buf.getvalue(...)

```python
res = buf.getvalue()
```

**Verification:**
```python
assert len(res.strip().split('\n')) == len_
```

### Step 5: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 6: Call df.info()

```python
df.info(buf=buf, verbose=verbose)
```

### Step 7: Assign res = buf.getvalue(...)

```python
res = buf.getvalue()
```

**Verification:**
```python
assert len(res.strip().split('\n')) == len_
```

### Step 8: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 9: Call df.info()

```python
df.info(buf=buf, max_cols=max_cols)
```

### Step 10: Assign res = buf.getvalue(...)

```python
res = buf.getvalue()
```

**Verification:**
```python
assert len(res.strip().split('\n')) == len_
```

### Step 11: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 12: Call df.info()

```python
df.info(buf=buf, max_cols=max_cols)
```

### Step 13: Assign res = buf.getvalue(...)

```python
res = buf.getvalue()
```

**Verification:**
```python
assert len(res.strip().split('\n')) == len_
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((10, 5)))
for len_, verbose in [(5, None), (5, False), (12, True)]:
    with option_context('max_info_columns', 4):
        buf = StringIO()
        df.info(buf=buf, verbose=verbose)
        res = buf.getvalue()
        assert len(res.strip().split('\n')) == len_
for len_, verbose in [(12, None), (5, False), (12, True)]:
    with option_context('max_info_columns', 5):
        buf = StringIO()
        df.info(buf=buf, verbose=verbose)
        res = buf.getvalue()
        assert len(res.strip().split('\n')) == len_
for len_, max_cols in [(12, 5), (5, 4)]:
    with option_context('max_info_columns', 4):
        buf = StringIO()
        df.info(buf=buf, max_cols=max_cols)
        res = buf.getvalue()
        assert len(res.strip().split('\n')) == len_
    with option_context('max_info_columns', 5):
        buf = StringIO()
        df.info(buf=buf, max_cols=max_cols)
        res = buf.getvalue()
        assert len(res.strip().split('\n')) == len_
```

## Next Steps


---

*Source: test_info.py:286 | Complexity: Advanced | Last updated: 2026-06-02*