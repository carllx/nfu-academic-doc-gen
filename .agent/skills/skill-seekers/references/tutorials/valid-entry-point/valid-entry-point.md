# How To: Valid Entry Point

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test valid entry point

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
assert '[abc]\nfoo = bar:baz\n' in content
```

### Step 2: Assign dist.entry_points = value

```python
dist.entry_points = {'abc': 'foo = bar:baz', 'def': ['faa = bor:boz']}
```

**Verification:**
```python
assert '[def]\nfaa = bor:boz\n' in content
```

### Step 3: Assign cmd = dist.get_command_obj(...)

```python
cmd = dist.get_command_obj('egg_info')
```

### Step 4: Call write_entries()

```python
write_entries(cmd, 'entry_points', 'entry_points.txt')
```

### Step 5: Assign content = Path.read_text(...)

```python
content = Path('entry_points.txt').read_text(encoding='utf-8')
```

**Verification:**
```python
assert '[abc]\nfoo = bar:baz\n' in content
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd, env

# Workflow
dist = Distribution({'name': 'foo', 'version': '0.0.1'})
dist.entry_points = {'abc': 'foo = bar:baz', 'def': ['faa = bor:boz']}
cmd = dist.get_command_obj('egg_info')
write_entries(cmd, 'entry_points', 'entry_points.txt')
content = Path('entry_points.txt').read_text(encoding='utf-8')
assert '[abc]\nfoo = bar:baz\n' in content
assert '[def]\nfaa = bor:boz\n' in content
```

## Next Steps


---

*Source: test_egg_info.py:1296 | Complexity: Advanced | Last updated: 2026-06-02*