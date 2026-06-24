# How To: Round Trip Through Email Generator

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: In pypa/setuptools#4033, it was shown that once PKG-INFO is
re-generated using ``email.generator.Generator``, some control
characters might cause problems.

## Prerequisites

**Required Modules:**
- `email`
- `email.generator`
- `email.policy`
- `functools`
- `io`
- `os`
- `sys`
- `textwrap`
- `unittest.mock`
- `warnings`
- `distutils.cmd`
- `distutils.dist`
- `distutils.tests`
- `typing`
- `jaraco.path`
- `pytest`
- `distutils.tests.test_dist`


## Step-by-Step Guide

### Step 1: '\n        In pypa/setuptools#4033, it was shown that once PKG-INFO is\n        re-generated using ``email.generator.Generator``, some control\n        characters might cause problems.\n        '

```python
'\n        In pypa/setuptools#4033, it was shown that once PKG-INFO is\n        re-generated using ``email.generator.Generator``, some control\n        characters might cause problems.\n        '
```

**Verification:**
```python
assert regen_desc == orig_desc
```

### Step 2: Assign attrs = value

```python
attrs = {'name': 'package', 'version': '1.0', 'long_description': 'hello\x0b\nworld\n'}
```

### Step 3: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

### Step 4: Assign metadata = value

```python
metadata = dist.metadata
```

### Step 5: Assign orig = email.message_from_string(...)

```python
orig = email.message_from_string(msg)
```

### Step 6: Assign policy = email.policy.EmailPolicy(...)

```python
policy = email.policy.EmailPolicy(utf8=True, mangle_from_=False, max_line_length=0)
```

### Step 7: Assign orig_desc = set(...)

```python
orig_desc = set(orig['Description'].splitlines())
```

### Step 8: Assign regen_desc = set(...)

```python
regen_desc = set(regen['Description'].splitlines())
```

**Verification:**
```python
assert regen_desc == orig_desc
```

### Step 9: Call metadata.write_pkg_file()

```python
metadata.write_pkg_file(buffer)
```

### Step 10: Assign msg = buffer.getvalue(...)

```python
msg = buffer.getvalue()
```

### Step 11: Call email.generator.Generator.flatten()

```python
email.generator.Generator(buffer, policy=policy).flatten(orig)
```

### Step 12: Call buffer.seek()

```python
buffer.seek(0)
```

### Step 13: Assign regen = email.message_from_file(...)

```python
regen = email.message_from_file(buffer)
```


## Complete Example

```python
# Workflow
'\n        In pypa/setuptools#4033, it was shown that once PKG-INFO is\n        re-generated using ``email.generator.Generator``, some control\n        characters might cause problems.\n        '
attrs = {'name': 'package', 'version': '1.0', 'long_description': 'hello\x0b\nworld\n'}
dist = Distribution(attrs)
metadata = dist.metadata
with io.StringIO() as buffer:
    metadata.write_pkg_file(buffer)
    msg = buffer.getvalue()
orig = email.message_from_string(msg)
policy = email.policy.EmailPolicy(utf8=True, mangle_from_=False, max_line_length=0)
with io.StringIO() as buffer:
    email.generator.Generator(buffer, policy=policy).flatten(orig)
    buffer.seek(0)
    regen = email.message_from_file(buffer)
orig_desc = set(orig['Description'].splitlines())
regen_desc = set(regen['Description'].splitlines())
assert regen_desc == orig_desc
```

## Next Steps


---

*Source: test_dist.py:516 | Complexity: Advanced | Last updated: 2026-06-02*