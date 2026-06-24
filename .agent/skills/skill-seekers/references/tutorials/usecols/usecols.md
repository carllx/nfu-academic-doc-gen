# How To: Usecols

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols

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

### Step 1: Assign data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9\n10,11,12'

```python
data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9\n10,11,12'
```

**Verification:**
```python
assert len(result) == 2
```

### Step 2: Assign reader = _make_reader(...)

```python
reader = _make_reader(usecols=(1, 2))
```

**Verification:**
```python
assert (result[1] == exp[1]).all()
```

### Step 3: Assign result = reader.read(...)

```python
result = reader.read()
```

**Verification:**
```python
assert (result[2] == exp[2]).all()
```

### Step 4: Assign exp = _make_reader.read(...)

```python
exp = _make_reader().read()
```

**Verification:**
```python
assert len(result) == 2
```


## Complete Example

```python
# Workflow
data = 'a,b,c\n1,2,3\n4,5,6\n7,8,9\n10,11,12'

def _make_reader(**kwds):
    return TextReader(StringIO(data), delimiter=',', **kwds)
reader = _make_reader(usecols=(1, 2))
result = reader.read()
exp = _make_reader().read()
assert len(result) == 2
assert (result[1] == exp[1]).all()
assert (result[2] == exp[2]).all()
```

## Next Steps


---

*Source: test_textreader.py:243 | Complexity: Intermediate | Last updated: 2026-06-02*