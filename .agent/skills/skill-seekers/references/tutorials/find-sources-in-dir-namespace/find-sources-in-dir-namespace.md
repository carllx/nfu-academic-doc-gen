# How To: Find Sources In Dir Namespace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test find sources in dir namespace

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `os`
- `shutil`
- `tempfile`
- `unittest`
- `pytest`
- `mypy.find_sources`
- `mypy.fscache`
- `mypy.modulefinder`
- `mypy.options`

**Setup Required:**
```python
self.tempdir = tempfile.mkdtemp()
self.oldcwd = os.getcwd()
os.chdir(self.tempdir)
```

## Step-by-Step Guide

### Step 1: Assign options = Options(...)

```python
options = Options()
```

**Verification:**
```python
assert find_sources_in_dir(finder, '/') == [('a2', '/pkg'), ('a2.b.c.d.e', '/pkg'), ('a2.b.f', '/pkg'), ('e', '/pkg/a1/b/c/d'), ('f', '/pkg/a1/b')]
```

### Step 2: Assign options.namespace_packages = True

```python
options.namespace_packages = True
```

### Step 3: Assign files = value

```python
files = {'/pkg/a1/b/c/d/e.py', '/pkg/a1/b/f.py', '/pkg/a2/__init__.py', '/pkg/a2/b/c/d/e.py', '/pkg/a2/b/f.py'}
```

### Step 4: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache(files), options)
```

**Verification:**
```python
assert find_sources_in_dir(finder, '/') == [('a2', '/pkg'), ('a2.b.c.d.e', '/pkg'), ('a2.b.f', '/pkg'), ('e', '/pkg/a1/b/c/d'), ('f', '/pkg/a1/b')]
```


## Complete Example

```python
# Setup
self.tempdir = tempfile.mkdtemp()
self.oldcwd = os.getcwd()
os.chdir(self.tempdir)

# Workflow
options = Options()
options.namespace_packages = True
files = {'/pkg/a1/b/c/d/e.py', '/pkg/a1/b/f.py', '/pkg/a2/__init__.py', '/pkg/a2/b/c/d/e.py', '/pkg/a2/b/f.py'}
finder = SourceFinder(FakeFSCache(files), options)
assert find_sources_in_dir(finder, '/') == [('a2', '/pkg'), ('a2.b.c.d.e', '/pkg'), ('a2.b.f', '/pkg'), ('e', '/pkg/a1/b/c/d'), ('f', '/pkg/a1/b')]
```

## Next Steps


---

*Source: test_find_sources.py:203 | Complexity: Intermediate | Last updated: 2026-06-02*