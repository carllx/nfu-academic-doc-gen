# How To: Pkg Info Roundtrip

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Ensure PKG-INFO round trips according to pypa/wheel's methodology

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `functools`
- `io`
- `email`
- `email.generator`
- `email.message`
- `email.parser`
- `email.policy`
- `inspect`
- `pathlib`
- `unittest.mock`
- `jaraco.path`
- `pytest`
- `packaging.metadata`
- `setuptools`
- `setuptools._core_metadata`
- `setuptools.config`
- `setuptools.dist`
- `config.downloads`

**Setup Required:**
```python
# Fixtures: tmp_path, dist
```

## Step-by-Step Guide

### Step 1: "Ensure PKG-INFO round trips according to pypa/wheel's methodology"

```python
"Ensure PKG-INFO round trips according to pypa/wheel's methodology"
```

**Verification:**
```python
assert regenerated == raw_metadata
```

### Step 2: Assign pkg_info = _get_pkginfo(...)

```python
pkg_info = _get_pkginfo(dist)
```

### Step 3: Assign serialization_policy = EmailPolicy(...)

```python
serialization_policy = EmailPolicy(utf8=True, mangle_from_=False, max_line_length=0)
```

### Step 4: Assign raw_metadata = bytes(...)

```python
raw_metadata = bytes(pkg_info, 'utf-8')
```

### Step 5: Assign raw_metadata = unknown.join(...)

```python
raw_metadata = b'\n'.join(raw_metadata.splitlines())
```

### Step 6: Assign regenerated = unknown.join(...)

```python
regenerated = b'\n'.join(regenerated.splitlines())
```

**Verification:**
```python
assert regenerated == raw_metadata
```

### Step 7: Assign msg = Parser.parse(...)

```python
msg = Parser(EmailMessage).parse(buffer)
```

### Step 8: Assign out = io.TextIOWrapper(...)

```python
out = io.TextIOWrapper(buffer, encoding='utf-8')
```

### Step 9: Call Generator.flatten()

```python
Generator(out, policy=serialization_policy).flatten(msg)
```

### Step 10: Call out.flush()

```python
out.flush()
```

### Step 11: Assign regenerated = buffer.getvalue(...)

```python
regenerated = buffer.getvalue()
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, dist

# Workflow
"Ensure PKG-INFO round trips according to pypa/wheel's methodology"
pkg_info = _get_pkginfo(dist)
with io.StringIO(pkg_info) as buffer:
    msg = Parser(EmailMessage).parse(buffer)
serialization_policy = EmailPolicy(utf8=True, mangle_from_=False, max_line_length=0)
with io.BytesIO() as buffer:
    out = io.TextIOWrapper(buffer, encoding='utf-8')
    Generator(out, policy=serialization_policy).flatten(msg)
    out.flush()
    regenerated = buffer.getvalue()
raw_metadata = bytes(pkg_info, 'utf-8')
raw_metadata = b'\n'.join(raw_metadata.splitlines())
regenerated = b'\n'.join(regenerated.splitlines())
assert regenerated == raw_metadata
```

## Next Steps


---

*Source: test_core_metadata.py:384 | Complexity: Advanced | Last updated: 2026-06-02*