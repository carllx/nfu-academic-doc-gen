# How To: Crawl Namespace Explicit Base

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test crawl namespace explicit base

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
assert crawl(finder, '/setup.py') == ('setup', '/')
```

### Step 2: Assign options.namespace_packages = True

```python
options.namespace_packages = True
```

**Verification:**
```python
assert crawl(finder, '/a/setup.py') == ('setup', '/a')
```

### Step 3: Assign options.explicit_package_bases = True

```python
options.explicit_package_bases = True
```

**Verification:**
```python
assert crawl(finder, '/a/b/setup.py') == ('setup', '/a/b')
```

### Step 4: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/setup.py') == ('a.setup', '/')
```

### Step 5: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/invalid-name/setup.py') == ('setup', '/a/invalid-name')
```

### Step 6: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/setup.py') == ('a.b.setup', '/')
```

### Step 7: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/setup.py', '/a/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('a.b.c.setup', '/')
```

### Step 8: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/invalid-name/setup.py', '/a/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('c.setup', '/a/b')
```

### Step 9: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/setup.py', '/a/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('c.setup', '/a/b')
```

### Step 10: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py', '/a/__init__.py', '/a/b/c/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('setup', '/a/b/c')
```

### Step 11: Assign options.mypy_path = value

```python
options.mypy_path = ['/a/b']
```

### Step 12: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('c.setup', '/a/b')
```

### Step 13: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py', '/a/__init__.py', '/a/b/c/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('c.setup', '/a/b')
```

### Step 14: Assign options.mypy_path = value

```python
options.mypy_path = ['/a/b', '/a/b/c']
```

### Step 15: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('setup', '/a/b/c')
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
finder = SourceFinder(FakeFSCache({'/setup.py'}), options)
assert crawl(finder, '/setup.py') == ('setup', '/')
finder = SourceFinder(FakeFSCache({'/a/setup.py'}), options)
assert crawl(finder, '/a/setup.py') == ('setup', '/a')
finder = SourceFinder(FakeFSCache({'/a/b/setup.py'}), options)
assert crawl(finder, '/a/b/setup.py') == ('setup', '/a/b')
finder = SourceFinder(FakeFSCache({'/a/setup.py', '/a/__init__.py'}), options)
assert crawl(finder, '/a/setup.py') == ('a.setup', '/')
finder = SourceFinder(FakeFSCache({'/a/invalid-name/setup.py', '/a/__init__.py'}), options)
assert crawl(finder, '/a/invalid-name/setup.py') == ('setup', '/a/invalid-name')
finder = SourceFinder(FakeFSCache({'/a/b/setup.py', '/a/__init__.py'}), options)
assert crawl(finder, '/a/b/setup.py') == ('a.b.setup', '/')
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py', '/a/__init__.py', '/a/b/c/__init__.py'}), options)
assert crawl(finder, '/a/b/c/setup.py') == ('a.b.c.setup', '/')
options.mypy_path = ['/a/b']
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py'}), options)
assert crawl(finder, '/a/b/c/setup.py') == ('c.setup', '/a/b')
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py', '/a/__init__.py', '/a/b/c/__init__.py'}), options)
assert crawl(finder, '/a/b/c/setup.py') == ('c.setup', '/a/b')
options.mypy_path = ['/a/b', '/a/b/c']
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py'}), options)
assert crawl(finder, '/a/b/c/setup.py') == ('setup', '/a/b/c')
```

## Next Steps


---

*Source: test_find_sources.py:130 | Complexity: Advanced | Last updated: 2026-06-02*