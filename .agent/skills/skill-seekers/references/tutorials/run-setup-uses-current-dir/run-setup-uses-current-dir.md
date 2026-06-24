# How To: Run Setup Uses Current Dir

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that the setup script is run with the current directory
as its own current directory.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `distutils.core`
- `io`
- `os`
- `sys`
- `distutils.dist`
- `pytest`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: '\n        Test that the setup script is run with the current directory\n        as its own current directory.\n        '

```python
'\n        Test that the setup script is run with the current directory\n        as its own current directory.\n        '
```

**Verification:**
```python
assert cwd == output
```

### Step 2: Assign sys.stdout = io.StringIO(...)

```python
sys.stdout = io.StringIO()
```

### Step 3: Assign cwd = os.getcwd(...)

```python
cwd = os.getcwd()
```

### Step 4: Assign setup_py = value

```python
setup_py = tmp_path / 'setup.py'
```

### Step 5: Call setup_py.write_text()

```python
setup_py.write_text(setup_prints_cwd, encoding='utf-8')
```

### Step 6: Call distutils.core.run_setup()

```python
distutils.core.run_setup(setup_py)
```

### Step 7: Assign output = sys.stdout.getvalue(...)

```python
output = sys.stdout.getvalue()
```

**Verification:**
```python
assert cwd == output
```

### Step 8: Assign output = value

```python
output = output[:-1]
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'\n        Test that the setup script is run with the current directory\n        as its own current directory.\n        '
sys.stdout = io.StringIO()
cwd = os.getcwd()
setup_py = tmp_path / 'setup.py'
setup_py.write_text(setup_prints_cwd, encoding='utf-8')
distutils.core.run_setup(setup_py)
output = sys.stdout.getvalue()
if output.endswith('\n'):
    output = output[:-1]
assert cwd == output
```

## Next Steps


---

*Source: test_core.py:90 | Complexity: Advanced | Last updated: 2026-06-02*