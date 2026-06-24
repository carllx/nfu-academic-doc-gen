# How To: No Py312 Distutils Fcompiler

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Check that no distutils imports are performed on 3.12
CLI :: --fcompiler --help-link --backend distutils

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `platform`
- `re`
- `shlex`
- `subprocess`
- `sys`
- `textwrap`
- `collections`
- `pathlib`
- `pytest`
- `numpy.f2py.f2py2e`
- `numpy.testing._private.utils`
- `numpy`

**Setup Required:**
```python
# Fixtures: capfd, hello_world_f90, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'Check that no distutils imports are performed on 3.12\n    CLI :: --fcompiler --help-link --backend distutils\n    '

```python
'Check that no distutils imports are performed on 3.12\n    CLI :: --fcompiler --help-link --backend distutils\n    '
```

**Verification:**
```python
assert '--fcompiler cannot be used with meson' in out
```

### Step 2: Assign MNAME = 'hi'

```python
MNAME = 'hi'
```

**Verification:**
```python
assert 'Use --dep for meson builds' in out
```

### Step 3: Assign foutl = get_io_paths(...)

```python
foutl = get_io_paths(hello_world_f90, mname=MNAME)
```

**Verification:**
```python
assert 'Cannot use distutils backend with Python>=3.12' in out
```

### Step 4: Assign ipath = value

```python
ipath = foutl.f90inp
```

### Step 5: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -c --fcompiler=gfortran -m {MNAME}'.split())
```

### Step 6: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', ['f2py', '--help-link'])
```

### Step 7: Assign MNAME = 'hi2'

```python
MNAME = 'hi2'
```

### Step 8: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -c -m {MNAME} --backend distutils'.split())
```

### Step 9: Call compiler_check_f2pycli()

```python
compiler_check_f2pycli()
```

### Step 10: Assign unknown = capfd.readouterr(...)

```python
out, _ = capfd.readouterr()
```

**Verification:**
```python
assert '--fcompiler cannot be used with meson' in out
```

### Step 11: Call f2pycli()

```python
f2pycli()
```

### Step 12: Assign unknown = capfd.readouterr(...)

```python
out, _ = capfd.readouterr()
```

**Verification:**
```python
assert 'Use --dep for meson builds' in out
```

### Step 13: Call f2pycli()

```python
f2pycli()
```

### Step 14: Assign unknown = capfd.readouterr(...)

```python
out, _ = capfd.readouterr()
```

**Verification:**
```python
assert 'Cannot use distutils backend with Python>=3.12' in out
```


## Complete Example

```python
# Setup
# Fixtures: capfd, hello_world_f90, monkeypatch

# Workflow
'Check that no distutils imports are performed on 3.12\n    CLI :: --fcompiler --help-link --backend distutils\n    '
MNAME = 'hi'
foutl = get_io_paths(hello_world_f90, mname=MNAME)
ipath = foutl.f90inp
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -c --fcompiler=gfortran -m {MNAME}'.split())
with util.switchdir(ipath.parent):
    compiler_check_f2pycli()
    out, _ = capfd.readouterr()
    assert '--fcompiler cannot be used with meson' in out
monkeypatch.setattr(sys, 'argv', ['f2py', '--help-link'])
with util.switchdir(ipath.parent):
    f2pycli()
    out, _ = capfd.readouterr()
    assert 'Use --dep for meson builds' in out
MNAME = 'hi2'
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -c -m {MNAME} --backend distutils'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    out, _ = capfd.readouterr()
    assert 'Cannot use distutils backend with Python>=3.12' in out
```

## Next Steps


---

*Source: test_f2py2e.py:237 | Complexity: Advanced | Last updated: 2026-06-02*