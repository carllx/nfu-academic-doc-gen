# How To: Spawn

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test spawn

## Prerequisites

**Required Modules:**
- `os`
- `stat`
- `sys`
- `unittest.mock`
- `distutils.errors`
- `distutils.spawn`
- `distutils.tests`
- `path`
- `pytest`
- `test.support`
- `compat`


## Step-by-Step Guide

### Step 1: Assign tmpdir = self.mkdtemp(...)

```python
tmpdir = self.mkdtemp()
```

### Step 2: Call os.chmod()

```python
os.chmod(exe, 511)
```

### Step 3: Call os.chmod()

```python
os.chmod(exe, 511)
```

### Step 4: Call spawn()

```python
spawn([exe])
```

### Step 5: Assign exe = os.path.join(...)

```python
exe = os.path.join(tmpdir, 'foo.sh')
```

### Step 6: Call self.write_file()

```python
self.write_file(exe, f'#!{unix_shell}\nexit 1')
```

### Step 7: Assign exe = os.path.join(...)

```python
exe = os.path.join(tmpdir, 'foo.bat')
```

### Step 8: Call self.write_file()

```python
self.write_file(exe, 'exit 1')
```

### Step 9: Call spawn()

```python
spawn([exe])
```

### Step 10: Assign exe = os.path.join(...)

```python
exe = os.path.join(tmpdir, 'foo.sh')
```

### Step 11: Call self.write_file()

```python
self.write_file(exe, f'#!{unix_shell}\nexit 0')
```

### Step 12: Assign exe = os.path.join(...)

```python
exe = os.path.join(tmpdir, 'foo.bat')
```

### Step 13: Call self.write_file()

```python
self.write_file(exe, 'exit 0')
```


## Complete Example

```python
# Workflow
tmpdir = self.mkdtemp()
if sys.platform != 'win32':
    exe = os.path.join(tmpdir, 'foo.sh')
    self.write_file(exe, f'#!{unix_shell}\nexit 1')
else:
    exe = os.path.join(tmpdir, 'foo.bat')
    self.write_file(exe, 'exit 1')
os.chmod(exe, 511)
with pytest.raises(DistutilsExecError):
    spawn([exe])
if sys.platform != 'win32':
    exe = os.path.join(tmpdir, 'foo.sh')
    self.write_file(exe, f'#!{unix_shell}\nexit 0')
else:
    exe = os.path.join(tmpdir, 'foo.bat')
    self.write_file(exe, 'exit 0')
os.chmod(exe, 511)
spawn([exe])
```

## Next Steps


---

*Source: test_spawn.py:20 | Complexity: Advanced | Last updated: 2026-06-02*