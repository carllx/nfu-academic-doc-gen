# How To: Get Outputs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test get outputs

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
assert outputs == [f'{build_lib}/ext3.mp3', f'{build_lib}/mypkg/ext1.mp3', f'{build_lib}/mypkg/subpkg/ext2.mp3']
```

### Step 2: Call monkeypatch.setattr()

```python
monkeypatch.setattr('setuptools.command.build_ext.use_stubs', False)
```

**Verification:**
```python
assert build_ext.get_output_mapping() == {}
```

### Step 3: Assign dist = self.dist_with_example(...)

```python
dist = self.dist_with_example()
```

**Verification:**
```python
assert mapping == {f'{build_lib}/ext3.mp3': 'src/ext3.mp3', f'{build_lib}/mypkg/ext1.mp3': 'src/mypkg/ext1.mp3', f'{build_lib}/mypkg/subpkg/ext2.mp3': 'src/mypkg/subpkg/ext2.mp3'}
```

### Step 4: Assign build_ext = dist.get_command_obj(...)

```python
build_ext = dist.get_command_obj('build_ext')
```

### Step 5: Assign build_ext.editable_mode = False

```python
build_ext.editable_mode = False
```

### Step 6: Call build_ext.ensure_finalized()

```python
build_ext.ensure_finalized()
```

### Step 7: Assign build_lib = build_ext.build_lib.replace(...)

```python
build_lib = build_ext.build_lib.replace(os.sep, '/')
```

### Step 8: Assign outputs = value

```python
outputs = [x.replace(os.sep, '/') for x in build_ext.get_outputs()]
```

**Verification:**
```python
assert outputs == [f'{build_lib}/ext3.mp3', f'{build_lib}/mypkg/ext1.mp3', f'{build_lib}/mypkg/subpkg/ext2.mp3']
```

### Step 9: Call dist.reinitialize_command()

```python
dist.reinitialize_command('build_ext')
```

### Step 10: Assign build_ext.editable_mode = True

```python
build_ext.editable_mode = True
```

### Step 11: Call build_ext.ensure_finalized()

```python
build_ext.ensure_finalized()
```

### Step 12: Assign mapping = value

```python
mapping = {k.replace(os.sep, '/'): v.replace(os.sep, '/') for k, v in build_ext.get_output_mapping().items()}
```

**Verification:**
```python
assert mapping == {f'{build_lib}/ext3.mp3': 'src/ext3.mp3', f'{build_lib}/mypkg/ext1.mp3': 'src/mypkg/ext1.mp3', f'{build_lib}/mypkg/subpkg/ext2.mp3': 'src/mypkg/subpkg/ext2.mp3'}
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, monkeypatch

# Workflow
monkeypatch.setenv('SETUPTOOLS_EXT_SUFFIX', '.mp3')
monkeypatch.setattr('setuptools.command.build_ext.use_stubs', False)
dist = self.dist_with_example()
build_ext = dist.get_command_obj('build_ext')
build_ext.editable_mode = False
build_ext.ensure_finalized()
build_lib = build_ext.build_lib.replace(os.sep, '/')
outputs = [x.replace(os.sep, '/') for x in build_ext.get_outputs()]
assert outputs == [f'{build_lib}/ext3.mp3', f'{build_lib}/mypkg/ext1.mp3', f'{build_lib}/mypkg/subpkg/ext2.mp3']
assert build_ext.get_output_mapping() == {}
dist.reinitialize_command('build_ext')
build_ext.editable_mode = True
build_ext.ensure_finalized()
mapping = {k.replace(os.sep, '/'): v.replace(os.sep, '/') for k, v in build_ext.get_output_mapping().items()}
assert mapping == {f'{build_lib}/ext3.mp3': 'src/ext3.mp3', f'{build_lib}/mypkg/ext1.mp3': 'src/mypkg/ext1.mp3', f'{build_lib}/mypkg/subpkg/ext2.mp3': 'src/mypkg/subpkg/ext2.mp3'}
```

## Next Steps


---

*Source: test_build_ext.py:108 | Complexity: Advanced | Last updated: 2026-06-02*