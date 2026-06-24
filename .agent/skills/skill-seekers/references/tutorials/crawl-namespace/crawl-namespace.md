# How To: Crawl Namespace

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test crawl namespace

## Prerequisites

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

### Step 3: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/setup.py') == ('setup', '/a/b')
```

### Step 4: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/setup.py') == ('a.setup', '/')
```

### Step 5: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/setup.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/invalid-name/setup.py') == ('setup', '/a/invalid-name')
```

### Step 6: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/setup.py', '/a/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/setup.py') == ('a.b.setup', '/')
```

### Step 7: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/invalid-name/setup.py', '/a/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('a.b.c.setup', '/')
```

### Step 8: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/setup.py', '/a/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/setup.py') == ('a.b.setup', '/')
```

### Step 9: Assign finder = SourceFinder(...)

```python
finder = SourceFinder(FakeFSCache({'/a/b/c/setup.py', '/a/__init__.py', '/a/b/c/__init__.py'}), options)
```

**Verification:**
```python
assert crawl(finder, '/a/b/c/setup.py') == ('a.b.c.setup', '/')
```


## Complete Example

```python
# Workflow
options = Options()
options.namespace_packages = True
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
```

## Next Steps


---

*Source: test_find_sources.py:103 | Complexity: Advanced | Last updated: 2026-06-02*