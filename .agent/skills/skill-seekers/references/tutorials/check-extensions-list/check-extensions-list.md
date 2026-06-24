# How To: Check Extensions List

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check extensions list

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

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert isinstance(ext, Extension)
```

### Step 2: Assign cmd = self.build_ext(...)

```python
cmd = self.build_ext(dist)
```

**Verification:**
```python
assert ext.libraries == 'foo'
```

### Step 3: Call cmd.finalize_options()

```python
cmd.finalize_options()
```

**Verification:**
```python
assert not hasattr(ext, 'some')
```

### Step 4: Assign exts = value

```python
exts = [('bar', 'foo', 'bar'), 'foo']
```

**Verification:**
```python
assert exts[0].undef_macros == ['3']
```

### Step 5: Assign exts = value

```python
exts = [('foo-bar', '')]
```

**Verification:**
```python
assert exts[0].define_macros == [('1', '2')]
```

### Step 6: Assign exts = value

```python
exts = [('foo.bar', '')]
```

### Step 7: Assign exts = value

```python
exts = [('foo.bar', {'sources': [''], 'libraries': 'foo', 'some': 'bar'})]
```

### Step 8: Call cmd.check_extensions_list()

```python
cmd.check_extensions_list(exts)
```

### Step 9: Assign ext = value

```python
ext = exts[0]
```

**Verification:**
```python
assert isinstance(ext, Extension)
```

### Step 10: Assign exts = value

```python
exts = [('foo.bar', {'sources': [''], 'libraries': 'foo', 'some': 'bar', 'macros': [('1', '2', '3'), 'foo']})]
```

### Step 11: Assign unknown = value

```python
exts[0][1]['macros'] = [('1', '2'), ('3',)]
```

### Step 12: Call cmd.check_extensions_list()

```python
cmd.check_extensions_list(exts)
```

**Verification:**
```python
assert exts[0].undef_macros == ['3']
```

### Step 13: Call cmd.check_extensions_list()

```python
cmd.check_extensions_list('foo')
```

### Step 14: Call cmd.check_extensions_list()

```python
cmd.check_extensions_list(exts)
```

### Step 15: Call cmd.check_extensions_list()

```python
cmd.check_extensions_list(exts)
```

### Step 16: Call cmd.check_extensions_list()

```python
cmd.check_extensions_list(exts)
```

### Step 17: Call cmd.check_extensions_list()

```python
cmd.check_extensions_list(exts)
```


## Complete Example

```python
# Workflow
dist = Distribution()
cmd = self.build_ext(dist)
cmd.finalize_options()
with pytest.raises(DistutilsSetupError):
    cmd.check_extensions_list('foo')
exts = [('bar', 'foo', 'bar'), 'foo']
with pytest.raises(DistutilsSetupError):
    cmd.check_extensions_list(exts)
exts = [('foo-bar', '')]
with pytest.raises(DistutilsSetupError):
    cmd.check_extensions_list(exts)
exts = [('foo.bar', '')]
with pytest.raises(DistutilsSetupError):
    cmd.check_extensions_list(exts)
exts = [('foo.bar', {'sources': [''], 'libraries': 'foo', 'some': 'bar'})]
cmd.check_extensions_list(exts)
ext = exts[0]
assert isinstance(ext, Extension)
assert ext.libraries == 'foo'
assert not hasattr(ext, 'some')
exts = [('foo.bar', {'sources': [''], 'libraries': 'foo', 'some': 'bar', 'macros': [('1', '2', '3'), 'foo']})]
with pytest.raises(DistutilsSetupError):
    cmd.check_extensions_list(exts)
exts[0][1]['macros'] = [('1', '2'), ('3',)]
cmd.check_extensions_list(exts)
assert exts[0].undef_macros == ['3']
assert exts[0].define_macros == [('1', '2')]
```

## Next Steps


---

*Source: test_build_ext.py:323 | Complexity: Advanced | Last updated: 2026-06-02*