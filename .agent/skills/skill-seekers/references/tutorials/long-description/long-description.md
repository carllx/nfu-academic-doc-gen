# How To: Long Description

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test long description

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

### Step 1: Assign long_desc = textwrap.dedent(...)

```python
long_desc = textwrap.dedent('        example::\n              We start here\n            and continue here\n          and end here.')
```

**Verification:**
```python
assert long_desc in meta
```

### Step 2: Assign attrs = value

```python
attrs = {'name': 'package', 'version': '1.0', 'long_description': long_desc}
```

### Step 3: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

### Step 4: Assign meta = self.format_metadata(...)

```python
meta = self.format_metadata(dist)
```

### Step 5: Assign meta = meta.replace(...)

```python
meta = meta.replace('\n' + 8 * ' ', '\n')
```

**Verification:**
```python
assert long_desc in meta
```


## Complete Example

```python
# Workflow
long_desc = textwrap.dedent('        example::\n              We start here\n            and continue here\n          and end here.')
attrs = {'name': 'package', 'version': '1.0', 'long_description': long_desc}
dist = Distribution(attrs)
meta = self.format_metadata(dist)
meta = meta.replace('\n' + 8 * ' ', '\n')
assert long_desc in meta
```

## Next Steps


---

*Source: test_dist.py:438 | Complexity: Intermediate | Last updated: 2026-06-02*