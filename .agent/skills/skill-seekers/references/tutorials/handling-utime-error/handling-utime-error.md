# How To: Handling Utime Error

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test handling utime error

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `ast`
- `glob`
- `os`
- `re`
- `stat`
- `sys`
- `time`
- `pathlib`
- `unittest`
- `pytest`
- `jaraco`
- `setuptools`
- `setuptools.command.egg_info`
- `setuptools.dist`
- `textwrap`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd, env
```

## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution()
```

### Step 2: Assign ei = egg_info(...)

```python
ei = egg_info(dist)
```

### Step 3: Assign utime_patch = mock.patch(...)

```python
utime_patch = mock.patch('os.utime', side_effect=OSError('TEST'))
```

### Step 4: Assign mkpath_patch = mock.patch(...)

```python
mkpath_patch = mock.patch('setuptools.command.egg_info.egg_info.mkpath', return_val=None)
```

### Step 5: Assign msg = "Cannot update time stamp of directory 'None'"

```python
msg = "Cannot update time stamp of directory 'None'"
```

### Step 6: Call ei.run()

```python
ei.run()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, env

# Workflow
dist = Distribution()
ei = egg_info(dist)
utime_patch = mock.patch('os.utime', side_effect=OSError('TEST'))
mkpath_patch = mock.patch('setuptools.command.egg_info.egg_info.mkpath', return_val=None)
with utime_patch, mkpath_patch:
    import distutils.errors
    msg = "Cannot update time stamp of directory 'None'"
    with pytest.raises(distutils.errors.DistutilsFileError, match=msg):
        ei.run()
```

## Next Steps


---

*Source: test_egg_info.py:167 | Complexity: Intermediate | Last updated: 2026-06-02*