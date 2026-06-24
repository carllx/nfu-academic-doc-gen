# How To: Build Dir

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Ensures that the build directory can be specified

CLI :: --build-dir

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

### Step 1: 'Ensures that the build directory can be specified\n\n    CLI :: --build-dir\n    '

```python
'Ensures that the build directory can be specified\n\n    CLI :: --build-dir\n    '
```

**Verification:**
```python
assert f'Wrote C/API module "{mname}"' in out
```

### Step 2: Assign ipath = Path(...)

```python
ipath = Path(hello_world_f90)
```

### Step 3: Assign mname = 'blah'

```python
mname = 'blah'
```

### Step 4: Assign odir = 'tttmp'

```python
odir = 'tttmp'
```

### Step 5: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath} --build-dir {odir}'.split())
```

### Step 6: Call f2pycli()

```python
f2pycli()
```

### Step 7: Assign unknown = capfd.readouterr(...)

```python
out, _ = capfd.readouterr()
```

**Verification:**
```python
assert f'Wrote C/API module "{mname}"' in out
```


## Complete Example

```python
# Setup
# Fixtures: capfd, hello_world_f90, monkeypatch

# Workflow
'Ensures that the build directory can be specified\n\n    CLI :: --build-dir\n    '
ipath = Path(hello_world_f90)
mname = 'blah'
odir = 'tttmp'
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath} --build-dir {odir}'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    out, _ = capfd.readouterr()
    assert f'Wrote C/API module "{mname}"' in out
```

## Next Steps


---

*Source: test_f2py2e.py:443 | Complexity: Intermediate | Last updated: 2026-06-02*