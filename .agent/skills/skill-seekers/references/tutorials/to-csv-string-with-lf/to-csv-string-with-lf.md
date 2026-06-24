# How To: To Csv String With Lf

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to csv string with lf

## Prerequisites

**Required Modules:**
- `io`
- `os`
- `sys`
- `zipfile`
- `_csv`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'int': [1, 2, 3], 'str_lf': ['abc', 'd\nef', 'g\nh\n\ni']}
```

**Verification:**
```python
assert f.read() == expected_noarg
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

**Verification:**
```python
assert f.read() == expected_lf
```

### Step 3: Assign os_linesep = os.linesep.encode(...)

```python
os_linesep = os.linesep.encode('utf-8')
```

**Verification:**
```python
assert f.read() == expected_crlf
```

### Step 4: Assign expected_noarg = value

```python
expected_noarg = b'int,str_lf' + os_linesep + b'1,abc' + os_linesep + b'2,"d\nef"' + os_linesep + b'3,"g\nh\n\ni"' + os_linesep
```

### Step 5: Call df.to_csv()

```python
df.to_csv(path, index=False)
```

### Step 6: Assign expected_lf = b'int,str_lf\n1,abc\n2,"d\nef"\n3,"g\nh\n\ni"\n'

```python
expected_lf = b'int,str_lf\n1,abc\n2,"d\nef"\n3,"g\nh\n\ni"\n'
```

### Step 7: Call df.to_csv()

```python
df.to_csv(path, lineterminator='\n', index=False)
```

### Step 8: Assign expected_crlf = b'int,str_lf\r\n1,abc\r\n2,"d\nef"\r\n3,"g\nh\n\ni"\r\n'

```python
expected_crlf = b'int,str_lf\r\n1,abc\r\n2,"d\nef"\r\n3,"g\nh\n\ni"\r\n'
```

### Step 9: Call df.to_csv()

```python
df.to_csv(path, lineterminator='\r\n', index=False)
```

**Verification:**
```python
assert f.read() == expected_noarg
```


## Complete Example

```python
# Workflow
data = {'int': [1, 2, 3], 'str_lf': ['abc', 'd\nef', 'g\nh\n\ni']}
df = DataFrame(data)
with tm.ensure_clean('lf_test.csv') as path:
    os_linesep = os.linesep.encode('utf-8')
    expected_noarg = b'int,str_lf' + os_linesep + b'1,abc' + os_linesep + b'2,"d\nef"' + os_linesep + b'3,"g\nh\n\ni"' + os_linesep
    df.to_csv(path, index=False)
    with open(path, 'rb') as f:
        assert f.read() == expected_noarg
with tm.ensure_clean('lf_test.csv') as path:
    expected_lf = b'int,str_lf\n1,abc\n2,"d\nef"\n3,"g\nh\n\ni"\n'
    df.to_csv(path, lineterminator='\n', index=False)
    with open(path, 'rb') as f:
        assert f.read() == expected_lf
with tm.ensure_clean('lf_test.csv') as path:
    expected_crlf = b'int,str_lf\r\n1,abc\r\n2,"d\nef"\r\n3,"g\nh\n\ni"\r\n'
    df.to_csv(path, lineterminator='\r\n', index=False)
    with open(path, 'rb') as f:
        assert f.read() == expected_crlf
```

## Next Steps


---

*Source: test_to_csv.py:421 | Complexity: Advanced | Last updated: 2026-06-02*