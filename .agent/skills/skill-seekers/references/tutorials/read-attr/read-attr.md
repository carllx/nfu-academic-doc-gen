# How To: Read Attr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test read attr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `pathlib`
- `pytest`
- `setuptools._static`
- `setuptools.config`
- `setuptools.discovery`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmp_path, monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'pkg/__init__.py': '', 'pkg/sub/__init__.py': "VERSION = '0.1.1'", 'pkg/sub/mod.py': "VALUES = {'a': 0, 'b': {42}, 'c': (0, 1, 1)}\nraise SystemExit(1)"}
```

**Verification:**
```python
assert version == '0.1.1'
```

### Step 2: Call write_files()

```python
write_files(files, tmp_path)
```

**Verification:**
```python
assert is_static(values)
```

### Step 3: Assign values = expand.read_attr(...)

```python
values = expand.read_attr('lib.mod.VALUES', {'lib': 'pkg/sub'}, tmp_path)
```

**Verification:**
```python
assert values['a'] == 0
```

### Step 4: Call m.chdir()

```python
m.chdir(tmp_path)
```

**Verification:**
```python
assert values['b'] == {42}
```

### Step 5: Assign version = expand.read_attr(...)

```python
version = expand.read_attr('pkg.sub.VERSION')
```

**Verification:**
```python
assert is_static(values)
```

### Step 6: Assign values = expand.read_attr(...)

```python
values = expand.read_attr('lib.mod.VALUES', {'lib': 'pkg/sub'})
```

**Verification:**
```python
assert expand.read_attr('pkg.sub.VERSION', root_dir=tmp_path) == '0.1.1'
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, monkeypatch

# Workflow
files = {'pkg/__init__.py': '', 'pkg/sub/__init__.py': "VERSION = '0.1.1'", 'pkg/sub/mod.py': "VALUES = {'a': 0, 'b': {42}, 'c': (0, 1, 1)}\nraise SystemExit(1)"}
write_files(files, tmp_path)
with monkeypatch.context() as m:
    m.chdir(tmp_path)
    version = expand.read_attr('pkg.sub.VERSION')
    values = expand.read_attr('lib.mod.VALUES', {'lib': 'pkg/sub'})
assert version == '0.1.1'
assert is_static(values)
assert values['a'] == 0
assert values['b'] == {42}
assert is_static(values)
assert expand.read_attr('pkg.sub.VERSION', root_dir=tmp_path) == '0.1.1'
values = expand.read_attr('lib.mod.VALUES', {'lib': 'pkg/sub'}, tmp_path)
assert values['c'] == (0, 1, 1)
```

## Next Steps


---

*Source: test_expand.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*