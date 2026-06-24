# How To: Validbz2File

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ValidBz2File

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
assert_equal(magic_line, result)
```

### Step 2: Assign filepath = os.path.join(...)

```python
filepath = os.path.join(tmp_path, 'foobar.txt.bz2')
```

### Step 3: Assign fp = bz2.BZ2File(...)

```python
fp = bz2.BZ2File(filepath, 'w')
```

### Step 4: Call fp.write()

```python
fp.write(magic_line)
```

### Step 5: Call fp.close()

```python
fp.close()
```

### Step 6: Assign fp = ds.open(...)

```python
fp = ds.open(filepath)
```

### Step 7: Assign result = fp.readline(...)

```python
result = fp.readline()
```

### Step 8: Call fp.close()

```python
fp.close()
```

### Step 9: Call assert_equal()

```python
assert_equal(magic_line, result)
```

### Step 10: Call pytest.skip()

```python
pytest.skip()
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
try:
    import bz2
except ImportError:
    pytest.skip()
ds = datasource.DataSource(tmp_path)
filepath = os.path.join(tmp_path, 'foobar.txt.bz2')
fp = bz2.BZ2File(filepath, 'w')
fp.write(magic_line)
fp.close()
fp = ds.open(filepath)
result = fp.readline()
fp.close()
assert_equal(magic_line, result)
```

## Next Steps


---

*Source: test__datasource.py:141 | Complexity: Advanced | Last updated: 2026-06-02*