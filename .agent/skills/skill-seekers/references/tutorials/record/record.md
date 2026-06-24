# How To: Record

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test record

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

### Step 1: Assign install_dir = self.mkdtemp(...)

```python
install_dir = self.mkdtemp()
```

**Verification:**
```python
assert found == expected
```

### Step 2: Assign unknown = self.create_dist(...)

```python
project_dir, dist = self.create_dist(py_modules=['hello'], scripts=['sayhi'])
```

### Step 3: Call os.chdir()

```python
os.chdir(project_dir)
```

### Step 4: Call self.write_file()

```python
self.write_file('hello.py', "def main(): print('o hai')")
```

### Step 5: Call self.write_file()

```python
self.write_file('sayhi', 'from hello import main; main()')
```

### Step 6: Assign cmd = install(...)

```python
cmd = install(dist)
```

### Step 7: Assign unknown = cmd

```python
dist.command_obj['install'] = cmd
```

### Step 8: Assign cmd.root = install_dir

```python
cmd.root = install_dir
```

### Step 9: Assign cmd.record = os.path.join(...)

```python
cmd.record = os.path.join(project_dir, 'filelist')
```

### Step 10: Call cmd.ensure_finalized()

```python
cmd.ensure_finalized()
```

### Step 11: Call cmd.run()

```python
cmd.run()
```

### Step 12: Assign content = pathlib.Path.read_text(...)

```python
content = pathlib.Path(cmd.record).read_text(encoding='utf-8')
```

### Step 13: Assign found = value

```python
found = [pathlib.Path(line).name for line in content.splitlines()]
```

### Step 14: Assign expected = value

```python
expected = ['hello.py', f'hello.{sys.implementation.cache_tag}.pyc', 'sayhi', 'UNKNOWN-0.0.0-py{}.{}.egg-info'.format(*sys.version_info[:2])]
```

**Verification:**
```python
assert found == expected
```


## Complete Example

```python
# Workflow
install_dir = self.mkdtemp()
project_dir, dist = self.create_dist(py_modules=['hello'], scripts=['sayhi'])
os.chdir(project_dir)
self.write_file('hello.py', "def main(): print('o hai')")
self.write_file('sayhi', 'from hello import main; main()')
cmd = install(dist)
dist.command_obj['install'] = cmd
cmd.root = install_dir
cmd.record = os.path.join(project_dir, 'filelist')
cmd.ensure_finalized()
cmd.run()
content = pathlib.Path(cmd.record).read_text(encoding='utf-8')
found = [pathlib.Path(line).name for line in content.splitlines()]
expected = ['hello.py', f'hello.{sys.implementation.cache_tag}.pyc', 'sayhi', 'UNKNOWN-0.0.0-py{}.{}.egg-info'.format(*sys.version_info[:2])]
assert found == expected
```

## Next Steps


---

*Source: test_install.py:183 | Complexity: Advanced | Last updated: 2026-06-02*