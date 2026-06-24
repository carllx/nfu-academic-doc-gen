# How To: File Processing Switch

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Tests that it is possible to return to file processing mode
CLI :: :
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
# Fixtures: capfd, hello_world_f90, retreal_f77, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'Tests that it is possible to return to file processing mode\n    CLI :: :\n    BUG: numpy-gh #20520\n    '

```python
'Tests that it is possible to return to file processing mode\n    CLI :: :\n    BUG: numpy-gh #20520\n    '
```

**Verification:**
```python
assert f'buildmodule: Could not find the body of interfaced routine "{skey}". Skipping.' in err
```

### Step 2: Assign foutl = get_io_paths(...)

```python
foutl = get_io_paths(retreal_f77, mname='test')
```

**Verification:**
```python
assert f'Constructing wrapper function "{rkey}"' in out
```

### Step 3: Assign ipath = value

```python
ipath = foutl.finp
```

### Step 4: Assign toskip = 't0 t4 t8 sd s8 s4'

```python
toskip = 't0 t4 t8 sd s8 s4'
```

### Step 5: Assign ipath2 = Path(...)

```python
ipath2 = Path(hello_world_f90)
```

### Step 6: Assign tokeep = 'td s0 hi'

```python
tokeep = 'td s0 hi'
```

### Step 7: Assign mname = 'blah'

```python
mname = 'blah'
```

### Step 8: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -m {mname} only: {tokeep} : {ipath2}'.split())
```

### Step 9: Call f2pycli()

```python
f2pycli()
```

### Step 10: Assign unknown = capfd.readouterr(...)

```python
out, err = capfd.readouterr()
```

**Verification:**
```python
assert f'buildmodule: Could not find the body of interfaced routine "{skey}". Skipping.' in err
```


## Complete Example

```python
# Setup
# Fixtures: capfd, hello_world_f90, retreal_f77, monkeypatch

# Workflow
'Tests that it is possible to return to file processing mode\n    CLI :: :\n    BUG: numpy-gh #20520\n    '
foutl = get_io_paths(retreal_f77, mname='test')
ipath = foutl.finp
toskip = 't0 t4 t8 sd s8 s4'
ipath2 = Path(hello_world_f90)
tokeep = 'td s0 hi'
mname = 'blah'
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -m {mname} only: {tokeep} : {ipath2}'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    out, err = capfd.readouterr()
    for skey in toskip.split():
        assert f'buildmodule: Could not find the body of interfaced routine "{skey}". Skipping.' in err
    for rkey in tokeep.split():
        assert f'Constructing wrapper function "{rkey}"' in out
```

## Next Steps


---

*Source: test_f2py2e.py:315 | Complexity: Advanced | Last updated: 2026-06-02*