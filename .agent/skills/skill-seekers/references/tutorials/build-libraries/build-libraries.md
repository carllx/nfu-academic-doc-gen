# How To: Build Libraries

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test build libraries

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `unittest`
- `pytest`
- `setuptools.command.build_clib`
- `setuptools.dist`
- `distutils.errors`

**Setup Required:**
```python
# Fixtures: mock_newer
```

## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution()
```

**Verification:**
```python
assert [['example.c', 'global.h', 'example.h']] in mock_newer.call_args[0]
```

### Step 2: Assign cmd = build_clib(...)

```python
cmd = build_clib(dist)
```

**Verification:**
```python
assert not cmd.compiler.compile.called
```

### Step 3: Assign libs = value

```python
libs = [('example', {'sources': 'broken.c'})]
```

**Verification:**
```python
assert cmd.compiler.create_static_lib.call_count == 1
```

### Step 4: Assign obj_deps = 'some_string'

```python
obj_deps = 'some_string'
```

**Verification:**
```python
assert cmd.compiler.compile.call_count == 1
```

### Step 5: Assign libs = value

```python
libs = [('example', {'sources': ['source.c'], 'obj_deps': obj_deps})]
```

**Verification:**
```python
assert cmd.compiler.create_static_lib.call_count == 1
```

### Step 6: Assign obj_deps = value

```python
obj_deps = {'': ''}
```

### Step 7: Assign libs = value

```python
libs = [('example', {'sources': ['source.c'], 'obj_deps': obj_deps})]
```

### Step 8: Assign obj_deps = value

```python
obj_deps = {'source.c': ''}
```

### Step 9: Assign libs = value

```python
libs = [('example', {'sources': ['source.c'], 'obj_deps': obj_deps})]
```

### Step 10: Assign cmd.compiler = mock.MagicMock(...)

```python
cmd.compiler = mock.MagicMock(spec=cmd.compiler)
```

### Step 11: Assign mock_newer.return_value = value

```python
mock_newer.return_value = ([], [])
```

### Step 12: Assign obj_deps = value

```python
obj_deps = {'': ('global.h',), 'example.c': ('example.h',)}
```

### Step 13: Assign libs = value

```python
libs = [('example', {'sources': ['example.c'], 'obj_deps': obj_deps})]
```

### Step 14: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```

**Verification:**
```python
assert [['example.c', 'global.h', 'example.h']] in mock_newer.call_args[0]
```

### Step 15: Call cmd.compiler.reset_mock()

```python
cmd.compiler.reset_mock()
```

### Step 16: Assign mock_newer.return_value = ''

```python
mock_newer.return_value = ''
```

### Step 17: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```

**Verification:**
```python
assert cmd.compiler.compile.call_count == 1
```

### Step 18: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```

### Step 19: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```

### Step 20: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```

### Step 21: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```


## Complete Example

```python
# Setup
# Fixtures: mock_newer

# Workflow
dist = Distribution()
cmd = build_clib(dist)
libs = [('example', {'sources': 'broken.c'})]
with pytest.raises(DistutilsSetupError):
    cmd.build_libraries(libs)
obj_deps = 'some_string'
libs = [('example', {'sources': ['source.c'], 'obj_deps': obj_deps})]
with pytest.raises(DistutilsSetupError):
    cmd.build_libraries(libs)
obj_deps = {'': ''}
libs = [('example', {'sources': ['source.c'], 'obj_deps': obj_deps})]
with pytest.raises(DistutilsSetupError):
    cmd.build_libraries(libs)
obj_deps = {'source.c': ''}
libs = [('example', {'sources': ['source.c'], 'obj_deps': obj_deps})]
with pytest.raises(DistutilsSetupError):
    cmd.build_libraries(libs)
cmd.compiler = mock.MagicMock(spec=cmd.compiler)
mock_newer.return_value = ([], [])
obj_deps = {'': ('global.h',), 'example.c': ('example.h',)}
libs = [('example', {'sources': ['example.c'], 'obj_deps': obj_deps})]
cmd.build_libraries(libs)
assert [['example.c', 'global.h', 'example.h']] in mock_newer.call_args[0]
assert not cmd.compiler.compile.called
assert cmd.compiler.create_static_lib.call_count == 1
cmd.compiler.reset_mock()
mock_newer.return_value = ''
cmd.build_libraries(libs)
assert cmd.compiler.compile.call_count == 1
assert cmd.compiler.create_static_lib.call_count == 1
```

## Next Steps


---

*Source: test_build_clib.py:14 | Complexity: Advanced | Last updated: 2026-06-02*