# How To: Invalidfile

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test InvalidFile

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
assert_(invalidfile != ds.abspath(tmpfilename))
```

### Step 2: Assign invalidfile = valid_textfile(...)

```python
invalidfile = valid_textfile(tmp_path)
```

**Verification:**
```python
assert_(invalidfile != ds.abspath(tmpfile))
```

### Step 3: Assign tmpfile = valid_textfile(...)

```python
tmpfile = valid_textfile(tmp_path)
```

### Step 4: Assign tmpfilename = value

```python
tmpfilename = os.path.split(tmpfile)[-1]
```

### Step 5: Call assert_()

```python
assert_(invalidfile != ds.abspath(tmpfilename))
```

### Step 6: Call assert_()

```python
assert_(invalidfile != ds.abspath(tmpfile))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
ds = datasource.DataSource(tmp_path)
invalidfile = valid_textfile(tmp_path)
tmpfile = valid_textfile(tmp_path)
tmpfilename = os.path.split(tmpfile)[-1]
assert_(invalidfile != ds.abspath(tmpfilename))
assert_(invalidfile != ds.abspath(tmpfile))
```

## Next Steps


---

*Source: test__datasource.py:209 | Complexity: Intermediate | Last updated: 2026-06-02*