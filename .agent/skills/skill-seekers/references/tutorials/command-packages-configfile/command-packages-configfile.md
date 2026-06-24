# How To: Command Packages Configfile

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test command packages configfile

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `email`
- `email.generator`
- `email.policy`
- `functools`
- `io`
- `os`
- `sys`
- `textwrap`
- `unittest.mock`
- `warnings`
- `distutils.cmd`
- `distutils.dist`
- `distutils.tests`
- `typing`
- `jaraco.path`
- `pytest`
- `distutils.tests.test_dist`

**Setup Required:**
```python
# Fixtures: tmp_path, clear_argv
```

## Step-by-Step Guide

### Step 1: Call sys.argv.append()

```python
sys.argv.append('build')
```

**Verification:**
```python
assert d.get_command_packages() == ['distutils.command', 'foo.bar', 'splat']
```

### Step 2: Assign file = str(...)

```python
file = str(tmp_path / 'file')
```

**Verification:**
```python
assert d.get_command_packages() == ['distutils.command', 'spork']
```

### Step 3: Call jaraco.path.build()

```python
jaraco.path.build({file: '\n                    [global]\n                    command_packages = foo.bar, splat\n                    '})
```

**Verification:**
```python
assert d.get_command_packages() == ['distutils.command']
```

### Step 4: Assign d = self.create_distribution(...)

```python
d = self.create_distribution([file])
```

**Verification:**
```python
assert d.get_command_packages() == ['distutils.command', 'foo.bar', 'splat']
```

### Step 5: Assign unknown = value

```python
sys.argv[1:] = ['--command-packages', 'spork', 'build']
```

### Step 6: Assign d = self.create_distribution(...)

```python
d = self.create_distribution([file])
```

**Verification:**
```python
assert d.get_command_packages() == ['distutils.command', 'spork']
```

### Step 7: Assign unknown = value

```python
sys.argv[1:] = ['--command-packages', '', 'build']
```

### Step 8: Assign d = self.create_distribution(...)

```python
d = self.create_distribution([file])
```

**Verification:**
```python
assert d.get_command_packages() == ['distutils.command']
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, clear_argv

# Workflow
sys.argv.append('build')
file = str(tmp_path / 'file')
jaraco.path.build({file: '\n                    [global]\n                    command_packages = foo.bar, splat\n                    '})
d = self.create_distribution([file])
assert d.get_command_packages() == ['distutils.command', 'foo.bar', 'splat']
sys.argv[1:] = ['--command-packages', 'spork', 'build']
d = self.create_distribution([file])
assert d.get_command_packages() == ['distutils.command', 'spork']
sys.argv[1:] = ['--command-packages', '', 'build']
d = self.create_distribution([file])
assert d.get_command_packages() == ['distutils.command']
```

## Next Steps


---

*Source: test_dist.py:153 | Complexity: Advanced | Last updated: 2026-06-02*