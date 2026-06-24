# How To: Lower Sig

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: Lowers cases in signature files by flag or when -h is present

CLI :: --[no-]lower -h

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

### Step 1: 'Lowers cases in signature files by flag or when -h is present\n\n    CLI :: --[no-]lower -h\n    '

```python
'Lowers cases in signature files by flag or when -h is present\n\n    CLI :: --[no-]lower -h\n    '
```

**Verification:**
```python
assert capslo.search(out) is not None
```

### Step 2: Assign foutl = get_io_paths(...)

```python
foutl = get_io_paths(hello_world_f77, mname='test')
```

**Verification:**
```python
assert capshi.search(out) is None
```

### Step 3: Assign ipath = value

```python
ipath = foutl.finp
```

**Verification:**
```python
assert capslo.search(out) is None
```

### Step 4: Assign capshi = re.compile(...)

```python
capshi = re.compile('Block: HI')
```

**Verification:**
```python
assert capshi.search(out) is not None
```

### Step 5: Assign capslo = re.compile(...)

```python
capslo = re.compile('Block: hi')
```

### Step 6: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -h {foutl.pyf} -m test --overwrite-signature'.split())
```

### Step 7: Call monkeypatch.setattr()

```python
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -h {foutl.pyf} -m test --overwrite-signature --no-lower'.split())
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
assert capslo.search(out) is not None
```

### Step 10: Call f2pycli()

```python
f2pycli()
```

### Step 11: Assign unknown = capfd.readouterr(...)

```python
out, _ = capfd.readouterr()
```

**Verification:**
```python
assert capslo.search(out) is None
```


## Complete Example

```python
# Setup
# Fixtures: capfd, hello_world_f77, monkeypatch

# Workflow
'Lowers cases in signature files by flag or when -h is present\n\n    CLI :: --[no-]lower -h\n    '
foutl = get_io_paths(hello_world_f77, mname='test')
ipath = foutl.finp
capshi = re.compile('Block: HI')
capslo = re.compile('Block: hi')
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -h {foutl.pyf} -m test --overwrite-signature'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    out, _ = capfd.readouterr()
    assert capslo.search(out) is not None
    assert capshi.search(out) is None
monkeypatch.setattr(sys, 'argv', f'f2py {ipath} -h {foutl.pyf} -m test --overwrite-signature --no-lower'.split())
with util.switchdir(ipath.parent):
    f2pycli()
    out, _ = capfd.readouterr()
    assert capslo.search(out) is None
    assert capshi.search(out) is not None
```

## Next Steps


---

*Source: test_f2py2e.py:404 | Complexity: Advanced | Last updated: 2026-06-02*