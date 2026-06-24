# How To: Setup Requires

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test setup requires

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `importlib`
- `os`
- `re`
- `shutil`
- `signal`
- `sys`
- `tarfile`
- `warnings`
- `concurrent`
- `pathlib`
- `typing`
- `zipfile`
- `pytest`
- `jaraco`
- `packaging.requirements`
- `setuptools.warnings`
- `textwrap`

**Setup Required:**
```python
# Fixtures: setup_literal, requirements, use_wheel, tmpdir_cwd
```

## Step-by-Step Guide

### Step 1: Assign files = value

```python
files = {'setup.py': DALS('\n                from setuptools import setup\n\n                setup(\n                    name="qux",\n                    version="0.0.0",\n                    py_modules=["hello"],\n                    setup_requires={setup_literal},\n                )\n            ').format(setup_literal=setup_literal), 'hello.py': DALS("\n            def run():\n                print('hello')\n            ")}
```

**Verification:**
```python
assert expected == sorted(actual)
```

### Step 2: Call path.build()

```python
path.build(files)
```

### Step 3: Assign build_backend = self.get_build_backend(...)

```python
build_backend = self.get_build_backend()
```

### Step 4: Assign expected = sorted(...)

```python
expected = sorted(requirements)
```

### Step 5: Assign actual = get_requires(...)

```python
actual = get_requires()
```

**Verification:**
```python
assert expected == sorted(actual)
```

### Step 6: Assign get_requires = value

```python
get_requires = build_backend.get_requires_for_build_wheel
```

### Step 7: Assign get_requires = value

```python
get_requires = build_backend.get_requires_for_build_sdist
```


## Complete Example

```python
# Setup
# Fixtures: setup_literal, requirements, use_wheel, tmpdir_cwd

# Workflow
files = {'setup.py': DALS('\n                from setuptools import setup\n\n                setup(\n                    name="qux",\n                    version="0.0.0",\n                    py_modules=["hello"],\n                    setup_requires={setup_literal},\n                )\n            ').format(setup_literal=setup_literal), 'hello.py': DALS("\n            def run():\n                print('hello')\n            ")}
path.build(files)
build_backend = self.get_build_backend()
if use_wheel:
    get_requires = build_backend.get_requires_for_build_wheel
else:
    get_requires = build_backend.get_requires_for_build_sdist
expected = sorted(requirements)
actual = get_requires()
assert expected == sorted(actual)
```

## Next Steps


---

*Source: test_build_meta.py:769 | Complexity: Intermediate | Last updated: 2026-06-02*