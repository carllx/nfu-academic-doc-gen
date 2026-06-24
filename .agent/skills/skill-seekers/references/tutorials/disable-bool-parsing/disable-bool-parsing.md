# How To: Disable Bool Parsing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test disable bool parsing

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
# Fixtures: c_parser_only
```

## Step-by-Step Guide

### Step 1: Assign parser = c_parser_only

```python
parser = c_parser_only
```

**Verification:**
```python
assert (result.dtypes == object).all()
```

### Step 2: Assign data = 'A,B,C\nYes,No,Yes\nNo,Yes,Yes\nYes,,Yes\nNo,No,No'

```python
data = 'A,B,C\nYes,No,Yes\nNo,Yes,Yes\nYes,,Yes\nNo,No,No'
```

**Verification:**
```python
assert result['B'][2] == ''
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype=object)
```

**Verification:**
```python
assert (result.dtypes == object).all()
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), dtype=object, na_filter=False)
```

**Verification:**
```python
assert result['B'][2] == ''
```


## Complete Example

```python
# Setup
# Fixtures: c_parser_only

# Workflow
parser = c_parser_only
data = 'A,B,C\nYes,No,Yes\nNo,Yes,Yes\nYes,,Yes\nNo,No,No'
result = parser.read_csv(StringIO(data), dtype=object)
assert (result.dtypes == object).all()
result = parser.read_csv(StringIO(data), dtype=object, na_filter=False)
assert result['B'][2] == ''
```

## Next Steps


---

*Source: test_c_parser_only.py:219 | Complexity: Intermediate | Last updated: 2026-06-02*