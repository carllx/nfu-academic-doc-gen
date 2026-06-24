# How To: Record Extensions

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test record extensions

## Prerequisites

**Required Modules:**
- `logging`
- `os`
- `pathlib`
- `site`
- `sys`
- `distutils`
- `distutils.command`
- `distutils.command.build_ext`
- `distutils.command.install`
- `distutils.core`
- `distutils.errors`
- `distutils.extension`
- `distutils.tests`
- `distutils.util`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign cmd = missing_compiler_executable(...)

```python
cmd = missing_compiler_executable()
```

**Verification:**
```python
assert found == expected
```

### Step 2: Assign install_dir = self.mkdtemp(...)

```python
install_dir = self.mkdtemp()
```

### Step 3: Assign unknown = self.create_dist(...)

```python
project_dir, dist = self.create_dist(ext_modules=[Extension('xx', ['xxmodule.c'])])
```

### Step 4: Call os.chdir()

```python
os.chdir(project_dir)
```

### Step 5: Call support.copy_xxmodule_c()

```python
support.copy_xxmodule_c(project_dir)
```

### Step 6: Assign buildextcmd = build_ext(...)

```python
buildextcmd = build_ext(dist)
```

### Step 7: Call support.fixup_build_ext()

```python
support.fixup_build_ext(buildextcmd)
```

### Step 8: Call buildextcmd.ensure_finalized()

```python
buildextcmd.ensure_finalized()
```

### Step 9: Assign cmd = install(...)

```python
cmd = install(dist)
```

### Step 10: Assign unknown = cmd

```python
dist.command_obj['install'] = cmd
```

### Step 11: Assign unknown = buildextcmd

```python
dist.command_obj['build_ext'] = buildextcmd
```

### Step 12: Assign cmd.root = install_dir

```python
cmd.root = install_dir
```

### Step 13: Assign cmd.record = os.path.join(...)

```python
cmd.record = os.path.join(project_dir, 'filelist')
```

### Step 14: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 15: Call cmd.run()

```python
cmd.run()
```

### Step 16: Assign content = pathlib.Path.read_text(...)

```python
content = pathlib.Path(cmd.record).read_text(encoding='utf-8')
```

### Step 17: Assign found = value

```python
found = [pathlib.Path(line).name for line in content.splitlines()]
```

### Step 18: Assign expected = value

```python
expected = [_make_ext_name('xx'), 'UNKNOWN-0.0.0-py{}.{}.egg-info'.format(*sys.version_info[:2])]
```

**Verification:**
```python
assert found == expected
```

### Step 19: Call pytest.skip()

```python
pytest.skip(f'The {cmd!r} command is not found')
```


## Complete Example

```python
# Workflow
cmd = missing_compiler_executable()
if cmd is not None:
    pytest.skip(f'The {cmd!r} command is not found')
install_dir = self.mkdtemp()
project_dir, dist = self.create_dist(ext_modules=[Extension('xx', ['xxmodule.c'])])
os.chdir(project_dir)
support.copy_xxmodule_c(project_dir)
buildextcmd = build_ext(dist)
support.fixup_build_ext(buildextcmd)
buildextcmd.ensure_finalized()
cmd = install(dist)
dist.command_obj['install'] = cmd
dist.command_obj['build_ext'] = buildextcmd
cmd.root = install_dir
cmd.record = os.path.join(project_dir, 'filelist')
cmd.ensure_finalized()
cmd.run()
content = pathlib.Path(cmd.record).read_text(encoding='utf-8')
found = [pathlib.Path(line).name for line in content.splitlines()]
expected = [_make_ext_name('xx'), 'UNKNOWN-0.0.0-py{}.{}.egg-info'.format(*sys.version_info[:2])]
assert found == expected
```

## Next Steps


---

*Source: test_install.py:208 | Complexity: Advanced | Last updated: 2026-06-02*