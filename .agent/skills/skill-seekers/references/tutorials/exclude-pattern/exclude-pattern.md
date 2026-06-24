# How To: Exclude Pattern

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test exclude pattern

## Prerequisites

**Required Modules:**
- `__future__`
- `contextlib`
- `io`
- `itertools`
- `logging`
- `os`
- `shutil`
- `sys`
- `tempfile`
- `pytest`
- `setuptools.command.egg_info`
- `setuptools.dist`
- `setuptools.tests.textwrap`
- `distutils`
- `distutils.errors`


## Step-by-Step Guide

### Step 1: Assign file_list = FileList(...)

```python
file_list = FileList()
```

**Verification:**
```python
assert not file_list.exclude_pattern('*.py')
```

### Step 2: Assign file_list = FileList(...)

```python
file_list = FileList()
```

**Verification:**
```python
assert file_list.exclude_pattern('*.py')
```

### Step 3: Assign file_list.files = value

```python
file_list.files = ['a.py', 'b.py']
```

**Verification:**
```python
assert file_list.files == ['a.txt']
```

### Step 4: Assign file_list = FileList(...)

```python
file_list = FileList()
```

### Step 5: Assign file_list.files = value

```python
file_list.files = ['a.py', 'a.txt']
```

### Step 6: Call file_list.exclude_pattern()

```python
file_list.exclude_pattern('*.py')
```

### Step 7: Call file_list.sort()

```python
file_list.sort()
```

**Verification:**
```python
assert file_list.files == ['a.txt']
```


## Complete Example

```python
# Workflow
file_list = FileList()
assert not file_list.exclude_pattern('*.py')
file_list = FileList()
file_list.files = ['a.py', 'b.py']
assert file_list.exclude_pattern('*.py')
file_list = FileList()
file_list.files = ['a.py', 'a.txt']
file_list.exclude_pattern('*.py')
file_list.sort()
assert file_list.files == ['a.txt']
```

## Next Steps


---

*Source: test_manifest.py:436 | Complexity: Intermediate | Last updated: 2026-06-02*