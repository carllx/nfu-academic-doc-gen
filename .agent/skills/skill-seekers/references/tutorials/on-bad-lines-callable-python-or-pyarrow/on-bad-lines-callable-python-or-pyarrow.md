# How To: On Bad Lines Callable Python Or Pyarrow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test on bad lines callable python or pyarrow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `os`
- `pathlib`
- `pytest`
- `pandas.errors`
- `pandas._testing`
- `pandas.io.parsers`
- `pandas.io.parsers.readers`
- `pandas.io.parsers.readers`
- `pandas.io.parsers.readers`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign sio = StringIO(...)

```python
sio = StringIO('a,b\n1,2')
```

### Step 2: Assign bad_lines_func = value

```python
bad_lines_func = lambda x: x
```

### Step 3: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 4: Assign msg = "on_bad_line can only be a callable function if engine='python' or 'pyarrow'"

```python
msg = "on_bad_line can only be a callable function if engine='python' or 'pyarrow'"
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(sio, on_bad_lines=bad_lines_func)
```

### Step 6: Call parser.read_csv()

```python
parser.read_csv(sio, on_bad_lines=bad_lines_func)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
sio = StringIO('a,b\n1,2')
bad_lines_func = lambda x: x
parser = all_parsers
if all_parsers.engine not in ['python', 'pyarrow']:
    msg = "on_bad_line can only be a callable function if engine='python' or 'pyarrow'"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(sio, on_bad_lines=bad_lines_func)
else:
    parser.read_csv(sio, on_bad_lines=bad_lines_func)
```

## Next Steps


---

*Source: test_unsupported.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*