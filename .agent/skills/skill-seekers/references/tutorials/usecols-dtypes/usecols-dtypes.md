# How To: Usecols Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test usecols dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `io`
- `mmap`
- `os`
- `tarfile`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: c_parser_only, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign parser = c_parser_only

```python
parser = c_parser_only
```

**Verification:**
```python
assert (result.dtypes == ['string', int, float]).all()
```

### Step 2: Assign data = '1,2,3\n4,5,6\n7,8,9\n10,11,12'

```python
data = '1,2,3\n4,5,6\n7,8,9\n10,11,12'
```

**Verification:**
```python
assert (result2.dtypes == ['string', float]).all()
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), usecols=(0, 1, 2), names=('a', 'b', 'c'), header=None, converters={'a': str}, dtype={'b': int, 'c': float})
```

**Verification:**
```python
assert (result.dtypes == [object, int, float]).all()
```

### Step 4: Assign result2 = parser.read_csv(...)

```python
result2 = parser.read_csv(StringIO(data), usecols=(0, 2), names=('a', 'b', 'c'), header=None, converters={'a': str}, dtype={'b': int, 'c': float})
```

**Verification:**
```python
assert (result2.dtypes == [object, float]).all()
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only, using_infer_string

# Workflow
parser = c_parser_only
data = '1,2,3\n4,5,6\n7,8,9\n10,11,12'
result = parser.read_csv(StringIO(data), usecols=(0, 1, 2), names=('a', 'b', 'c'), header=None, converters={'a': str}, dtype={'b': int, 'c': float})
result2 = parser.read_csv(StringIO(data), usecols=(0, 2), names=('a', 'b', 'c'), header=None, converters={'a': str}, dtype={'b': int, 'c': float})
if using_infer_string:
    assert (result.dtypes == ['string', int, float]).all()
    assert (result2.dtypes == ['string', float]).all()
else:
    assert (result.dtypes == [object, int, float]).all()
    assert (result2.dtypes == [object, float]).all()
```

## Next Steps


---

*Source: test_c_parser_only.py:186 | Complexity: Intermediate | Last updated: 2026-06-02*