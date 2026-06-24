# How To: Pkg Roots

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: This test focus in getting a particular implementation detail right.
If at some point in time the implementation is changed for something different,
this test can be modified or even excluded.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `os`
- `platform`
- `stat`
- `subprocess`
- `sys`
- `copy`
- `importlib`
- `importlib.machinery`
- `pathlib`
- `textwrap`
- `typing`
- `unittest.mock`
- `uuid`
- `jaraco.envs`
- `jaraco.path`
- `pytest`
- `path`
- `setuptools._importlib`
- `setuptools.command.editable_wheel`
- `setuptools.dist`
- `setuptools.extension`
- `setuptools.warnings`
- `distutils.core`
- `distutils.command.build_ext`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: 'This test focus in getting a particular implementation detail right.\n    If at some point in time the implementation is changed for something different,\n    this test can be modified or even excluded.\n    '

```python
'This test focus in getting a particular implementation detail right.\n    If at some point in time the implementation is changed for something different,\n    this test can be modified or even excluded.\n    '
```

**Verification:**
```python
assert roots == {'a': str(tmp_path / 'a'), 'a.b.c': str(tmp_path / 'other'), 'a.b.c.x.y.z': str(tmp_path / 'another'), 'd': str(tmp_path / 'd'), 'f': str(tmp_path / 'f'), 'm.n.o.p.q': str(tmp_path / 'yet_another')}
```

### Step 2: Assign files = value

```python
files = {'a': {'b': {'__init__.py': 'ab = 1'}, '__init__.py': 'a = 1'}, 'd': {'__init__.py': 'd = 1', 'e': {'__init__.py': 'de = 1'}}, 'f': {'g': {'h': {'__init__.py': 'fgh = 1'}}}, 'other': {'__init__.py': 'abc = 1'}, 'another': {'__init__.py': 'abcxyz = 1'}, 'yet_another': {'__init__.py': 'mnopq = 1'}}
```

**Verification:**
```python
assert ns == {'f', 'f.g'}
```

### Step 3: Call jaraco.path.build()

```python
jaraco.path.build(files, prefix=tmp_path)
```

**Verification:**
```python
assert ns == {'a.b', 'a.b.c.x', 'a.b.c.x.y', 'm', 'm.n', 'm.n.o', 'm.n.o.p'}
```

### Step 4: Assign package_dir = value

```python
package_dir = {'a.b.c': 'other', 'a.b.c.x.y.z': 'another', 'm.n.o.p.q': 'yet_another'}
```

### Step 5: Assign packages = value

```python
packages = ['a', 'a.b', 'a.b.c', 'a.b.c.x.y', 'a.b.c.x.y.z', 'd', 'd.e', 'f', 'f.g', 'f.g.h', 'm.n.o.p.q']
```

### Step 6: Assign roots = _find_package_roots(...)

```python
roots = _find_package_roots(packages, package_dir, tmp_path)
```

**Verification:**
```python
assert roots == {'a': str(tmp_path / 'a'), 'a.b.c': str(tmp_path / 'other'), 'a.b.c.x.y.z': str(tmp_path / 'another'), 'd': str(tmp_path / 'd'), 'f': str(tmp_path / 'f'), 'm.n.o.p.q': str(tmp_path / 'yet_another')}
```

### Step 7: Assign ns = set(...)

```python
ns = set(dict(_find_namespaces(packages, roots)))
```

**Verification:**
```python
assert ns == {'f', 'f.g'}
```

### Step 8: Assign ns = set(...)

```python
ns = set(_find_virtual_namespaces(roots))
```

**Verification:**
```python
assert ns == {'a.b', 'a.b.c.x', 'a.b.c.x.y', 'm', 'm.n', 'm.n.o', 'm.n.o.p'}
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'This test focus in getting a particular implementation detail right.\n    If at some point in time the implementation is changed for something different,\n    this test can be modified or even excluded.\n    '
files = {'a': {'b': {'__init__.py': 'ab = 1'}, '__init__.py': 'a = 1'}, 'd': {'__init__.py': 'd = 1', 'e': {'__init__.py': 'de = 1'}}, 'f': {'g': {'h': {'__init__.py': 'fgh = 1'}}}, 'other': {'__init__.py': 'abc = 1'}, 'another': {'__init__.py': 'abcxyz = 1'}, 'yet_another': {'__init__.py': 'mnopq = 1'}}
jaraco.path.build(files, prefix=tmp_path)
package_dir = {'a.b.c': 'other', 'a.b.c.x.y.z': 'another', 'm.n.o.p.q': 'yet_another'}
packages = ['a', 'a.b', 'a.b.c', 'a.b.c.x.y', 'a.b.c.x.y.z', 'd', 'd.e', 'f', 'f.g', 'f.g.h', 'm.n.o.p.q']
roots = _find_package_roots(packages, package_dir, tmp_path)
assert roots == {'a': str(tmp_path / 'a'), 'a.b.c': str(tmp_path / 'other'), 'a.b.c.x.y.z': str(tmp_path / 'another'), 'd': str(tmp_path / 'd'), 'f': str(tmp_path / 'f'), 'm.n.o.p.q': str(tmp_path / 'yet_another')}
ns = set(dict(_find_namespaces(packages, roots)))
assert ns == {'f', 'f.g'}
ns = set(_find_virtual_namespaces(roots))
assert ns == {'a.b', 'a.b.c.x', 'a.b.c.x.y', 'm', 'm.n', 'm.n.o', 'm.n.o.p'}
```

## Next Steps


---

*Source: test_editable_install.py:785 | Complexity: Advanced | Last updated: 2026-06-02*