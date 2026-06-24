# How To: Stub Only Package

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test stub only package

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `shutil`
- `stat`
- `warnings`
- `pathlib`
- `unittest.mock`
- `jaraco.path`
- `pytest`
- `setuptools`
- `setuptools.dist`
- `textwrap`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd
```

## Step-by-Step Guide

### Step 1: Assign structure = value

```python
structure = {'pyproject.toml': DALS('\n                [project]\n                name = "foo-stubs"\n                version = "1"\n                '), 'foo-stubs': {'__init__.pyi': '', 'bar.pyi': ''}}
```

**Verification:**
```python
assert expected_type_files <= outputs
```

### Step 2: Assign expected_type_files = value

```python
expected_type_files = {'foo-stubs/__init__.pyi', 'foo-stubs/bar.pyi'}
```

### Step 3: Call jaraco.path.build()

```python
jaraco.path.build(structure)
```

### Step 4: Assign build_py = get_finalized_build_py(...)

```python
build_py = get_finalized_build_py()
```

### Step 5: Assign outputs = get_outputs(...)

```python
outputs = get_outputs(build_py)
```

**Verification:**
```python
assert expected_type_files <= outputs
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd

# Workflow
structure = {'pyproject.toml': DALS('\n                [project]\n                name = "foo-stubs"\n                version = "1"\n                '), 'foo-stubs': {'__init__.pyi': '', 'bar.pyi': ''}}
expected_type_files = {'foo-stubs/__init__.pyi', 'foo-stubs/bar.pyi'}
jaraco.path.build(structure)
build_py = get_finalized_build_py()
outputs = get_outputs(build_py)
assert expected_type_files <= outputs
```

## Next Steps


---

*Source: test_build_py.py:448 | Complexity: Intermediate | Last updated: 2026-06-02*