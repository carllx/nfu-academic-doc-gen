# How To: Compat Install

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compat install

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
# Fixtures: tmp_path, venv
```

## Step-by-Step Guide

### Step 1: Assign opts = value

```python
opts = ['--config-settings', 'editable-mode=compat']
```

**Verification:**
```python
assert '42' in out
```

### Step 2: Assign files = value

```python
files = TestOverallBehaviour.EXAMPLES['custom-layout']
```

**Verification:**
```python
assert expected_path in out
```

### Step 3: Call install_project()

```python
install_project('mypkg', venv, tmp_path, files, *opts)
```

**Verification:**
```python
assert "cannot import name 'subpackage'" in out
```

### Step 4: Assign out = venv.run(...)

```python
out = venv.run(['python', '-c', 'import mypkg.mod1; print(mypkg.mod1.var)'])
```

**Verification:**
```python
assert '42' in out
```

### Step 5: Assign expected_path = comparable_path(...)

```python
expected_path = comparable_path(str(tmp_path))
```

### Step 6: Assign cmd = '    try:\n        from mypkg import subpackage;\n    except ImportError as ex:\n        print(ex)\n    '

```python
cmd = '    try:\n        from mypkg import subpackage;\n    except ImportError as ex:\n        print(ex)\n    '
```

### Step 7: Assign out = venv.run(...)

```python
out = venv.run(['python', '-c', dedent(cmd)])
```

**Verification:**
```python
assert "cannot import name 'subpackage'" in out
```

### Step 8: Assign out = comparable_path(...)

```python
out = comparable_path(venv.run(['python', '-c', cmd]))
```

**Verification:**
```python
assert expected_path in out
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, venv

# Workflow
opts = ['--config-settings', 'editable-mode=compat']
files = TestOverallBehaviour.EXAMPLES['custom-layout']
install_project('mypkg', venv, tmp_path, files, *opts)
out = venv.run(['python', '-c', 'import mypkg.mod1; print(mypkg.mod1.var)'])
assert '42' in out
expected_path = comparable_path(str(tmp_path))
for cmd in ('import otherfile; print(otherfile)', 'import other; print(other)', 'import mypkg; print(mypkg)'):
    out = comparable_path(venv.run(['python', '-c', cmd]))
    assert expected_path in out
cmd = '    try:\n        from mypkg import subpackage;\n    except ImportError as ex:\n        print(ex)\n    '
out = venv.run(['python', '-c', dedent(cmd)])
assert "cannot import name 'subpackage'" in out
```

## Next Steps


---

*Source: test_editable_install.py:1038 | Complexity: Advanced | Last updated: 2026-06-02*