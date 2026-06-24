# How To: Check Metadata

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check metadata

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

### Step 1: Assign cmd = self._run(...)

```python
cmd = self._run()
```

**Verification:**
```python
assert cmd._warnings == 1
```

### Step 2: Assign metadata = value

```python
metadata = {'url': 'xxx', 'author': 'xxx', 'author_email': 'xxx', 'name': 'xxx', 'version': 'xxx'}
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 3: Assign cmd = self._run(...)

```python
cmd = self._run(metadata)
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 4: Assign cmd = self._run(...)

```python
cmd = self._run(metadata, strict=True)
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 5: Assign metadata = value

```python
metadata = {'url': 'xxx', 'author': 'Éric', 'author_email': 'xxx', 'name': 'xxx', 'version': 'xxx', 'description': 'Something about esszet ß', 'long_description': 'More things about esszet ß'}
```

### Step 6: Assign cmd = self._run(...)

```python
cmd = self._run(metadata)
```

**Verification:**
```python
assert cmd._warnings == 0
```

### Step 7: Call self._run()

```python
self._run({}, **{'strict': 1})
```


## Complete Example

```python
# Workflow
cmd = self._run()
assert cmd._warnings == 1
metadata = {'url': 'xxx', 'author': 'xxx', 'author_email': 'xxx', 'name': 'xxx', 'version': 'xxx'}
cmd = self._run(metadata)
assert cmd._warnings == 0
with pytest.raises(DistutilsSetupError):
    self._run({}, **{'strict': 1})
cmd = self._run(metadata, strict=True)
assert cmd._warnings == 0
metadata = {'url': 'xxx', 'author': 'Éric', 'author_email': 'xxx', 'name': 'xxx', 'version': 'xxx', 'description': 'Something about esszet ß', 'long_description': 'More things about esszet ß'}
cmd = self._run(metadata)
assert cmd._warnings == 0
```

## Next Steps


---

*Source: test_check.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*