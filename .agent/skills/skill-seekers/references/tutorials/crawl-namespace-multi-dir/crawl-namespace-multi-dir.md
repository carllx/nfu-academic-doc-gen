# How To: Crawl Namespace Multi Dir

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test crawl namespace multi dir

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
assert crawl(finder, '/a/pkg/a.py') == ('pkg.a', '/a')
```

### Step 2: Assign options.namespace_packages = True

```python
options.namespace_packages = True
```

**Verification:**
```python
assert crawl(finder, '/b/pkg/b.py') == ('pkg.b', '/b')
```

### Step 3: Assign options.explicit_package_bases = True

```python
options.explicit_package_bases = True
```

### Step 4: Assign options.mypy_path = value

```python
options.mypy_path = ['/a', '/b']
```

### Step 5: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/pkg/a.py', '/b/pkg/b.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/pkg/a.py') == ('pkg.a', '/a')
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
options.mypy_path = ['/a', '/b']
finder = SourceFinder(FakeFSCache({'/a/pkg/a.py', '/b/pkg/b.py'}), options)
assert crawl(finder, '/a/pkg/a.py') == ('pkg.a', '/a')
assert crawl(finder, '/b/pkg/b.py') == ('pkg.b', '/b')
```

## Next Steps


---

*Source: test_find_sources.py:173 | Complexity: Intermediate | Last updated: 2026-06-02*