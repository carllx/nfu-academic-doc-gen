# How To: Overrides

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test overrides

## Prerequisites

**Required Modules:**
- `os`
- `shutil`
- `pytest`
- `tempfile`
- `subprocess`
- `importlib.metadata`
- `distutils.errors`
- `numpy.testing`
- `numpy.distutils`
- `numpy.distutils.system_info`
- `numpy.distutils.system_info`
- `numpy.distutils.system_info`
- `numpy.distutils`
- `numpy.distutils.system_info`


## Step-by-Step Guide

### Step 1: Assign previousDir = os.getcwd(...)

```python
previousDir = os.getcwd()
```

**Verification:**
```python
assert info.get_lib_dirs() != lib_dirs
```

### Step 2: Assign cfg = os.path.join(...)

```python
cfg = os.path.join(self._dir1, 'site.cfg')
```

**Verification:**
```python
assert info.get_lib_dirs() == lib_dirs
```

### Step 3: Call shutil.copy()

```python
shutil.copy(self._sitecfg, cfg)
```

**Verification:**
```python
assert info.get_lib_dirs() == lib_dirs
```

### Step 4: Call os.chdir()

```python
os.chdir(self._dir1)
```

### Step 5: Assign info = mkl_info(...)

```python
info = mkl_info()
```

### Step 6: Assign lib_dirs = unknown.split(...)

```python
lib_dirs = info.cp['ALL']['library_dirs'].split(os.pathsep)
```

**Verification:**
```python
assert info.get_lib_dirs() != lib_dirs
```

### Step 7: Assign info = mkl_info(...)

```python
info = mkl_info()
```

**Verification:**
```python
assert info.get_lib_dirs() == lib_dirs
```

### Step 8: Assign info = mkl_info(...)

```python
info = mkl_info()
```

**Verification:**
```python
assert info.get_lib_dirs() == lib_dirs
```

### Step 9: Call os.chdir()

```python
os.chdir(previousDir)
```

### Step 10: Assign mkl = fid.read.replace(...)

```python
mkl = fid.read().replace('[ALL]', '[mkl]', 1)
```

### Step 11: Call fid.write()

```python
fid.write(mkl)
```

### Step 12: Assign dflt = fid.read.replace(...)

```python
dflt = fid.read().replace('[mkl]', '[DEFAULT]', 1)
```

### Step 13: Call fid.write()

```python
fid.write(dflt)
```


## Complete Example

```python
# Workflow
previousDir = os.getcwd()
cfg = os.path.join(self._dir1, 'site.cfg')
shutil.copy(self._sitecfg, cfg)
try:
    os.chdir(self._dir1)
    info = mkl_info()
    lib_dirs = info.cp['ALL']['library_dirs'].split(os.pathsep)
    assert info.get_lib_dirs() != lib_dirs
    with open(cfg) as fid:
        mkl = fid.read().replace('[ALL]', '[mkl]', 1)
    with open(cfg, 'w') as fid:
        fid.write(mkl)
    info = mkl_info()
    assert info.get_lib_dirs() == lib_dirs
    with open(cfg) as fid:
        dflt = fid.read().replace('[mkl]', '[DEFAULT]', 1)
    with open(cfg, 'w') as fid:
        fid.write(dflt)
    info = mkl_info()
    assert info.get_lib_dirs() == lib_dirs
finally:
    os.chdir(previousDir)
```

## Next Steps


---

*Source: test_system_info.py:271 | Complexity: Advanced | Last updated: 2026-06-02*