# How To: Wrapfunc Def

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Ensures that fortran subroutine wrappers for F77 are included by default

CLI :: --[no]-wrap-functions

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

### Step 1: 'Ensures that fortran subroutine wrappers for F77 are included by default\n\n    CLI :: --[no]-wrap-functions\n    '

```python
'Ensures that fortran subroutine wrappers for F77 are included by default\n\n    CLI :: --[no]-wrap-functions\n    '
```

**Verification:**
```python
assert 'Fortran 77 wrappers are saved to' in out
```

### Step 2: Assign ipath = Path(...)

```python
ipath = Path(hello_world_f90)
```

**Verification:**
```python
assert 'Fortran 77 wrappers are saved to' in out
```

### Step 3: Assign mname = 'blah'

```python
mname = 'blah'
```

### Step 4: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath}'.split())
```

### Step 5: Assign unknown = capfd.readouterr(...)

```python
out, _ = capfd.readouterr()
```

**Verification:**
```python
assert 'Fortran 77 wrappers are saved to' in out
```

### Step 6: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath} --wrap-functions'.split())
```

### Step 7: Call f2pycli()

```python
f2pycli()
```

### Step 8: Call f2pycli()

```python
f2pycli()
```

### Step 9: Assign unknown = capfd.readouterr(...)

```python
out, _ = capfd.readouterr()
```

**Verification:**
```python
assert 'Fortran 77 wrappers are saved to' in out
```


## Complete Example

```python
# Setup
# Fixtures: capfd, hello_world_f90, monkeypatch

# Workflow
'Ensures that fortran subroutine wrappers for F77 are included by default\n\n    CLI :: --[no]-wrap-functions\n    '
ipath = Path(hello_world_f90)
mname = 'blah'
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath}'.split())
with util.switchdir(ipath.parent):
    f2pycli()
out, _ = capfd.readouterr()
assert 'Fortran 77 wrappers are saved to' in out
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath} --wrap-functions'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    out, _ = capfd.readouterr()
    assert 'Fortran 77 wrappers are saved to' in out
```

## Next Steps


---

*Source: test_f2py2e.py:613 | Complexity: Advanced | Last updated: 2026-06-02*