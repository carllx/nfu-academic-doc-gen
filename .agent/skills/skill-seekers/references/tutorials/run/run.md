# How To: Run

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test run

## Prerequisites

**Required Modules:**
- `os`
- `distutils.command.build_clib`
- `distutils.errors`
- `distutils.tests`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign unknown = self.create_dist(...)

```python
pkg_dir, dist = self.create_dist()
```

**Verification:**
```python
assert 'libfoo.a' in os.listdir(build_temp)
```

### Step 2: Assign cmd = build_clib(...)

```python
cmd = build_clib(dist)
```

### Step 3: Assign foo_c = os.path.join(...)

```python
foo_c = os.path.join(pkg_dir, 'foo.c')
```

### Step 4: Call self.write_file()

```python
self.write_file(foo_c, 'int main(void) { return 1;}\n')
```

### Step 5: Assign cmd.libraries = value

```python
cmd.libraries = [('foo', {'sources': [foo_c]})]
```

### Step 6: Assign build_temp = os.path.join(...)

```python
build_temp = os.path.join(pkg_dir, 'build')
```

### Step 7: Call os.mkdir()

```python
os.mkdir(build_temp)
```

### Step 8: Assign cmd.build_temp = build_temp

```python
cmd.build_temp = build_temp
```

### Step 9: Assign cmd.build_clib = build_temp

```python
cmd.build_clib = build_temp
```

### Step 10: Assign ccmd = missing_compiler_executable(...)

```python
ccmd = missing_compiler_executable()
```

### Step 11: Call cmd.run()

```python
cmd.run()
```

**Verification:**
```python
assert 'libfoo.a' in os.listdir(build_temp)
```

### Step 12: Call self.skipTest()

```python
self.skipTest(f'The {ccmd!r} command is not found')
```


## Complete Example

```python
# Workflow
pkg_dir, dist = self.create_dist()
cmd = build_clib(dist)
foo_c = os.path.join(pkg_dir, 'foo.c')
self.write_file(foo_c, 'int main(void) { return 1;}\n')
cmd.libraries = [('foo', {'sources': [foo_c]})]
build_temp = os.path.join(pkg_dir, 'build')
os.mkdir(build_temp)
cmd.build_temp = build_temp
cmd.build_clib = build_temp
ccmd = missing_compiler_executable()
if ccmd is not None:
    self.skipTest(f'The {ccmd!r} command is not found')
cmd.run()
assert 'libfoo.a' in os.listdir(build_temp)
```

## Next Steps


---

*Source: test_build_clib.py:111 | Complexity: Advanced | Last updated: 2026-06-02*