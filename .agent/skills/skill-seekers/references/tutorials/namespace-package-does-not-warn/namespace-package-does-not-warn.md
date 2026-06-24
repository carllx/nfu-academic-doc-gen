# How To: Namespace Package Does Not Warn

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Originally distutils implementation did not account for PEP 420
and included warns for package directories that did not contain
``__init__.py`` files.
After the acceptance of PEP 420, these warnings don't make more sense
so we want to ensure there are not displayed to not confuse the users.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `distutils.command.build_py`
- `distutils.core`
- `distutils.errors`
- `distutils.tests`
- `jaraco.path`
- `pytest`

**Setup Required:**
```python
# Fixtures: caplog
```

## Step-by-Step Guide

### Step 1: "\n        Originally distutils implementation did not account for PEP 420\n        and included warns for package directories that did not contain\n        ``__init__.py`` files.\n        After the acceptance of PEP 420, these warnings don't make more sense\n        so we want to ensure there are not displayed to not confuse the users.\n        "

```python
"\n        Originally distutils implementation did not account for PEP 420\n        and included warns for package directories that did not contain\n        ``__init__.py`` files.\n        After the acceptance of PEP 420, these warnings don't make more sense\n        so we want to ensure there are not displayed to not confuse the users.\n        "
```

**Verification:**
```python
assert len(modules) == 1
```

### Step 2: Assign tmp = self.mkdtemp(...)

```python
tmp = self.mkdtemp()
```

**Verification:**
```python
assert module_path.replace(os.sep, '/') == 'ns/pkg/module.py'
```

### Step 3: Call jaraco.path.build()

```python
jaraco.path.build({'ns': {'pkg': {'module.py': ''}}}, tmp)
```

**Verification:**
```python
assert not any(('package init file' in msg and 'not found' in msg for msg in caplog.messages))
```

### Step 4: Call os.chdir()

```python
os.chdir(tmp)
```

### Step 5: Assign attrs = value

```python
attrs = {'name': 'ns.pkg', 'packages': ['ns', 'ns.pkg'], 'script_name': 'setup.py'}
```

### Step 6: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

### Step 7: Assign cmd = dist.get_command_obj(...)

```python
cmd = dist.get_command_obj('build_py')
```

### Step 8: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 9: Assign modules = cmd.find_all_modules(...)

```python
modules = cmd.find_all_modules()
```

**Verification:**
```python
assert len(modules) == 1
```

### Step 10: Assign module_path = value

```python
module_path = modules[0][-1]
```

**Verification:**
```python
assert module_path.replace(os.sep, '/') == 'ns/pkg/module.py'
```

### Step 11: Call cmd.run()

```python
cmd.run()
```

**Verification:**
```python
assert not any(('package init file' in msg and 'not found' in msg for msg in caplog.messages))
```


## Complete Example

```python
# Setup
# Fixtures: caplog

# Workflow
"\n        Originally distutils implementation did not account for PEP 420\n        and included warns for package directories that did not contain\n        ``__init__.py`` files.\n        After the acceptance of PEP 420, these warnings don't make more sense\n        so we want to ensure there are not displayed to not confuse the users.\n        "
tmp = self.mkdtemp()
jaraco.path.build({'ns': {'pkg': {'module.py': ''}}}, tmp)
os.chdir(tmp)
attrs = {'name': 'ns.pkg', 'packages': ['ns', 'ns.pkg'], 'script_name': 'setup.py'}
dist = Distribution(attrs)
cmd = dist.get_command_obj('build_py')
cmd.finalize_options()
modules = cmd.find_all_modules()
assert len(modules) == 1
module_path = modules[0][-1]
assert module_path.replace(os.sep, '/') == 'ns/pkg/module.py'
cmd.run()
assert not any(('package init file' in msg and 'not found' in msg for msg in caplog.messages))
```

## Next Steps


---

*Source: test_build_py.py:163 | Complexity: Advanced | Last updated: 2026-06-02*