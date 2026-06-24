# How To: Mod Gen Gh25263

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Check that pyf files are correctly generated with module structure
CLI :: -m <name> -h pyf_file
BUG: numpy-gh #20520

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
# Fixtures: capfd, hello_world_f77, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'Check that pyf files are correctly generated with module structure\n    CLI :: -m <name> -h pyf_file\n    BUG: numpy-gh #20520\n    '

```python
'Check that pyf files are correctly generated with module structure\n    CLI :: -m <name> -h pyf_file\n    BUG: numpy-gh #20520\n    '
```

**Verification:**
```python
assert 'python module hi' in pyfdat
```

### Step 2: Assign MNAME = 'hi'

```python
MNAME = 'hi'
```

### Step 3: Assign foutl = get_io_paths(...)

```python
foutl = get_io_paths(hello_world_f77, mname=MNAME)
```

### Step 4: Assign ipath = value

```python
ipath = foutl.finp
```

### Step 5: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -m {MNAME} -h hi.pyf'.split())
```

### Step 6: Call f2pycli()

```python
f2pycli()
```

### Step 7: Assign pyfdat = hipyf.read(...)

```python
pyfdat = hipyf.read()
```

**Verification:**
```python
assert 'python module hi' in pyfdat
```


## Complete Example

```python
# Setup
# Fixtures: capfd, hello_world_f77, monkeypatch

# Workflow
'Check that pyf files are correctly generated with module structure\n    CLI :: -m <name> -h pyf_file\n    BUG: numpy-gh #20520\n    '
MNAME = 'hi'
foutl = get_io_paths(hello_world_f77, mname=MNAME)
ipath = foutl.finp
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -m {MNAME} -h hi.pyf'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    with Path('hi.pyf').open() as hipyf:
        pyfdat = hipyf.read()
        assert 'python module hi' in pyfdat
```

## Next Steps


---

*Source: test_f2py2e.py:362 | Complexity: Intermediate | Last updated: 2026-06-02*