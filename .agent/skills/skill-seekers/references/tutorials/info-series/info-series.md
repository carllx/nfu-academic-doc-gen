# How To: Info Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test info series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `string`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`

**Setup Required:**
```python
# Fixtures: lexsorted_two_level_string_multiindex, verbose, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign index = lexsorted_two_level_string_multiindex

```python
index = lexsorted_two_level_string_multiindex
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(len(index)), index=index, name='sth')
```

### Step 3: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 4: Call ser.info()

```python
ser.info(verbose=verbose, buf=buf)
```

### Step 5: Assign result = buf.getvalue(...)

```python
result = buf.getvalue()
```

### Step 6: Assign expected = textwrap.dedent(...)

```python
expected = textwrap.dedent("        <class 'pandas.core.series.Series'>\n        MultiIndex: 10 entries, ('foo', 'one') to ('qux', 'three')\n        ")
```

### Step 7: Assign qualifier = value

```python
qualifier = '' if using_infer_string and HAS_PYARROW else '+'
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: lexsorted_two_level_string_multiindex, verbose, using_infer_string

# Workflow
index = lexsorted_two_level_string_multiindex
ser = Series(range(len(index)), index=index, name='sth')
buf = StringIO()
ser.info(verbose=verbose, buf=buf)
result = buf.getvalue()
expected = textwrap.dedent("        <class 'pandas.core.series.Series'>\n        MultiIndex: 10 entries, ('foo', 'one') to ('qux', 'three')\n        ")
if verbose:
    expected += textwrap.dedent('            Series name: sth\n            Non-Null Count  Dtype\n            --------------  -----\n            10 non-null     int64\n            ')
qualifier = '' if using_infer_string and HAS_PYARROW else '+'
expected += textwrap.dedent(f'        dtypes: int64(1)\n        memory usage: {ser.memory_usage()}.0{qualifier} bytes\n        ')
assert result == expected
```

## Next Steps


---

*Source: test_info.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*