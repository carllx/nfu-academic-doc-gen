# How To: Build Ext

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test build ext

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `glob`
- `importlib`
- `os.path`
- `platform`
- `re`
- `shutil`
- `site`
- `subprocess`
- `sys`
- `tempfile`
- `textwrap`
- `time`
- `distutils`
- `distutils.command.build_ext`
- `distutils.core`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `distutils.tests.support`
- `io`
- `jaraco.path`
- `path`
- `pytest`
- `test`
- `compat`
- `distutils.command`
- `xx`
- `distutils.sysconfig`
- `site`
- `pprint`

**Setup Required:**
```python
# Fixtures: copy_so
```

## Step-by-Step Guide

### Step 1: Call missing_compiler_executable()

```python
missing_compiler_executable()
```

### Step 2: Call copy_xxmodule_c()

```python
copy_xxmodule_c(self.tmp_dir)
```

### Step 3: Assign xx_c = os.path.join(...)

```python
xx_c = os.path.join(self.tmp_dir, 'xxmodule.c')
```

### Step 4: Assign xx_ext = Extension(...)

```python
xx_ext = Extension('xx', [xx_c])
```

### Step 5: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'xx', 'ext_modules': [xx_ext]})
```

### Step 6: Assign dist.package_dir = value

```python
dist.package_dir = self.tmp_dir
```

### Step 7: Assign cmd = self.build_ext(...)

```python
cmd = self.build_ext(dist)
```

### Step 8: Call fixup_build_ext()

```python
fixup_build_ext(cmd)
```

### Step 9: Assign cmd.build_lib = value

```python
cmd.build_lib = self.tmp_dir
```

### Step 10: Assign cmd.build_temp = value

```python
cmd.build_temp = self.tmp_dir
```

### Step 11: Assign old_stdout = value

```python
old_stdout = sys.stdout
```

### Step 12: Assign sys.stdout = StringIO(...)

```python
sys.stdout = StringIO()
```

### Step 13: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 14: Call cmd.run()

```python
cmd.run()
```

### Step 15: Assign sys.stdout = old_stdout

```python
sys.stdout = old_stdout
```

### Step 16: Call self._test_xx()

```python
self._test_xx(copy_so)
```

### Step 17: Call os.unlink()

```python
os.unlink('/tmp/libxx_z.so')
```

### Step 18: Assign xx_ext = Extension(...)

```python
xx_ext = Extension('xx', [xx_c], library_dirs=['/usr/lib'], libraries=['z'], runtime_library_dirs=['/usr/lib'])
```

### Step 19: Assign libz_so = value

```python
libz_so = {os.path.realpath(name) for name in glob.iglob('/usr/lib*/libz.so*')}
```

### Step 20: Assign libz_so = sorted(...)

```python
libz_so = sorted(libz_so, key=lambda lib_path: len(lib_path))
```

### Step 21: Call shutil.copyfile()

```python
shutil.copyfile(libz_so[-1], '/tmp/libxx_z.so')
```

### Step 22: Assign xx_ext = Extension(...)

```python
xx_ext = Extension('xx', [xx_c], library_dirs=['/tmp'], libraries=['xx_z'], runtime_library_dirs=['/tmp'])
```


## Complete Example

```python
# Setup
# Fixtures: copy_so

# Workflow
missing_compiler_executable()
copy_xxmodule_c(self.tmp_dir)
xx_c = os.path.join(self.tmp_dir, 'xxmodule.c')
xx_ext = Extension('xx', [xx_c])
if sys.platform != 'win32':
    if not copy_so:
        xx_ext = Extension('xx', [xx_c], library_dirs=['/usr/lib'], libraries=['z'], runtime_library_dirs=['/usr/lib'])
    elif sys.platform == 'linux':
        libz_so = {os.path.realpath(name) for name in glob.iglob('/usr/lib*/libz.so*')}
        libz_so = sorted(libz_so, key=lambda lib_path: len(lib_path))
        shutil.copyfile(libz_so[-1], '/tmp/libxx_z.so')
        xx_ext = Extension('xx', [xx_c], library_dirs=['/tmp'], libraries=['xx_z'], runtime_library_dirs=['/tmp'])
dist = Distribution({'name': 'xx', 'ext_modules': [xx_ext]})
dist.package_dir = self.tmp_dir
cmd = self.build_ext(dist)
fixup_build_ext(cmd)
cmd.build_lib = self.tmp_dir
cmd.build_temp = self.tmp_dir
old_stdout = sys.stdout
if not support.verbose:
    sys.stdout = StringIO()
try:
    cmd.ensure_finalized()
    cmd.run()
finally:
    sys.stdout = old_stdout
with safe_extension_import('xx', self.tmp_dir):
    self._test_xx(copy_so)
if sys.platform == 'linux' and copy_so:
    os.unlink('/tmp/libxx_z.so')
```

## Next Steps


---

*Source: test_build_ext.py:96 | Complexity: Advanced | Last updated: 2026-06-02*