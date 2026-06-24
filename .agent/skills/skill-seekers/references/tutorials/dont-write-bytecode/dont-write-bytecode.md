# How To: Dont Write Bytecode

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dont write bytecode

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `sys`
- `distutils.command.build_py`
- `distutils.core`
- `distutils.errors`
- `distutils.tests`
- `jaraco.path`
- `pytest`

**Setup Required:**
```python
# Fixtures: caplog
```

## Step-by-Step Guide

### Step 1: Assign dist = value

```python
dist = self.create_dist()[1]
```

**Verification:**
```python
assert 'byte-compiling is disabled' in caplog.records[0].message
```

### Step 2: Assign cmd = build_py(...)

```python
cmd = build_py(dist)
```

### Step 3: Assign cmd.compile = True

```python
cmd.compile = True
```

### Step 4: Assign cmd.optimize = 1

```python
cmd.optimize = 1
```

### Step 5: Assign old_dont_write_bytecode = value

```python
old_dont_write_bytecode = sys.dont_write_bytecode
```

### Step 6: Assign sys.dont_write_bytecode = True

```python
sys.dont_write_bytecode = True
```

**Verification:**
```python
assert 'byte-compiling is disabled' in caplog.records[0].message
```

### Step 7: Call cmd.byte_compile()

```python
cmd.byte_compile([])
```

### Step 8: Assign sys.dont_write_bytecode = old_dont_write_bytecode

```python
sys.dont_write_bytecode = old_dont_write_bytecode
```


## Complete Example

```python
# Setup
# Fixtures: caplog

# Workflow
dist = self.create_dist()[1]
cmd = build_py(dist)
cmd.compile = True
cmd.optimize = 1
old_dont_write_bytecode = sys.dont_write_bytecode
sys.dont_write_bytecode = True
try:
    cmd.byte_compile([])
finally:
    sys.dont_write_bytecode = old_dont_write_bytecode
assert 'byte-compiling is disabled' in caplog.records[0].message
```

## Next Steps


---

*Source: test_build_py.py:147 | Complexity: Advanced | Last updated: 2026-06-02*