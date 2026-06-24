# How To: Info Memory Usage Qualified

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info memory usage qualified

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign buf = StringIO(...)

```python
buf = StringIO()
```

**Verification:**
```python
assert '+' not in buf.getvalue()
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(1, columns=list('ab'), index=[1, 2, 3])
```

**Verification:**
```python
assert '+' in buf.getvalue()
```

### Step 3: Call df.info()

```python
df.info(buf=buf)
```

**Verification:**
```python
assert '+' not in buf.getvalue()
```

### Step 4: Assign buf = StringIO(...)

```python
buf = StringIO()
```

**Verification:**
```python
assert '+' in buf.getvalue()
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(1, columns=list('ab'), index=Index(list('ABC'), dtype=object))
```

**Verification:**
```python
assert '+' not in buf.getvalue()
```

### Step 6: Call df.info()

```python
df.info(buf=buf)
```

**Verification:**
```python
assert '+' not in buf.getvalue()
```

### Step 7: Assign buf = StringIO(...)

```python
buf = StringIO()
```

**Verification:**
```python
assert '+' in buf.getvalue()
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(1, columns=list('ab'), index=Index(list('ABC'), dtype='str'))
```

### Step 9: Call df.info()

```python
df.info(buf=buf)
```

### Step 10: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 11: Assign df = DataFrame(...)

```python
df = DataFrame(1, columns=list('ab'), index=MultiIndex.from_product([range(3), range(3)]))
```

### Step 12: Call df.info()

```python
df.info(buf=buf)
```

**Verification:**
```python
assert '+' not in buf.getvalue()
```

### Step 13: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 14: Assign df = DataFrame(...)

```python
df = DataFrame(1, columns=list('ab'), index=MultiIndex.from_product([range(3), ['foo', 'bar']]))
```

### Step 15: Call df.info()

```python
df.info(buf=buf)
```

**Verification:**
```python
assert '+' not in buf.getvalue()
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
buf = StringIO()
df = DataFrame(1, columns=list('ab'), index=[1, 2, 3])
df.info(buf=buf)
assert '+' not in buf.getvalue()
buf = StringIO()
df = DataFrame(1, columns=list('ab'), index=Index(list('ABC'), dtype=object))
df.info(buf=buf)
assert '+' in buf.getvalue()
buf = StringIO()
df = DataFrame(1, columns=list('ab'), index=Index(list('ABC'), dtype='str'))
df.info(buf=buf)
if using_infer_string and HAS_PYARROW:
    assert '+' not in buf.getvalue()
else:
    assert '+' in buf.getvalue()
buf = StringIO()
df = DataFrame(1, columns=list('ab'), index=MultiIndex.from_product([range(3), range(3)]))
df.info(buf=buf)
assert '+' not in buf.getvalue()
buf = StringIO()
df = DataFrame(1, columns=list('ab'), index=MultiIndex.from_product([range(3), ['foo', 'bar']]))
df.info(buf=buf)
if using_infer_string and HAS_PYARROW:
    assert '+' not in buf.getvalue()
else:
    assert '+' in buf.getvalue()
```

## Next Steps


---

*Source: test_info.py:441 | Complexity: Advanced | Last updated: 2026-06-02*