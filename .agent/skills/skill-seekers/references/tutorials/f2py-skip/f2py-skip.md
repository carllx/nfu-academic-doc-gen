# How To: F2Py Skip

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Tests that functions can be skipped
CLI :: skip:

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
# Fixtures: capfd, retreal_f77, monkeypatch
```

## Step-by-Step Guide

### Step 1: 'Tests that functions can be skipped\n    CLI :: skip:\n    '

```python
'Tests that functions can be skipped\n    CLI :: skip:\n    '
```

**Verification:**
```python
assert f'buildmodule: Could not found the body of interfaced routine "{skey}". Skipping.' in err
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

### Step 5: Assign remaining = 'td s0'

```python
remaining = 'td s0'
```

### Step 6: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -m test skip: {toskip}'.split())
```

### Step 7: Call f2pycli()

```python
f2pycli()
```

### Step 8: Assign unknown = capfd.readouterr(...)

```python
out, err = capfd.readouterr()
```

**Verification:**
```python
assert f'buildmodule: Could not found the body of interfaced routine "{skey}". Skipping.' in err
```


## Complete Example

```python
# Setup
# Fixtures: capfd, retreal_f77, monkeypatch

# Workflow
'Tests that functions can be skipped\n    CLI :: skip:\n    '
foutl = get_io_paths(retreal_f77, mname='test')
ipath = foutl.finp
toskip = 't0 t4 t8 sd s8 s4'
remaining = 'td s0'
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -m test skip: {toskip}'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    out, err = capfd.readouterr()
    for skey in toskip.split():
        assert f'buildmodule: Could not found the body of interfaced routine "{skey}". Skipping.' in err
    for rkey in remaining.split():
        assert f'Constructing wrapper function "{rkey}"' in out
```

## Next Steps


---

*Source: test_f2py2e.py:269 | Complexity: Advanced | Last updated: 2026-06-02*