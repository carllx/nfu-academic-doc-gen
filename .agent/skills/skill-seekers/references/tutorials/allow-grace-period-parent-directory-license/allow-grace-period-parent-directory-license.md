# How To: Allow Grace Period Parent Directory License

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test allow grace period parent directory license

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `builtins`
- `importlib`
- `os.path`
- `platform`
- `shutil`
- `stat`
- `struct`
- `sys`
- `sysconfig`
- `contextlib`
- `inspect`
- `zipfile`
- `jaraco.path`
- `pytest`
- `packaging`
- `setuptools`
- `setuptools.command.bdist_wheel`
- `setuptools.dist`
- `setuptools.warnings`
- `distutils.core`
- `setuptools.command.bdist_wheel`
- `wheel.macosx_libfile`

**Setup Required:**
```python
# Fixtures: monkeypatch, tmp_path
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'LICENSE.txt': 'parent license', 'NOTICE.txt': 'parent notice', 'python': {'pyproject.toml': cleandoc('\n                [project]\n                name = "test-proj"\n                dynamic = ["version"]      # <---- testing dynamic will not break\n                [tool.setuptools.dynamic]\n                version.file = "VERSION"\n                '), 'setup.cfg': cleandoc('\n                [metadata]\n                license_files =\n                  ../LICENSE.txt\n                  ../NOTICE.txt\n                '), 'VERSION': '42'}}
```

**Verification:**
```python
assert expected_files <= files_found
```

### Step 2: Call jaraco.path.build()

```python
jaraco.path.build(files, prefix=str(tmp_path))
```

**Verification:**
```python
assert 'License-File: LICENSE.txt' in metadata
```

### Step 3: Call monkeypatch.chdir()

```python
monkeypatch.chdir(tmp_path / 'python')
```

**Verification:**
```python
assert 'License-File: NOTICE.txt' in metadata
```

### Step 4: Assign msg = "Pattern '../.*.txt' cannot contain '..'"

```python
msg = "Pattern '../.*.txt' cannot contain '..'"
```

### Step 5: Call bdist_wheel_cmd.run()

```python
bdist_wheel_cmd().run()
```

### Step 6: Assign files_found = set(...)

```python
files_found = set(wf.namelist())
```

### Step 7: Assign expected_files = value

```python
expected_files = {'test_proj-42.dist-info/licenses/LICENSE.txt', 'test_proj-42.dist-info/licenses/NOTICE.txt'}
```

**Verification:**
```python
assert expected_files <= files_found
```

### Step 8: Assign metadata = wf.read.decode(...)

```python
metadata = wf.read('test_proj-42.dist-info/METADATA').decode('utf8')
```

**Verification:**
```python
assert 'License-File: LICENSE.txt' in metadata
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch, tmp_path

# Workflow
files = {'LICENSE.txt': 'parent license', 'NOTICE.txt': 'parent notice', 'python': {'pyproject.toml': cleandoc('\n                [project]\n                name = "test-proj"\n                dynamic = ["version"]      # <---- testing dynamic will not break\n                [tool.setuptools.dynamic]\n                version.file = "VERSION"\n                '), 'setup.cfg': cleandoc('\n                [metadata]\n                license_files =\n                  ../LICENSE.txt\n                  ../NOTICE.txt\n                '), 'VERSION': '42'}}
jaraco.path.build(files, prefix=str(tmp_path))
monkeypatch.chdir(tmp_path / 'python')
msg = "Pattern '../.*.txt' cannot contain '..'"
with pytest.warns(SetuptoolsDeprecationWarning, match=msg):
    bdist_wheel_cmd().run()
with ZipFile('dist/test_proj-42-py3-none-any.whl') as wf:
    files_found = set(wf.namelist())
    expected_files = {'test_proj-42.dist-info/licenses/LICENSE.txt', 'test_proj-42.dist-info/licenses/NOTICE.txt'}
    assert expected_files <= files_found
    metadata = wf.read('test_proj-42.dist-info/METADATA').decode('utf8')
    assert 'License-File: LICENSE.txt' in metadata
    assert 'License-File: NOTICE.txt' in metadata
```

## Next Steps


---

*Source: test_bdist_wheel.py:666 | Complexity: Advanced | Last updated: 2026-06-02*