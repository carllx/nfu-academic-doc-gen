# How To: Optional Extension

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test optional extension

## Prerequisites

**Required Modules:**
- `contextlib`
- `glob`
- `importlib`
- `os.path`
- `platform`
- `re`
- `shutil`
- `site`
- `subprocess`
- `sys`
- `tempfile`
- `textwrap`
- `time`
- `distutils`
- `distutils.command.build_ext`
- `distutils.core`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `distutils.tests.support`
- `io`
- `jaraco.path`
- `path`
- `pytest`
- `test`
- `compat`
- `distutils.command`
- `xx`
- `distutils.sysconfig`
- `site`
- `pprint`


## Step-by-Step Guide

### Step 1: Assign modules = value

```python
modules = [Extension('foo', ['xxx'], optional=False)]
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'xx', 'ext_modules': modules})
```

### Step 3: Assign cmd = self.build_ext(...)

```python
cmd = self.build_ext(dist)
```

### Step 4: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 5: Assign modules = value

```python
modules = [Extension('foo', ['xxx'], optional=True)]
```

### Step 6: Assign dist = Distribution(...)

```python
dist = Distribution({'name': 'xx', 'ext_modules': modules})
```

### Step 7: Assign cmd = self.build_ext(...)

```python
cmd = self.build_ext(dist)
```

### Step 8: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 9: Call cmd.run()

```python
cmd.run()
```

### Step 10: Call cmd.run()

```python
cmd.run()
```


## Complete Example

```python
# Workflow
modules = [Extension('foo', ['xxx'], optional=False)]
dist = Distribution({'name': 'xx', 'ext_modules': modules})
cmd = self.build_ext(dist)
cmd.ensure_finalized()
with pytest.raises((UnknownFileError, CompileError)):
    cmd.run()
modules = [Extension('foo', ['xxx'], optional=True)]
dist = Distribution({'name': 'xx', 'ext_modules': modules})
cmd = self.build_ext(dist)
cmd.ensure_finalized()
cmd.run()
```

## Next Steps


---

*Source: test_build_ext.py:235 | Complexity: Advanced | Last updated: 2026-06-02*