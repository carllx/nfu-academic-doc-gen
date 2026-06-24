# How To: Temporary File

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test temporary file

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
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = '0 0'

```python
data = '0 0'
```

### Step 3: Call new_file.write()

```python
new_file.write(data)
```

### Step 4: Call new_file.flush()

```python
new_file.flush()
```

### Step 5: Call new_file.seek()

```python
new_file.seek(0)
```

### Step 6: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(new_file, sep='\\s+', header=None)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[0, 0]])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign msg = "the 'pyarrow' engine does not support regex separators"

```python
msg = "the 'pyarrow' engine does not support regex separators"
```

### Step 10: Call parser.read_csv()

```python
parser.read_csv(new_file, sep='\\s+', header=None)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = '0 0'
with tm.ensure_clean(mode='w+', return_filelike=True) as new_file:
    new_file.write(data)
    new_file.flush()
    new_file.seek(0)
    if parser.engine == 'pyarrow':
        msg = "the 'pyarrow' engine does not support regex separators"
        with pytest.raises(ValueError, match=msg):
            parser.read_csv(new_file, sep='\\s+', header=None)
        return
    result = parser.read_csv(new_file, sep='\\s+', header=None)
    expected = DataFrame([[0, 0]])
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_file_buffer_url.py:250 | Complexity: Advanced | Last updated: 2026-06-02*