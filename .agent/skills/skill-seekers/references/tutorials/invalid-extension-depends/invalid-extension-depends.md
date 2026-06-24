# How To: Invalid Extension Depends

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, pytest, workflow, integration

## Overview

Workflow: Due to backwards compatibility reasons, `Extension.depends` should accept
invalid/weird paths, but then ignore them when building a sdist.

This test verifies that the source distribution is still built
successfully with such paths, but that instead of adding these paths to
the manifest, we emit an informational message, notifying the user that
the invalid path won't be automatically included.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `io`
- `logging`
- `os`
- `pathlib`
- `sys`
- `tarfile`
- `tempfile`
- `unicodedata`
- `inspect`
- `pathlib`
- `unittest`
- `jaraco.path`
- `pytest`
- `setuptools`
- `setuptools._importlib`
- `setuptools.command.egg_info`
- `setuptools.command.sdist`
- `setuptools.dist`
- `setuptools.extension`
- `setuptools.tests`
- `text`
- `distutils`
- `distutils.core`
- `distutils.command.build_py`

**Setup Required:**
```python
# Fixtures: reason, caplog
```

## Step-by-Step Guide

### Step 1: "\n        Due to backwards compatibility reasons, `Extension.depends` should accept\n        invalid/weird paths, but then ignore them when building a sdist.\n\n        This test verifies that the source distribution is still built\n        successfully with such paths, but that instead of adding these paths to\n        the manifest, we emit an informational message, notifying the user that\n        the invalid path won't be automatically included.\n        "

```python
"\n        Due to backwards compatibility reasons, `Extension.depends` should accept\n        invalid/weird paths, but then ignore them when building a sdist.\n\n        This test verifies that the source distribution is still built\n        successfully with such paths, but that instead of adding these paths to\n        the manifest, we emit an informational message, notifying the user that\n        the invalid path won't be automatically included.\n        "
```

**Verification:**
```python
assert invalid_path not in manifest
```

### Step 2: Assign invalid_path = unknown(...)

```python
invalid_path = self._INVALID_PATHS[reason]()
```

**Verification:**
```python
assert len(expected_message) == 1
```

### Step 3: Assign extension = Extension(...)

```python
extension = Extension(name='sdist_test.f', sources=[], depends=[invalid_path])
```

**Verification:**
```python
assert reason in expected_message
```

### Step 4: Assign setup_attrs = value

```python
setup_attrs = {**SETUP_ATTRS, 'ext_modules': [extension]}
```

### Step 5: Assign dist = Distribution(...)

```python
dist = Distribution(setup_attrs)
```

### Step 6: Assign dist.script_name = 'setup.py'

```python
dist.script_name = 'setup.py'
```

### Step 7: Assign cmd = sdist(...)

```python
cmd = sdist(dist)
```

### Step 8: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 9: Call self.assert_package_data_in_manifest()

```python
self.assert_package_data_in_manifest(cmd)
```

### Step 10: Assign manifest = value

```python
manifest = cmd.filelist.files
```

**Verification:**
```python
assert invalid_path not in manifest
```

### Step 11: Assign expected_message = value

```python
expected_message = [message for logger, level, message in caplog.record_tuples if logger == 'root' and level == logging.INFO and (invalid_path in message)]
```

**Verification:**
```python
assert len(expected_message) == 1
```

### Step 12: Assign unknown = expected_message

```python
expected_message, = expected_message
```

**Verification:**
```python
assert reason in expected_message
```

### Step 13: Call cmd.run()

```python
cmd.run()
```


## Complete Example

```python
# Setup
# Fixtures: reason, caplog

# Workflow
"\n        Due to backwards compatibility reasons, `Extension.depends` should accept\n        invalid/weird paths, but then ignore them when building a sdist.\n\n        This test verifies that the source distribution is still built\n        successfully with such paths, but that instead of adding these paths to\n        the manifest, we emit an informational message, notifying the user that\n        the invalid path won't be automatically included.\n        "
invalid_path = self._INVALID_PATHS[reason]()
extension = Extension(name='sdist_test.f', sources=[], depends=[invalid_path])
setup_attrs = {**SETUP_ATTRS, 'ext_modules': [extension]}
dist = Distribution(setup_attrs)
dist.script_name = 'setup.py'
cmd = sdist(dist)
cmd.ensure_finalized()
with quiet(), caplog.at_level(logging.INFO):
    cmd.run()
self.assert_package_data_in_manifest(cmd)
manifest = cmd.filelist.files
assert invalid_path not in manifest
expected_message = [message for logger, level, message in caplog.record_tuples if logger == 'root' and level == logging.INFO and (invalid_path in message)]
assert len(expected_message) == 1
expected_message, = expected_message
assert reason in expected_message
```

## Next Steps


---

*Source: test_sdist.py:273 | Complexity: Advanced | Last updated: 2026-06-02*