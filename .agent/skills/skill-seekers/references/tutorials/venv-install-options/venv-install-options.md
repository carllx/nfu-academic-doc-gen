# How To: Venv Install Options

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: test venv install options

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
sys.argv.append('install')
```

**Verification:**
```python
assert sorted(d.command_options.get('install').keys()) == sorted(result_dict.keys())
```

### Step 2: Assign file = str(...)

```python
file = str(tmp_path / 'file')
```

**Verification:**
```python
assert value == result_dict[key]
```

### Step 3: Assign fakepath = '/somedir'

```python
fakepath = '/somedir'
```

**Verification:**
```python
assert key not in d.command_options.get('install', {})
```

### Step 4: Call jaraco.path.build()

```python
jaraco.path.build({file: f'\n                    [install]\n                    install-base = {fakepath}\n                    install-platbase = {fakepath}\n                    install-lib = {fakepath}\n                    install-platlib = {fakepath}\n                    install-purelib = {fakepath}\n                    install-headers = {fakepath}\n                    install-scripts = {fakepath}\n                    install-data = {fakepath}\n                    prefix = {fakepath}\n                    exec-prefix = {fakepath}\n                    home = {fakepath}\n                    user = {fakepath}\n                    root = {fakepath}\n                    '})
```

### Step 5: Assign option_tuple = value

```python
option_tuple = (file, fakepath)
```

### Step 6: Assign result_dict = value

```python
result_dict = {'install_base': option_tuple, 'install_platbase': option_tuple, 'install_lib': option_tuple, 'install_platlib': option_tuple, 'install_purelib': option_tuple, 'install_headers': option_tuple, 'install_scripts': option_tuple, 'install_data': option_tuple, 'prefix': option_tuple, 'exec_prefix': option_tuple, 'home': option_tuple, 'user': option_tuple, 'root': option_tuple}
```

**Verification:**
```python
assert sorted(d.command_options.get('install').keys()) == sorted(result_dict.keys())
```

### Step 7: Assign d = self.create_distribution(...)

```python
d = self.create_distribution([file])
```

**Verification:**
```python
assert value == result_dict[key]
```

### Step 8: Assign d = self.create_distribution(...)

```python
d = self.create_distribution([file])
```

**Verification:**
```python
assert key not in d.command_options.get('install', {})
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, clear_argv

# Workflow
sys.argv.append('install')
file = str(tmp_path / 'file')
fakepath = '/somedir'
jaraco.path.build({file: f'\n                    [install]\n                    install-base = {fakepath}\n                    install-platbase = {fakepath}\n                    install-lib = {fakepath}\n                    install-platlib = {fakepath}\n                    install-purelib = {fakepath}\n                    install-headers = {fakepath}\n                    install-scripts = {fakepath}\n                    install-data = {fakepath}\n                    prefix = {fakepath}\n                    exec-prefix = {fakepath}\n                    home = {fakepath}\n                    user = {fakepath}\n                    root = {fakepath}\n                    '})
with mock.patch.multiple(sys, prefix='/a', base_prefix='/a'):
    d = self.create_distribution([file])
option_tuple = (file, fakepath)
result_dict = {'install_base': option_tuple, 'install_platbase': option_tuple, 'install_lib': option_tuple, 'install_platlib': option_tuple, 'install_purelib': option_tuple, 'install_headers': option_tuple, 'install_scripts': option_tuple, 'install_data': option_tuple, 'prefix': option_tuple, 'exec_prefix': option_tuple, 'home': option_tuple, 'user': option_tuple, 'root': option_tuple}
assert sorted(d.command_options.get('install').keys()) == sorted(result_dict.keys())
for key, value in d.command_options.get('install').items():
    assert value == result_dict[key]
with mock.patch.multiple(sys, prefix='/a', base_prefix='/b'):
    d = self.create_distribution([file])
for key in result_dict.keys():
    assert key not in d.command_options.get('install', {})
```

## Next Steps


---

*Source: test_dist.py:92 | Complexity: Advanced | Last updated: 2026-06-02*