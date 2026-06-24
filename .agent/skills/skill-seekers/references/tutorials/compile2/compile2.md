# How To: Compile2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compile2

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

### Step 1: Assign tsi = value

```python
tsi = self.c_temp2
```

**Verification:**
```python
assert_(os.path.isfile(self._src2.replace('.c', '.o')))
```

### Step 2: Assign c = customized_ccompiler(...)

```python
c = customized_ccompiler()
```

### Step 3: Assign extra_link_args = value

```python
extra_link_args = tsi.calc_extra_info()['extra_link_args']
```

### Step 4: Assign previousDir = os.getcwd(...)

```python
previousDir = os.getcwd()
```

### Step 5: Call os.chdir()

```python
os.chdir(self._dir2)
```

### Step 6: Call c.compile()

```python
c.compile([os.path.basename(self._src2)], output_dir=self._dir2, extra_postargs=extra_link_args)
```

### Step 7: Call assert_()

```python
assert_(os.path.isfile(self._src2.replace('.c', '.o')))
```

### Step 8: Call os.chdir()

```python
os.chdir(previousDir)
```


## Complete Example

```python
# Workflow
tsi = self.c_temp2
c = customized_ccompiler()
extra_link_args = tsi.calc_extra_info()['extra_link_args']
previousDir = os.getcwd()
try:
    os.chdir(self._dir2)
    c.compile([os.path.basename(self._src2)], output_dir=self._dir2, extra_postargs=extra_link_args)
    assert_(os.path.isfile(self._src2.replace('.c', '.o')))
finally:
    os.chdir(previousDir)
```

## Next Steps


---

*Source: test_system_info.py:251 | Complexity: Advanced | Last updated: 2026-06-02*