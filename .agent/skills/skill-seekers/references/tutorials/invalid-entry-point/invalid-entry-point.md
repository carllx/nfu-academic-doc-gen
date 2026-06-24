# How To: Invalid Entry Point

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test invalid entry point

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `ast`
- `glob`
- `os`
- `re`
- `stat`
- `sys`
- `time`
- `pathlib`
- `unittest`
- `pytest`
- `jaraco`
- `setuptools`
- `setuptools.command.egg_info`
- `setuptools.dist`
- `textwrap`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd, env
```

## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'foo', 'version': '0.0.1'})
```

**Verification:**
```python
assert 'ensure entry-point follows the spec' in ex.value.args[0]
```

### Step 2: Assign dist.entry_points = value

```python
dist.entry_points = {'foo': 'foo = invalid-identifier:foo'}
```

**Verification:**
```python
assert 'invalid-identifier' in str(ex.value)
```

### Step 3: Assign cmd = dist.get_command_obj(...)

```python
cmd = dist.get_command_obj('egg_info')
```

### Step 4: Assign expected_msg = '(Invalid object reference|Problems to parse)'

```python
expected_msg = '(Invalid object reference|Problems to parse)'
```

### Step 5: Call write_entries()

```python
write_entries(cmd, 'entry_points', 'entry_points.txt')
```

**Verification:**
```python
assert 'ensure entry-point follows the spec' in ex.value.args[0]
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, env

# Workflow
dist = Distribution({'name': 'foo', 'version': '0.0.1'})
dist.entry_points = {'foo': 'foo = invalid-identifier:foo'}
cmd = dist.get_command_obj('egg_info')
expected_msg = '(Invalid object reference|Problems to parse)'
with pytest.raises((errors.OptionError, ValueError), match=expected_msg) as ex:
    write_entries(cmd, 'entry_points', 'entry_points.txt')
    assert 'ensure entry-point follows the spec' in ex.value.args[0]
    assert 'invalid-identifier' in str(ex.value)
```

## Next Steps


---

*Source: test_egg_info.py:1286 | Complexity: Advanced | Last updated: 2026-06-02*