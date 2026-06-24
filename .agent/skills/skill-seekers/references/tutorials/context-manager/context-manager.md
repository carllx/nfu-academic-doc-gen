# How To: Context Manager

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test context manager

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `platform`
- `urllib.error`
- `uuid`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, datapath
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

**Verification:**
```python
assert not reader.handles.handle.closed
```

### Step 2: Assign path = datapath(...)

```python
path = datapath('io', 'data', 'csv', 'iris.csv')
```

**Verification:**
```python
assert False
```

### Step 3: Assign reader = parser.read_csv(...)

```python
reader = parser.read_csv(path, chunksize=1)
```

**Verification:**
```python
assert reader.handles.handle.closed
```

### Step 4: Assign msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(path, chunksize=1)
```

### Step 6: Call next()

```python
next(reader)
```

**Verification:**
```python
assert False
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, datapath

# Workflow
parser = all_parsers
path = datapath('io', 'data', 'csv', 'iris.csv')
if parser.engine == 'pyarrow':
    msg = "The 'chunksize' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(path, chunksize=1)
    return
reader = parser.read_csv(path, chunksize=1)
assert not reader.handles.handle.closed
try:
    with reader:
        next(reader)
        assert False
except AssertionError:
    assert reader.handles.handle.closed
```

## Next Steps


---

*Source: test_file_buffer_url.py:411 | Complexity: Advanced | Last updated: 2026-06-02*