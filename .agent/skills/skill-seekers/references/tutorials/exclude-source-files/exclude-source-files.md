# How To: Exclude Source Files

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test exclude source files

## Prerequisites

**Required Modules:**
- `os`
- `re`
- `zipfile`
- `pytest`
- `setuptools.dist`


## Step-by-Step Guide

### Step 1: Assign dist = Distribution(...)

```python
dist = Distribution(dict(script_name='setup.py', script_args=['bdist_egg', '--exclude-source-files'], py_modules=['hi']))
```

**Verification:**
```python
assert 'hi.pyc' in names
```

### Step 2: Assign unknown = os.listdir(...)

```python
[dist_name] = os.listdir('dist')
```

**Verification:**
```python
assert 'hi.py' not in names
```

### Step 3: Assign dist_filename = os.path.join(...)

```python
dist_filename = os.path.join('dist', dist_name)
```

### Step 4: Assign zip = zipfile.ZipFile(...)

```python
zip = zipfile.ZipFile(dist_filename)
```

### Step 5: Assign names = list(...)

```python
names = list((zi.filename for zi in zip.filelist))
```

**Verification:**
```python
assert 'hi.pyc' in names
```

### Step 6: Call dist.parse_command_line()

```python
dist.parse_command_line()
```

### Step 7: Call dist.run_commands()

```python
dist.run_commands()
```


## Complete Example

```python
# Workflow
dist = Distribution(dict(script_name='setup.py', script_args=['bdist_egg', '--exclude-source-files'], py_modules=['hi']))
with contexts.quiet():
    dist.parse_command_line()
    dist.run_commands()
[dist_name] = os.listdir('dist')
dist_filename = os.path.join('dist', dist_name)
zip = zipfile.ZipFile(dist_filename)
names = list((zi.filename for zi in zip.filelist))
assert 'hi.pyc' in names
assert 'hi.py' not in names
```

## Next Steps


---

*Source: test_bdist_egg.py:57 | Complexity: Intermediate | Last updated: 2026-06-02*