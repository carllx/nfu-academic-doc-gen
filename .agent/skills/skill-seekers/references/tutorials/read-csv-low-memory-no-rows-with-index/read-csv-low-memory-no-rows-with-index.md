# How To: Read Csv Low Memory No Rows With Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read csv low memory no rows with index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `inspect`
- `io`
- `os`
- `pathlib`
- `sys`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.c_parser_wrapper`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,C\n1,1,1,2\n2,2,3,4\n3,3,4,5\n'

```python
data = 'A,B,C\n1,1,1,2\n2,2,3,4\n3,3,4,5\n'
```

### Step 3: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), low_memory=True, index_col=0, nrows=0)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['A', 'B', 'C'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call pytest.skip()

```python
pytest.skip('This is a low-memory specific test')
```

### Step 7: Assign msg = "The 'nrows' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
```

### Step 8: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), low_memory=True, index_col=0, nrows=0)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
if not parser.low_memory:
    pytest.skip('This is a low-memory specific test')
data = 'A,B,C\n1,1,1,2\n2,2,3,4\n3,3,4,5\n'
if parser.engine == 'pyarrow':
    msg = "The 'nrows' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), low_memory=True, index_col=0, nrows=0)
    return
result = parser.read_csv(StringIO(data), low_memory=True, index_col=0, nrows=0)
expected = DataFrame(columns=['A', 'B', 'C'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_common_basic.py:173 | Complexity: Advanced | Last updated: 2026-06-02*