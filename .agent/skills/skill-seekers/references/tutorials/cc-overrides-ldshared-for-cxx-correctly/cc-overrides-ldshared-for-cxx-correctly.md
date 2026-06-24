# How To: Cc Overrides Ldshared For Cxx Correctly

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Ensure that setting CC env variable also changes default linker
correctly when building C++ extensions.

pypa/distutils#126

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

### Step 1: '\n        Ensure that setting CC env variable also changes default linker\n        correctly when building C++ extensions.\n\n        pypa/distutils#126\n        '

```python
'\n        Ensure that setting CC env variable also changes default linker\n        correctly when building C++ extensions.\n\n        pypa/distutils#126\n        '
```

**Verification:**
```python
assert self.cc.linker_so[0:2] == ['ccache', 'my_cc']
```

### Step 2: Assign sysconfig.get_config_var = gcv

```python
sysconfig.get_config_var = gcv
```

**Verification:**
```python
assert call_args[:4] == expected
```

### Step 3: Assign sysconfig.get_config_vars = gcvs

```python
sysconfig.get_config_vars = gcvs
```

### Step 4: Assign unknown = 'ccache my_cc'

```python
env['CC'] = 'ccache my_cc'
```

### Step 5: Assign unknown = 'my_cxx'

```python
env['CXX'] = 'my_cxx'
```

### Step 6: Call sysconfig.customize_compiler()

```python
sysconfig.customize_compiler(self.cc)
```

**Verification:**
```python
assert self.cc.linker_so[0:2] == ['ccache', 'my_cc']
```

### Step 7: Call self.cc.link()

```python
self.cc.link(None, [], 'a.out', target_lang='c++')
```

### Step 8: Assign call_args = value

```python
call_args = mock_spawn.call_args[0][0]
```

### Step 9: Assign expected = value

```python
expected = ['my_cxx', '-bundle', '-undefined', 'dynamic_lookup']
```

**Verification:**
```python
assert call_args[:4] == expected
```


## Complete Example

```python
# Workflow
'\n        Ensure that setting CC env variable also changes default linker\n        correctly when building C++ extensions.\n\n        pypa/distutils#126\n        '

def gcv(v):
    if v == 'LDSHARED':
        return 'gcc-4.2 -bundle -undefined dynamic_lookup '
    elif v == 'LDCXXSHARED':
        return 'g++-4.2 -bundle -undefined dynamic_lookup '
    elif v == 'CXX':
        return 'g++-4.2'
    elif v == 'CC':
        return 'gcc-4.2'
    return ''

def gcvs(*args, _orig=sysconfig.get_config_vars):
    if args:
        return list(map(sysconfig.get_config_var, args))
    return _orig()
sysconfig.get_config_var = gcv
sysconfig.get_config_vars = gcvs
with mock.patch.object(self.cc, 'spawn', return_value=None) as mock_spawn, mock.patch.object(self.cc, '_need_link', return_value=True), mock.patch.object(self.cc, 'mkpath', return_value=None), EnvironmentVarGuard() as env:
    env['CC'] = 'ccache my_cc'
    env['CXX'] = 'my_cxx'
    del env['LDSHARED']
    sysconfig.customize_compiler(self.cc)
    assert self.cc.linker_so[0:2] == ['ccache', 'my_cc']
    self.cc.link(None, [], 'a.out', target_lang='c++')
    call_args = mock_spawn.call_args[0][0]
    expected = ['my_cxx', '-bundle', '-undefined', 'dynamic_lookup']
    assert call_args[:4] == expected
```

## Next Steps


---

*Source: test_unix.py:312 | Complexity: Advanced | Last updated: 2026-06-02*