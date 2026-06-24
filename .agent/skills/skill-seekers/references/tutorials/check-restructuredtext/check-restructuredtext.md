# How To: Check Restructuredtext

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check restructuredtext

## Prerequisites

**Required Modules:**
- `os`
- `textwrap`
- `distutils.command.check`
- `distutils.errors`
- `distutils.tests`
- `pytest`
- `pygments`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('docutils')
```

**Verification:**
```python
assert cmd._warnings == 1
```

### Step 2: Assign broken_rest = 'title\n===\n\ntest'

```python
broken_rest = 'title\n===\n\ntest'
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 3: Assign unknown = self.create_dist(...)

```python
pkg_info, dist = self.create_dist(long_description=broken_rest)
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 4: Assign cmd = check(...)

```python
cmd = check(dist)
```

### Step 5: Call cmd.check_restructuredtext()

```python
cmd.check_restructuredtext()
```

**Verification:**
```python
assert cmd._warnings == 1
```

### Step 6: Assign metadata = value

```python
metadata = {'url': 'xxx', 'author': 'xxx', 'author_email': 'xxx', 'name': 'xxx', 'version': 'xxx', 'long_description': broken_rest}
```

### Step 7: Assign unknown = 'title\n=====\n\ntest ß'

```python
metadata['long_description'] = 'title\n=====\n\ntest ß'
```

### Step 8: Assign cmd = self._run(...)

```python
cmd = self._run(metadata, strict=True, restructuredtext=True)
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 9: Assign unknown = 'title\n=====\n\n.. include:: includetest.rst'

```python
metadata['long_description'] = 'title\n=====\n\n.. include:: includetest.rst'
```

### Step 10: Assign cmd = self._run(...)

```python
cmd = self._run(metadata, cwd=HERE, strict=True, restructuredtext=True)
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 11: Call self._run()

```python
self._run(metadata, **{'strict': 1, 'restructuredtext': 1})
```


## Complete Example

```python
# Workflow
pytest.importorskip('docutils')
broken_rest = 'title\n===\n\ntest'
pkg_info, dist = self.create_dist(long_description=broken_rest)
cmd = check(dist)
cmd.check_restructuredtext()
assert cmd._warnings == 1
metadata = {'url': 'xxx', 'author': 'xxx', 'author_email': 'xxx', 'name': 'xxx', 'version': 'xxx', 'long_description': broken_rest}
with pytest.raises(DistutilsSetupError):
    self._run(metadata, **{'strict': 1, 'restructuredtext': 1})
metadata['long_description'] = 'title\n=====\n\ntest ß'
cmd = self._run(metadata, strict=True, restructuredtext=True)
assert cmd._warnings == 0
metadata['long_description'] = 'title\n=====\n\n.. include:: includetest.rst'
cmd = self._run(metadata, cwd=HERE, strict=True, restructuredtext=True)
assert cmd._warnings == 0
```

## Next Steps


---

*Source: test_check.py:120 | Complexity: Advanced | Last updated: 2026-06-02*