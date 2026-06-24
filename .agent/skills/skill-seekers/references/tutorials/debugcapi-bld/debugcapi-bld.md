# How To: Debugcapi Bld

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Ensures that debugging wrappers work

CLI :: --debug-capi -c

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

**Required Fixtures:**
- `api_client` fixture

**Setup Required:**
```python
# Fixtures: hello_world_f90, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'Ensures that debugging wrappers work\n\n    CLI :: --debug-capi -c\n    '

```python
'Ensures that debugging wrappers work\n\n    CLI :: --debug-capi -c\n    '
```

**Verification:**
```python
assert rout.stdout == eout
```

### Step 2: Assign ipath = Path(...)

```python
ipath = Path(hello_world_f90)
```

**Verification:**
```python
assert rout.stderr == eerr
```

### Step 3: Assign mname = 'blah'

```python
mname = 'blah'
```

### Step 4: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath} -c --debug-capi'.split())
```

### Step 5: Call f2pycli()

```python
f2pycli()
```

### Step 6: Assign cmd_run = shlex.split(...)

```python
cmd_run = shlex.split(f'{sys.executable} -c "import blah; blah.hi()"')
```

### Step 7: Assign rout = subprocess.run(...)

```python
rout = subprocess.run(cmd_run, capture_output=True, encoding='UTF-8')
```

### Step 8: Assign eout = ' Hello World\n'

```python
eout = ' Hello World\n'
```

### Step 9: Assign eerr = textwrap.dedent(...)

```python
eerr = textwrap.dedent("debug-capi:Python C/API function blah.hi()\ndebug-capi:float hi=:output,hidden,scalar\ndebug-capi:hi=0\ndebug-capi:Fortran subroutine `f2pywraphi(&hi)'\ndebug-capi:hi=0\ndebug-capi:Building return value.\ndebug-capi:Python C/API function blah.hi: successful.\ndebug-capi:Freeing memory.\n        ")
```

**Verification:**
```python
assert rout.stdout == eout
```


## Complete Example

```python
# Setup
# Fixtures: hello_world_f90, monkeypatch

# Workflow
'Ensures that debugging wrappers work\n\n    CLI :: --debug-capi -c\n    '
ipath = Path(hello_world_f90)
mname = 'blah'
monkeypatch.setattr(sys, 'argv', f'f2py -m {mname} {ipath} -c --debug-capi'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    cmd_run = shlex.split(f'{sys.executable} -c "import blah; blah.hi()"')
    rout = subprocess.run(cmd_run, capture_output=True, encoding='UTF-8')
    eout = ' Hello World\n'
    eerr = textwrap.dedent("debug-capi:Python C/API function blah.hi()\ndebug-capi:float hi=:output,hidden,scalar\ndebug-capi:hi=0\ndebug-capi:Fortran subroutine `f2pywraphi(&hi)'\ndebug-capi:hi=0\ndebug-capi:Building return value.\ndebug-capi:Python C/API function blah.hi: successful.\ndebug-capi:Freeing memory.\n        ")
    assert rout.stdout == eout
    assert rout.stderr == eerr
```

## Next Steps


---

*Source: test_f2py2e.py:584 | Complexity: Advanced | Last updated: 2026-06-02*