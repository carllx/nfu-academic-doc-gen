# How To: Read Non Existent

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test read non existent

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `errno`
- `functools`
- `io`
- `mmap`
- `os`
- `pathlib`
- `pickle`
- `tempfile`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `py.path`

**Setup Required:**
```python
# Fixtures: reader, module, error_class, fn_ext
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip(module)
```

### Step 2: Assign path = os.path.join(...)

```python
path = os.path.join(HERE, 'data', 'does_not_exist.' + fn_ext)
```

### Step 3: Assign msg1 = value

```python
msg1 = f"File (b')?.+does_not_exist\\.{fn_ext}'? does not exist"
```

### Step 4: Assign msg2 = value

```python
msg2 = f"\\[Errno 2\\] No such file or directory: '.+does_not_exist\\.{fn_ext}'"
```

### Step 5: Assign msg3 = 'Expected object or value'

```python
msg3 = 'Expected object or value'
```

### Step 6: Assign msg4 = 'path_or_buf needs to be a string file path or file-like'

```python
msg4 = 'path_or_buf needs to be a string file path or file-like'
```

### Step 7: Assign msg5 = value

```python
msg5 = f"\\[Errno 2\\] File .+does_not_exist\\.{fn_ext} does not exist: '.+does_not_exist\\.{fn_ext}'"
```

### Step 8: Assign msg6 = value

```python
msg6 = f"\\[Errno 2\\] 没有那个文件或目录: '.+does_not_exist\\.{fn_ext}'"
```

### Step 9: Assign msg7 = value

```python
msg7 = f"\\[Errno 2\\] File o directory non esistente: '.+does_not_exist\\.{fn_ext}'"
```

### Step 10: Assign msg8 = value

```python
msg8 = f'Failed to open local file.+does_not_exist\\.{fn_ext}'
```

### Step 11: Call reader()

```python
reader(path)
```


## Complete Example

```python
# Setup
# Fixtures: reader, module, error_class, fn_ext

# Workflow
pytest.importorskip(module)
path = os.path.join(HERE, 'data', 'does_not_exist.' + fn_ext)
msg1 = f"File (b')?.+does_not_exist\\.{fn_ext}'? does not exist"
msg2 = f"\\[Errno 2\\] No such file or directory: '.+does_not_exist\\.{fn_ext}'"
msg3 = 'Expected object or value'
msg4 = 'path_or_buf needs to be a string file path or file-like'
msg5 = f"\\[Errno 2\\] File .+does_not_exist\\.{fn_ext} does not exist: '.+does_not_exist\\.{fn_ext}'"
msg6 = f"\\[Errno 2\\] 没有那个文件或目录: '.+does_not_exist\\.{fn_ext}'"
msg7 = f"\\[Errno 2\\] File o directory non esistente: '.+does_not_exist\\.{fn_ext}'"
msg8 = f'Failed to open local file.+does_not_exist\\.{fn_ext}'
with pytest.raises(error_class, match=f'({msg1}|{msg2}|{msg3}|{msg4}|{msg5}|{msg6}|{msg7}|{msg8})'):
    reader(path)
```

## Next Steps


---

*Source: test_common.py:201 | Complexity: Advanced | Last updated: 2026-06-02*