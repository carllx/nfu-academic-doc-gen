# How To: Sandboxing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sandboxing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `urllib.request`
- `shutil`
- `tempfile`
- `urllib.error`
- `urllib.parse`
- `pytest`
- `numpy.lib._datasource`
- `numpy.testing`
- `gzip`
- `bz2`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign ds = datasource.DataSource(...)

```python
ds = datasource.DataSource(tmp_path)
```

**Verification:**
```python
assert_(path(valid_httpurl()).startswith(str(tmp_path)))
```

### Step 2: Assign tmpfile = valid_textfile(...)

```python
tmpfile = valid_textfile(tmp_path)
```

**Verification:**
```python
assert_(path(invalid_httpurl()).startswith(str(tmp_path)))
```

### Step 3: Assign tmpfilename = value

```python
tmpfilename = os.path.split(tmpfile)[-1]
```

**Verification:**
```python
assert_(path(tmpfile).startswith(str(tmp_path)))
```

### Step 4: Assign path = value

```python
path = lambda x: os.path.abspath(ds.abspath(x))
```

**Verification:**
```python
assert_(path(tmpfilename).startswith(str(tmp_path)))
```

### Step 5: Call assert_()

```python
assert_(path(valid_httpurl()).startswith(str(tmp_path)))
```

**Verification:**
```python
assert_(path(http_path + fn).startswith(str(tmp_path)))
```

### Step 6: Call assert_()

```python
assert_(path(invalid_httpurl()).startswith(str(tmp_path)))
```

**Verification:**
```python
assert_(path(fn).startswith(str(tmp_path)))
```

### Step 7: Call assert_()

```python
assert_(path(tmpfile).startswith(str(tmp_path)))
```

### Step 8: Call assert_()

```python
assert_(path(tmpfilename).startswith(str(tmp_path)))
```

### Step 9: Call assert_()

```python
assert_(path(http_path + fn).startswith(str(tmp_path)))
```

### Step 10: Call assert_()

```python
assert_(path(fn).startswith(str(tmp_path)))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
ds = datasource.DataSource(tmp_path)
tmpfile = valid_textfile(tmp_path)
tmpfilename = os.path.split(tmpfile)[-1]
path = lambda x: os.path.abspath(ds.abspath(x))
assert_(path(valid_httpurl()).startswith(str(tmp_path)))
assert_(path(invalid_httpurl()).startswith(str(tmp_path)))
assert_(path(tmpfile).startswith(str(tmp_path)))
assert_(path(tmpfilename).startswith(str(tmp_path)))
for fn in malicious_files:
    assert_(path(http_path + fn).startswith(str(tmp_path)))
    assert_(path(fn).startswith(str(tmp_path)))
```

## Next Steps


---

*Source: test__datasource.py:219 | Complexity: Advanced | Last updated: 2026-06-02*