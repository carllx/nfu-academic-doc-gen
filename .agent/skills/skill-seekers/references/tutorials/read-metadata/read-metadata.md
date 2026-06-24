# How To: Read Metadata

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read metadata

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

### Step 1: Assign attrs = value

```python
attrs = {'name': 'package', 'version': '1.0', 'long_description': 'desc', 'description': 'xxx', 'download_url': 'http://example.com', 'keywords': ['one', 'two'], 'requires': ['foo']}
```

**Verification:**
```python
assert metadata.name == 'package'
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

**Verification:**
```python
assert metadata.version == '1.0'
```

### Step 3: Assign metadata = value

```python
metadata = dist.metadata
```

**Verification:**
```python
assert metadata.description == 'xxx'
```

### Step 4: Assign PKG_INFO = io.StringIO(...)

```python
PKG_INFO = io.StringIO()
```

**Verification:**
```python
assert metadata.download_url == 'http://example.com'
```

### Step 5: Call metadata.write_pkg_file()

```python
metadata.write_pkg_file(PKG_INFO)
```

**Verification:**
```python
assert metadata.keywords == ['one', 'two']
```

### Step 6: Call PKG_INFO.seek()

```python
PKG_INFO.seek(0)
```

**Verification:**
```python
assert metadata.platforms is None
```

### Step 7: Call metadata.read_pkg_file()

```python
metadata.read_pkg_file(PKG_INFO)
```

**Verification:**
```python
assert metadata.obsoletes is None
```


## Complete Example

```python
# Workflow
attrs = {'name': 'package', 'version': '1.0', 'long_description': 'desc', 'description': 'xxx', 'download_url': 'http://example.com', 'keywords': ['one', 'two'], 'requires': ['foo']}
dist = Distribution(attrs)
metadata = dist.metadata
PKG_INFO = io.StringIO()
metadata.write_pkg_file(PKG_INFO)
PKG_INFO.seek(0)
metadata.read_pkg_file(PKG_INFO)
assert metadata.name == 'package'
assert metadata.version == '1.0'
assert metadata.description == 'xxx'
assert metadata.download_url == 'http://example.com'
assert metadata.keywords == ['one', 'two']
assert metadata.platforms is None
assert metadata.obsoletes is None
assert metadata.requires == ['foo']
```

## Next Steps


---

*Source: test_dist.py:487 | Complexity: Intermediate | Last updated: 2026-06-02*