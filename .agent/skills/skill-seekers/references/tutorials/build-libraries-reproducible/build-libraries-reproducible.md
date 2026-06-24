# How To: Build Libraries Reproducible

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: test build libraries reproducible

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
assert computed_call_args == mock_newer.call_args[0]
```

### Step 2: Assign cmd = build_clib(...)

```python
cmd = build_clib(dist)
```

### Step 3: Assign cmd.compiler = mock.MagicMock(...)

```python
cmd.compiler = mock.MagicMock(spec=cmd.compiler)
```

### Step 4: Assign mock_newer.return_value = value

```python
mock_newer.return_value = ([], [])
```

### Step 5: Assign original_sources = value

```python
original_sources = ['a-example.c', 'example.c']
```

### Step 6: Assign sources = original_sources

```python
sources = original_sources
```

### Step 7: Assign obj_deps = value

```python
obj_deps = {'': ('global.h',), 'example.c': ('example.h',)}
```

### Step 8: Assign libs = value

```python
libs = [('example', {'sources': sources, 'obj_deps': obj_deps})]
```

### Step 9: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```

### Step 10: Assign computed_call_args = value

```python
computed_call_args = mock_newer.call_args[0]
```

### Step 11: Assign libs = value

```python
libs = [('example', {'sources': sources, 'obj_deps': obj_deps})]
```

### Step 12: Call cmd.build_libraries()

```python
cmd.build_libraries(libs)
```

**Verification:**
```python
assert computed_call_args == mock_newer.call_args[0]
```

### Step 13: Assign sources = random.sample(...)

```python
sources = random.sample(original_sources, len(original_sources))
```


## Complete Example

```python
# Setup
# Fixtures: mock_newer

# Workflow
dist = Distribution()
cmd = build_clib(dist)
cmd.compiler = mock.MagicMock(spec=cmd.compiler)
mock_newer.return_value = ([], [])
original_sources = ['a-example.c', 'example.c']
sources = original_sources
obj_deps = {'': ('global.h',), 'example.c': ('example.h',)}
libs = [('example', {'sources': sources, 'obj_deps': obj_deps})]
cmd.build_libraries(libs)
computed_call_args = mock_newer.call_args[0]
while sources == original_sources:
    sources = random.sample(original_sources, len(original_sources))
libs = [('example', {'sources': sources, 'obj_deps': obj_deps})]
cmd.build_libraries(libs)
assert computed_call_args == mock_newer.call_args[0]
```

## Next Steps


---

*Source: test_build_clib.py:61 | Complexity: Advanced | Last updated: 2026-06-02*