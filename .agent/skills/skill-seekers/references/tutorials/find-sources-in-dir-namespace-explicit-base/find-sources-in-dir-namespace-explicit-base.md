# How To: Find Sources In Dir Namespace Explicit Base

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test find sources in dir namespace explicit base

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
assert find_sources_in_dir(finder, '/') == [('pkg.a1.b.c.d.e', '/'), ('pkg.a1.b.f', '/'), ('pkg.a2', '/'), ('pkg.a2.b.c.d.e', '/'), ('pkg.a2.b.f', '/')]
```

### Step 2: Assign options.namespace_packages = True

```python
options.namespace_packages = True
```

**Verification:**
```python
assert find_sources_in_dir(finder, '/') == [('a1.b.c.d.e', '/pkg'), ('a1.b.f', '/pkg'), ('a2', '/pkg'), ('a2.b.c.d.e', '/pkg'), ('a2.b.f', '/pkg')]
```

### Step 3: Assign options.explicit_package_bases = True

```python
options.explicit_package_bases = True
```

### Step 4: Assign options.mypy_path = value

```python
options.mypy_path = ['/']
```

### Step 5: Assign files = value

```python
files = {'/pkg/a1/b/c/d/e.py', '/pkg/a1/b/f.py', '/pkg/a2/__init__.py', '/pkg/a2/b/c/d/e.py', '/pkg/a2/b/f.py'}
```

### Step 6: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache(files), options)
```

**Verification:**
```python
assert find_sources_in_dir(finder, '/') == [('pkg.a1.b.c.d.e', '/'), ('pkg.a1.b.f', '/'), ('pkg.a2', '/'), ('pkg.a2.b.c.d.e', '/'), ('pkg.a2.b.f', '/')]
```

### Step 7: Assign options.mypy_path = value

```python
options.mypy_path = ['/pkg']
```

### Step 8: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache(files), options)
```

**Verification:**
```python
assert find_sources_in_dir(finder, '/') == [('a1.b.c.d.e', '/pkg'), ('a1.b.f', '/pkg'), ('a2', '/pkg'), ('a2.b.c.d.e', '/pkg'), ('a2.b.f', '/pkg')]
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
options.explicit_package_bases = True
options.mypy_path = ['/']
files = {'/pkg/a1/b/c/d/e.py', '/pkg/a1/b/f.py', '/pkg/a2/__init__.py', '/pkg/a2/b/c/d/e.py', '/pkg/a2/b/f.py'}
finder = SourceFinder(FakeFSCache(files), options)
assert find_sources_in_dir(finder, '/') == [('pkg.a1.b.c.d.e', '/'), ('pkg.a1.b.f', '/'), ('pkg.a2', '/'), ('pkg.a2.b.c.d.e', '/'), ('pkg.a2.b.f', '/')]
options.mypy_path = ['/pkg']
finder = SourceFinder(FakeFSCache(files), options)
assert find_sources_in_dir(finder, '/') == [('a1.b.c.d.e', '/pkg'), ('a1.b.f', '/pkg'), ('a2', '/pkg'), ('a2.b.c.d.e', '/pkg'), ('a2.b.f', '/pkg')]
```

## Next Steps


---

*Source: test_find_sources.py:223 | Complexity: Advanced | Last updated: 2026-06-02*