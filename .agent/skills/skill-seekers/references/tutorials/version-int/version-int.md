# How To: Version Int

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test version int

## Prerequisites

**Required Modules:**
- `os`
- `textwrap`
- `distutils`
- `distutils.command.build_scripts`
- `distutils.core`
- `distutils.tests`
- `jaraco.path`
- `sys`


## Step-by-Step Guide

### Step 1: Assign source = self.mkdtemp(...)

```python
source = self.mkdtemp()
```

**Verification:**
```python
assert name in built
```

### Step 2: Assign target = self.mkdtemp(...)

```python
target = self.mkdtemp()
```

### Step 3: Assign expected = self.write_sample_scripts(...)

```python
expected = self.write_sample_scripts(source)
```

### Step 4: Assign cmd = self.get_build_scripts_cmd(...)

```python
cmd = self.get_build_scripts_cmd(target, [os.path.join(source, fn) for fn in expected])
```

### Step 5: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

### Step 6: Assign old = sysconfig.get_config_vars.get(...)

```python
old = sysconfig.get_config_vars().get('VERSION')
```

### Step 7: Assign unknown = 4

```python
sysconfig._config_vars['VERSION'] = 4
```

### Step 8: Assign built = os.listdir(...)

```python
built = os.listdir(target)
```

### Step 9: Call cmd.run()

```python
cmd.run()
```

**Verification:**
```python
assert name in built
```

### Step 10: Assign unknown = old

```python
sysconfig._config_vars['VERSION'] = old
```


## Complete Example

```python
# Workflow
source = self.mkdtemp()
target = self.mkdtemp()
expected = self.write_sample_scripts(source)
cmd = self.get_build_scripts_cmd(target, [os.path.join(source, fn) for fn in expected])
cmd.finalize_options()
old = sysconfig.get_config_vars().get('VERSION')
sysconfig._config_vars['VERSION'] = 4
try:
    cmd.run()
finally:
    if old is not None:
        sysconfig._config_vars['VERSION'] = old
built = os.listdir(target)
for name in expected:
    assert name in built
```

## Next Steps


---

*Source: test_build_scripts.py:71 | Complexity: Advanced | Last updated: 2026-06-02*