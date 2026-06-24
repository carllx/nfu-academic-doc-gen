# How To: Make Archive Owner Group

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test make archive owner group

## Prerequisites

**Required Modules:**
- `functools`
- `operator`
- `os`
- `pathlib`
- `sys`
- `tarfile`
- `distutils`
- `distutils.archive_util`
- `distutils.spawn`
- `distutils.tests`
- `os.path`
- `path`
- `pytest`
- `test.support`
- `unix_compat`


## Step-by-Step Guide

### Step 1: Assign base_dir = self._create_files(...)

```python
base_dir = self._create_files()
```

**Verification:**
```python
assert os.path.exists(res)
```

### Step 2: Assign root_dir = self.mkdtemp(...)

```python
root_dir = self.mkdtemp()
```

**Verification:**
```python
assert os.path.exists(res)
```

### Step 3: Assign base_name = os.path.join(...)

```python
base_name = os.path.join(self.mkdtemp(), 'archive')
```

**Verification:**
```python
assert os.path.exists(res)
```

### Step 4: Assign res = make_archive(...)

```python
res = make_archive(base_name, 'zip', root_dir, base_dir, owner=owner, group=group)
```

**Verification:**
```python
assert os.path.exists(res)
```

### Step 5: Assign res = make_archive(...)

```python
res = make_archive(base_name, 'zip', root_dir, base_dir)
```

**Verification:**
```python
assert os.path.exists(res)
```

### Step 6: Assign res = make_archive(...)

```python
res = make_archive(base_name, 'tar', root_dir, base_dir, owner=owner, group=group)
```

**Verification:**
```python
assert os.path.exists(res)
```

### Step 7: Assign res = make_archive(...)

```python
res = make_archive(base_name, 'tar', root_dir, base_dir, owner='kjhkjhkjg', group='oihohoh')
```

**Verification:**
```python
assert os.path.exists(res)
```

### Step 8: Assign group = value

```python
group = grp.getgrgid(0)[0]
```

### Step 9: Assign owner = value

```python
owner = pwd.getpwuid(0)[0]
```

### Step 10: Assign group, owner = 'root'

```python
group = owner = 'root'
```


## Complete Example

```python
# Workflow
if UID_0_SUPPORT:
    group = grp.getgrgid(0)[0]
    owner = pwd.getpwuid(0)[0]
else:
    group = owner = 'root'
base_dir = self._create_files()
root_dir = self.mkdtemp()
base_name = os.path.join(self.mkdtemp(), 'archive')
res = make_archive(base_name, 'zip', root_dir, base_dir, owner=owner, group=group)
assert os.path.exists(res)
res = make_archive(base_name, 'zip', root_dir, base_dir)
assert os.path.exists(res)
res = make_archive(base_name, 'tar', root_dir, base_dir, owner=owner, group=group)
assert os.path.exists(res)
res = make_archive(base_name, 'tar', root_dir, base_dir, owner='kjhkjhkjg', group='oihohoh')
assert os.path.exists(res)
```

## Next Steps


---

*Source: test_archive_util.py:285 | Complexity: Advanced | Last updated: 2026-06-02*