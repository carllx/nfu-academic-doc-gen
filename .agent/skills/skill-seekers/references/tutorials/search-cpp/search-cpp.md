# How To: Search Cpp

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test search cpp

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `distutils._log`
- `distutils.command.config`
- `distutils.tests`
- `more_itertools`
- `path`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign cmd = missing_compiler_executable(...)

```python
cmd = missing_compiler_executable(['preprocessor'])
```

**Verification:**
```python
assert match == 0
```

### Step 2: Assign unknown = self.create_dist(...)

```python
pkg_dir, dist = self.create_dist()
```

**Verification:**
```python
assert match == 1
```

### Step 3: Assign cmd = config(...)

```python
cmd = config(dist)
```

### Step 4: Call cmd._check_compiler()

```python
cmd._check_compiler()
```

### Step 5: Assign compiler = value

```python
compiler = cmd.compiler
```

### Step 6: Assign match = cmd.search_cpp(...)

```python
match = cmd.search_cpp(pattern='xxx', body='/* xxx */')
```

**Verification:**
```python
assert match == 0
```

### Step 7: Assign match = cmd.search_cpp(...)

```python
match = cmd.search_cpp(pattern='_configtest', body='/* xxx */')
```

**Verification:**
```python
assert match == 1
```

### Step 8: Call self.skipTest()

```python
self.skipTest(f'The {cmd!r} command is not found')
```

### Step 9: Call self.skipTest()

```python
self.skipTest('xlc: The -E option overrides the -P, -o, and -qsyntaxonly options')
```


## Complete Example

```python
# Workflow
cmd = missing_compiler_executable(['preprocessor'])
if cmd is not None:
    self.skipTest(f'The {cmd!r} command is not found')
pkg_dir, dist = self.create_dist()
cmd = config(dist)
cmd._check_compiler()
compiler = cmd.compiler
if sys.platform[:3] == 'aix' and 'xlc' in compiler.preprocessor[0].lower():
    self.skipTest('xlc: The -E option overrides the -P, -o, and -qsyntaxonly options')
match = cmd.search_cpp(pattern='xxx', body='/* xxx */')
assert match == 0
match = cmd.search_cpp(pattern='_configtest', body='/* xxx */')
assert match == 1
```

## Next Steps


---

*Source: test_config_cmd.py:36 | Complexity: Advanced | Last updated: 2026-06-02*