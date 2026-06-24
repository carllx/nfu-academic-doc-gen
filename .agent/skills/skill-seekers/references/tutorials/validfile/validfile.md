# How To: Validfile

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ValidFile

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
assert_(ds.exists(tmpfile))
```

### Step 2: Assign tmpfile = valid_textfile(...)

```python
tmpfile = valid_textfile(tmp_path)
```

**Verification:**
```python
assert_(ds.exists(tmpfile))
```

### Step 3: Call assert_()

```python
assert_(ds.exists(tmpfile))
```

### Step 4: Assign localdir = mkdtemp(...)

```python
localdir = mkdtemp()
```

### Step 5: Assign tmpfile = valid_textfile(...)

```python
tmpfile = valid_textfile(localdir)
```

### Step 6: Call assert_()

```python
assert_(ds.exists(tmpfile))
```

### Step 7: Call rmtree()

```python
rmtree(localdir)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
ds = datasource.DataSource(tmp_path)
tmpfile = valid_textfile(tmp_path)
assert_(ds.exists(tmpfile))
localdir = mkdtemp()
tmpfile = valid_textfile(localdir)
assert_(ds.exists(tmpfile))
rmtree(localdir)
```

## Next Steps


---

*Source: test__datasource.py:168 | Complexity: Intermediate | Last updated: 2026-06-02*