# How To: Find Library File

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test find library file

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `unittest.mock`
- `distutils`
- `distutils.compat`
- `distutils.errors`
- `distutils.tests`
- `distutils.tests.compat.py39`
- `distutils.util`
- `pytest`

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign compiler = unix.Compiler(...)

```python
compiler = unix.Compiler()
```

**Verification:**
```python
assert compiler.find_library_file(dirs, 'abc').replace('\\', '/') == f'/foo/bar/existing/{libname}'
```

### Step 2: Assign compiler._library_root = value

```python
compiler._library_root = lambda dir: dir
```

**Verification:**
```python
assert compiler.find_library_file(reversed(dirs), 'abc').replace('\\', '/') == f'/foo/bar/existing/{libname}'
```

### Step 3: Call monkeypatch.setattr()

```python
monkeypatch.setattr(os.path, 'exists', lambda d: 'existing' in d)
```

**Verification:**
```python
assert compiler.find_library_file(dirs, 'abc').replace('\\', '/') == '/foo/bar/existing/libabc.a'
```

### Step 4: Assign libname = value

```python
libname = 'libabc.dylib' if sys.platform != 'cygwin' else 'cygabc.dll'
```

**Verification:**
```python
assert compiler.find_library_file(reversed(dirs), 'abc').replace('\\', '/') == '/foo/bar/existing/libabc.a'
```

### Step 5: Assign dirs = value

```python
dirs = ('/foo/bar/missing', '/foo/bar/existing')
```

**Verification:**
```python
assert compiler.find_library_file(dirs, 'abc').replace('\\', '/') == f'/foo/bar/existing/{libname}'
```

### Step 6: Call monkeypatch.setattr()

```python
monkeypatch.setattr(os.path, 'exists', lambda d: 'existing' in d and '.a' in d and ('.dll.a' not in d))
```

**Verification:**
```python
assert compiler.find_library_file(dirs, 'abc').replace('\\', '/') == '/foo/bar/existing/libabc.a'
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
compiler = unix.Compiler()
compiler._library_root = lambda dir: dir
monkeypatch.setattr(os.path, 'exists', lambda d: 'existing' in d)
libname = 'libabc.dylib' if sys.platform != 'cygwin' else 'cygabc.dll'
dirs = ('/foo/bar/missing', '/foo/bar/existing')
assert compiler.find_library_file(dirs, 'abc').replace('\\', '/') == f'/foo/bar/existing/{libname}'
assert compiler.find_library_file(reversed(dirs), 'abc').replace('\\', '/') == f'/foo/bar/existing/{libname}'
monkeypatch.setattr(os.path, 'exists', lambda d: 'existing' in d and '.a' in d and ('.dll.a' not in d))
assert compiler.find_library_file(dirs, 'abc').replace('\\', '/') == '/foo/bar/existing/libabc.a'
assert compiler.find_library_file(reversed(dirs), 'abc').replace('\\', '/') == '/foo/bar/existing/libabc.a'
```

## Next Steps


---

*Source: test_unix.py:385 | Complexity: Intermediate | Last updated: 2026-06-02*