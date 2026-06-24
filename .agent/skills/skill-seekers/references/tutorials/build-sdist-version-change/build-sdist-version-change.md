# How To: Build Sdist Version Change

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test build sdist version change

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
# Fixtures: build_backend
```

## Step-by-Step Guide

### Step 1: Assign sdist_into_directory = os.path.abspath(...)

```python
sdist_into_directory = os.path.abspath('out_sdist')
```

**Verification:**
```python
assert os.path.isfile(os.path.join(sdist_into_directory, sdist_name))
```

### Step 2: Call os.makedirs()

```python
os.makedirs(sdist_into_directory)
```

**Verification:**
```python
assert os.path.isfile(os.path.join(os.path.abspath('out_sdist'), sdist_name))
```

### Step 3: Assign sdist_name = build_backend.build_sdist(...)

```python
sdist_name = build_backend.build_sdist(sdist_into_directory)
```

**Verification:**
```python
assert os.path.isfile(os.path.join(sdist_into_directory, sdist_name))
```

### Step 4: Assign setup_loc = os.path.abspath(...)

```python
setup_loc = os.path.abspath('setup.py')
```

### Step 5: Call shutil.rmtree()

```python
shutil.rmtree(sdist_into_directory)
```

### Step 6: Call os.makedirs()

```python
os.makedirs(sdist_into_directory)
```

### Step 7: Assign sdist_name = build_backend.build_sdist(...)

```python
sdist_name = build_backend.build_sdist('out_sdist')
```

**Verification:**
```python
assert os.path.isfile(os.path.join(os.path.abspath('out_sdist'), sdist_name))
```

### Step 8: Assign setup_loc = os.path.abspath(...)

```python
setup_loc = os.path.abspath('setup.cfg')
```

### Step 9: Assign content = file_handler.read(...)

```python
content = file_handler.read()
```

### Step 10: Call file_handler.write()

```python
file_handler.write(content.replace("version='0.0.0'", "version='0.0.1'"))
```


## Complete Example

```python
# Setup
# Fixtures: build_backend

# Workflow
sdist_into_directory = os.path.abspath('out_sdist')
os.makedirs(sdist_into_directory)
sdist_name = build_backend.build_sdist(sdist_into_directory)
assert os.path.isfile(os.path.join(sdist_into_directory, sdist_name))
setup_loc = os.path.abspath('setup.py')
if not os.path.exists(setup_loc):
    setup_loc = os.path.abspath('setup.cfg')
with open(setup_loc, 'rt', encoding='utf-8') as file_handler:
    content = file_handler.read()
with open(setup_loc, 'wt', encoding='utf-8') as file_handler:
    file_handler.write(content.replace("version='0.0.0'", "version='0.0.1'"))
shutil.rmtree(sdist_into_directory)
os.makedirs(sdist_into_directory)
sdist_name = build_backend.build_sdist('out_sdist')
assert os.path.isfile(os.path.join(os.path.abspath('out_sdist'), sdist_name))
```

## Next Steps


---

*Source: test_build_meta.py:567 | Complexity: Advanced | Last updated: 2026-06-02*