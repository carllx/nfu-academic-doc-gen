# How To: Verbosity Level

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Make sure the correct verbosity level is set (issue #3038)

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `inspect`
- `logging`
- `sys`
- `pytest`
- `setuptools`
- `distutils`
- `_distutils_hack`
- `setuptools.logging`
- `distutils`

**Setup Required:**
```python
# Fixtures: tmp_path, monkeypatch, flags, expected_level
```

## Step-by-Step Guide

### Step 1: 'Make sure the correct verbosity level is set (issue #3038)'

```python
'Make sure the correct verbosity level is set (issue #3038)'
```

**Verification:**
```python
assert logging.getLevelName(unset_log_level) == 'NOTSET'
```

### Step 2: Assign logger = logging.Logger(...)

```python
logger = logging.Logger(__name__)
```

**Verification:**
```python
assert log_level_name == expected_level
```

### Step 3: Call monkeypatch.setattr()

```python
monkeypatch.setattr(logging, 'root', logger)
```

### Step 4: Assign unset_log_level = logger.getEffectiveLevel(...)

```python
unset_log_level = logger.getEffectiveLevel()
```

**Verification:**
```python
assert logging.getLevelName(unset_log_level) == 'NOTSET'
```

### Step 5: Assign setup_script = value

```python
setup_script = tmp_path / 'setup.py'
```

### Step 6: Call setup_script.write_text()

```python
setup_script.write_text(setup_py, encoding='utf-8')
```

### Step 7: Assign dist = distutils.core.run_setup(...)

```python
dist = distutils.core.run_setup(setup_script, stop_after='init')
```

### Step 8: Assign dist.script_args = value

```python
dist.script_args = flags + ['sdist']
```

### Step 9: Call dist.parse_command_line()

```python
dist.parse_command_line()
```

### Step 10: Assign log_level = logger.getEffectiveLevel(...)

```python
log_level = logger.getEffectiveLevel()
```

### Step 11: Assign log_level_name = logging.getLevelName(...)

```python
log_level_name = logging.getLevelName(log_level)
```

**Verification:**
```python
assert log_level_name == expected_level
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, monkeypatch, flags, expected_level

# Workflow
'Make sure the correct verbosity level is set (issue #3038)'
import setuptools
import distutils
logger = logging.Logger(__name__)
monkeypatch.setattr(logging, 'root', logger)
unset_log_level = logger.getEffectiveLevel()
assert logging.getLevelName(unset_log_level) == 'NOTSET'
setup_script = tmp_path / 'setup.py'
setup_script.write_text(setup_py, encoding='utf-8')
dist = distutils.core.run_setup(setup_script, stop_after='init')
dist.script_args = flags + ['sdist']
dist.parse_command_line()
log_level = logger.getEffectiveLevel()
log_level_name = logging.getLevelName(log_level)
assert log_level_name == expected_level
```

## Next Steps


---

*Source: test_logging.py:24 | Complexity: Advanced | Last updated: 2026-06-02*