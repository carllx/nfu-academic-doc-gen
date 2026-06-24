# How To: Get Output Mapping With Stub

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test get output mapping with stub

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `os`
- `sys`
- `importlib.util`
- `pytest`
- `jaraco`
- `setuptools.command.build_ext`
- `setuptools.dist`
- `setuptools.errors`
- `setuptools.extension`
- `textwrap`
- `distutils.command.build_ext`
- `distutils.sysconfig`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd, monkeypatch
```

## Step-by-Step Guide

### Step 1: Call monkeypatch.setenv()

```python
monkeypatch.setenv('SETUPTOOLS_EXT_SUFFIX', '.mp3')
```

**Verification:**
```python
assert mapping == {C(f'{build_lib}/ext3.py'): C('src/ext3.py'), f'{build_lib}/ext3.mp3': 'src/ext3.mp3', C(f'{build_lib}/mypkg/ext1.py'): C('src/mypkg/ext1.py'), f'{build_lib}/mypkg/ext1.mp3': 'src/mypkg/ext1.mp3', C(f'{build_lib}/mypkg/subpkg/ext2.py'): C('src/mypkg/subpkg/ext2.py'), f'{build_lib}/mypkg/subpkg/ext2.mp3': 'src/mypkg/subpkg/ext2.mp3'}
```

### Step 2: Call monkeypatch.setattr()

```python
monkeypatch.setattr('setuptools.command.build_ext.use_stubs', True)
```

**Verification:**
```python
assert f'{build_lib}/mypkg/ext1.py' not in mapping
```

### Step 3: Assign dist = self.dist_with_example(...)

```python
dist = self.dist_with_example()
```

**Verification:**
```python
assert f'{build_lib}/mypkg/subpkg/ext2.py' not in mapping
```

### Step 4: Assign build_ext = dist.get_command_obj(...)

```python
build_ext = dist.get_command_obj('build_ext')
```

**Verification:**
```python
assert example_stub in mapping
```

### Step 5: Assign build_ext.editable_mode = True

```python
build_ext.editable_mode = True
```

**Verification:**
```python
assert example_stub.startswith(f'{build_lib}/mypkg/__pycache__/ext1')
```

### Step 6: Call build_ext.ensure_finalized()

```python
build_ext.ensure_finalized()
```

**Verification:**
```python
assert example_stub.endswith('.pyc')
```

### Step 7: Assign build_lib = build_ext.build_lib.replace(...)

```python
build_lib = build_ext.build_lib.replace(os.sep, '/')
```

### Step 8: Assign mapping = value

```python
mapping = {k.replace(os.sep, '/'): v.replace(os.sep, '/') for k, v in build_ext.get_output_mapping().items()}
```

**Verification:**
```python
assert mapping == {C(f'{build_lib}/ext3.py'): C('src/ext3.py'), f'{build_lib}/ext3.mp3': 'src/ext3.mp3', C(f'{build_lib}/mypkg/ext1.py'): C('src/mypkg/ext1.py'), f'{build_lib}/mypkg/ext1.mp3': 'src/mypkg/ext1.mp3', C(f'{build_lib}/mypkg/subpkg/ext2.py'): C('src/mypkg/subpkg/ext2.py'), f'{build_lib}/mypkg/subpkg/ext2.mp3': 'src/mypkg/subpkg/ext2.mp3'}
```

### Step 9: Assign example_stub = C(...)

```python
example_stub = C(f'{build_lib}/mypkg/ext1.py')
```

**Verification:**
```python
assert example_stub in mapping
```

### Step 10: Call monkeypatch.setattr()

```python
monkeypatch.setattr(ext, '_needs_stub', True)
```

### Step 11: """Make it possible to do comparisons and tests in a OS-independent way"""

```python
"""Make it possible to do comparisons and tests in a OS-independent way"""
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, monkeypatch

# Workflow
monkeypatch.setenv('SETUPTOOLS_EXT_SUFFIX', '.mp3')
monkeypatch.setattr('setuptools.command.build_ext.use_stubs', True)
dist = self.dist_with_example()
build_ext = dist.get_command_obj('build_ext')
build_ext.editable_mode = True
build_ext.ensure_finalized()
for ext in build_ext.extensions:
    monkeypatch.setattr(ext, '_needs_stub', True)
build_lib = build_ext.build_lib.replace(os.sep, '/')
mapping = {k.replace(os.sep, '/'): v.replace(os.sep, '/') for k, v in build_ext.get_output_mapping().items()}

def C(file):
    """Make it possible to do comparisons and tests in a OS-independent way"""
    return _compiled_file_name(file).replace(os.sep, '/')
assert mapping == {C(f'{build_lib}/ext3.py'): C('src/ext3.py'), f'{build_lib}/ext3.mp3': 'src/ext3.mp3', C(f'{build_lib}/mypkg/ext1.py'): C('src/mypkg/ext1.py'), f'{build_lib}/mypkg/ext1.mp3': 'src/mypkg/ext1.mp3', C(f'{build_lib}/mypkg/subpkg/ext2.py'): C('src/mypkg/subpkg/ext2.py'), f'{build_lib}/mypkg/subpkg/ext2.mp3': 'src/mypkg/subpkg/ext2.mp3'}
assert f'{build_lib}/mypkg/ext1.py' not in mapping
assert f'{build_lib}/mypkg/subpkg/ext2.py' not in mapping
example_stub = C(f'{build_lib}/mypkg/ext1.py')
assert example_stub in mapping
assert example_stub.startswith(f'{build_lib}/mypkg/__pycache__/ext1')
assert example_stub.endswith('.pyc')
```

## Next Steps


---

*Source: test_build_ext.py:140 | Complexity: Advanced | Last updated: 2026-06-02*