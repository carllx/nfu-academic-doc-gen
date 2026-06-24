# How To: Type Files Can Be Excluded

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test type files can be excluded

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
# Fixtures: tmpdir_cwd, pyproject, example
```

## Step-by-Step Guide

### Step 1: Assign structure = value

```python
structure = {**self.EXAMPLES[example]['directory_structure'], 'pyproject.toml': self.PYPROJECTS[pyproject]}
```

**Verification:**
```python
assert expected_type_files.isdisjoint(outputs)
```

### Step 2: Assign expected_type_files = value

```python
expected_type_files = self.EXAMPLES[example]['expected_type_files']
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
assert expected_type_files.isdisjoint(outputs)
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, pyproject, example

# Workflow
structure = {**self.EXAMPLES[example]['directory_structure'], 'pyproject.toml': self.PYPROJECTS[pyproject]}
expected_type_files = self.EXAMPLES[example]['expected_type_files']
jaraco.path.build(structure)
build_py = get_finalized_build_py()
outputs = get_outputs(build_py)
assert expected_type_files.isdisjoint(outputs)
```

## Next Steps


---

*Source: test_build_py.py:436 | Complexity: Intermediate | Last updated: 2026-06-02*