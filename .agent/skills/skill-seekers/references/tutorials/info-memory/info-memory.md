# How To: Info Memory

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info memory

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
df = DataFrame({'a': Series([1, 2], dtype='i8')})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 3: Call df.info()

```python
df.info(buf=buf)
```

### Step 4: Assign result = buf.getvalue(...)

```python
result = buf.getvalue()
```

### Step 5: Assign bytes = float(...)

```python
bytes = float(df.memory_usage().sum())
```

### Step 6: Assign expected = textwrap.dedent(...)

```python
expected = textwrap.dedent(f"    <class 'pandas.core.frame.DataFrame'>\n    RangeIndex: 2 entries, 0 to 1\n    Data columns (total 1 columns):\n     #   Column  Non-Null Count  Dtype\n    ---  ------  --------------  -----\n     0   a       2 non-null      int64\n    dtypes: int64(1)\n    memory usage: {bytes} bytes\n    ")
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': Series([1, 2], dtype='i8')})
buf = StringIO()
df.info(buf=buf)
result = buf.getvalue()
bytes = float(df.memory_usage().sum())
expected = textwrap.dedent(f"    <class 'pandas.core.frame.DataFrame'>\n    RangeIndex: 2 entries, 0 to 1\n    Data columns (total 1 columns):\n     #   Column  Non-Null Count  Dtype\n    ---  ------  --------------  -----\n     0   a       2 non-null      int64\n    dtypes: int64(1)\n    memory usage: {bytes} bytes\n    ")
assert result == expected
```

## Next Steps


---

*Source: test_info.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*