# How To: Explicit Ldshared

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test explicit ldshared

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `unittest.mock`
- `distutils`
- `distutils.compat`
- `distutils.errors`
- `distutils.tests`
- `distutils.tests.compat.py39`
- `distutils.util`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign sysconfig.get_config_var = gcv

```python
sysconfig.get_config_var = gcv
```

**Verification:**
```python
assert self.cc.linker_so[0] == 'my_ld'
```

### Step 2: Assign sysconfig.get_config_vars = gcvs

```python
sysconfig.get_config_vars = gcvs
```

**Verification:**
```python
assert self.cc.linker_so[0] == 'my_ld'
```

### Step 3: Assign unknown = 'my_cc'

```python
env['CC'] = 'my_cc'
```

### Step 4: Assign unknown = 'my_ld -bundle -dynamic'

```python
env['LDSHARED'] = 'my_ld -bundle -dynamic'
```

### Step 5: Call sysconfig.customize_compiler()

```python
sysconfig.customize_compiler(self.cc)
```


## Complete Example

```python
# Workflow
def gcv(v):
    if v == 'LDSHARED':
        return 'gcc-4.2 -bundle -undefined dynamic_lookup '
    return 'gcc-4.2'

def gcvs(*args, _orig=sysconfig.get_config_vars):
    if args:
        return list(map(sysconfig.get_config_var, args))
    return _orig()
sysconfig.get_config_var = gcv
sysconfig.get_config_vars = gcvs
with EnvironmentVarGuard() as env:
    env['CC'] = 'my_cc'
    env['LDSHARED'] = 'my_ld -bundle -dynamic'
    sysconfig.customize_compiler(self.cc)
assert self.cc.linker_so[0] == 'my_ld'
```

## Next Steps


---

*Source: test_unix.py:355 | Complexity: Intermediate | Last updated: 2026-06-02*