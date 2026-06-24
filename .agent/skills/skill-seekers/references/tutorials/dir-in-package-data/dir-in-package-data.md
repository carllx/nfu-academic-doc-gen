# How To: Dir In Package Data

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: A directory in package_data should not be added to the filelist.

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `distutils.command.build_py`
- `distutils.core`
- `distutils.errors`
- `distutils.tests`
- `jaraco.path`
- `pytest`


## Step-by-Step Guide

### Step 1: '\n        A directory in package_data should not be added to the filelist.\n        '

```python
'\n        A directory in package_data should not be added to the filelist.\n        '
```

### Step 2: Assign sources = self.mkdtemp(...)

```python
sources = self.mkdtemp()
```

### Step 3: Call jaraco.path.build()

```python
jaraco.path.build({'pkg': {'__init__.py': '', 'doc': {'testfile': '', 'otherdir': {}}}}, sources)
```

### Step 4: Call os.chdir()

```python
os.chdir(sources)
```

### Step 5: Assign dist = Distribution(...)

```python
dist = Distribution({'packages': ['pkg'], 'package_data': {'pkg': ['doc/*']}})
```

### Step 6: Assign dist.script_name = os.path.join(...)

```python
dist.script_name = os.path.join(sources, 'setup.py')
```

### Step 7: Assign dist.script_args = value

```python
dist.script_args = ['build']
```

### Step 8: Call dist.parse_command_line()

```python
dist.parse_command_line()
```

### Step 9: Call dist.run_commands()

```python
dist.run_commands()
```

### Step 10: Call self.fail()

```python
self.fail('failed package_data when data dir includes a dir')
```


## Complete Example

```python
# Workflow
'\n        A directory in package_data should not be added to the filelist.\n        '
sources = self.mkdtemp()
jaraco.path.build({'pkg': {'__init__.py': '', 'doc': {'testfile': '', 'otherdir': {}}}}, sources)
os.chdir(sources)
dist = Distribution({'packages': ['pkg'], 'package_data': {'pkg': ['doc/*']}})
dist.script_name = os.path.join(sources, 'setup.py')
dist.script_args = ['build']
dist.parse_command_line()
try:
    dist.run_commands()
except DistutilsFileError:
    self.fail('failed package_data when data dir includes a dir')
```

## Next Steps


---

*Source: test_build_py.py:115 | Complexity: Advanced | Last updated: 2026-06-02*