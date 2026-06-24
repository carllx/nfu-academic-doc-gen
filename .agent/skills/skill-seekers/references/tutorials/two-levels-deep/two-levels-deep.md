# How To: Two Levels Deep

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test nested namespace packages
Create namespace packages in the following tree :
    site-packages-1/pkg1/pkg2
    site-packages-2/pkg1/pkg2
Check both are in the _namespace_packages dict and that their __path__
is correct

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `os`
- `platform`
- `string`
- `sys`
- `pytest`
- `packaging.specifiers`
- `pkg_resources`
- `pkg_resources`
- `pkg1`
- `pkg1.pkg2`
- `nspkg`
- `nspkg.subpkg`

**Setup Required:**
```python
# Fixtures: symlinked_tmpdir
```

## Step-by-Step Guide

### Step 1: '\n        Test nested namespace packages\n        Create namespace packages in the following tree :\n            site-packages-1/pkg1/pkg2\n            site-packages-2/pkg1/pkg2\n        Check both are in the _namespace_packages dict and that their __path__\n        is correct\n        '

```python
'\n        Test nested namespace packages\n        Create namespace packages in the following tree :\n            site-packages-1/pkg1/pkg2\n            site-packages-2/pkg1/pkg2\n        Check both are in the _namespace_packages dict and that their __path__\n        is correct\n        '
```

**Verification:**
```python
assert 'pkg1' in pkg_resources._namespace_packages
```

### Step 2: Assign real_tmpdir = symlinked_tmpdir.realpath(...)

```python
real_tmpdir = symlinked_tmpdir.realpath()
```

**Verification:**
```python
assert 'pkg1.pkg2' in pkg_resources._namespace_packages
```

### Step 3: Assign tmpdir = symlinked_tmpdir

```python
tmpdir = symlinked_tmpdir
```

**Verification:**
```python
assert pkg_resources._namespace_packages['pkg1'] == ['pkg1.pkg2']
```

### Step 4: Call sys.path.append()

```python
sys.path.append(str(tmpdir / 'site-pkgs2'))
```

**Verification:**
```python
assert pkg1.pkg2.__path__ == expected
```

### Step 5: Assign site_dirs = value

```python
site_dirs = (tmpdir / 'site-pkgs', tmpdir / 'site-pkgs2')
```

**Verification:**
```python
assert 'pkg1' in pkg_resources._namespace_packages
```

### Step 6: Assign expected = value

```python
expected = [str(real_tmpdir / 'site-pkgs' / 'pkg1' / 'pkg2'), str(real_tmpdir / 'site-pkgs2' / 'pkg1' / 'pkg2')]
```

**Verification:**
```python
assert pkg1.pkg2.__path__ == expected
```

### Step 7: Assign pkg1 = value

```python
pkg1 = site / 'pkg1'
```

### Step 8: Assign pkg2 = value

```python
pkg2 = pkg1 / 'pkg2'
```

### Step 9: Call pkg2.ensure_dir()

```python
pkg2.ensure_dir()
```

### Step 10: Call unknown.write_text()

```python
(pkg1 / '__init__.py').write_text(self.ns_str, encoding='utf-8')
```

### Step 11: Call unknown.write_text()

```python
(pkg2 / '__init__.py').write_text(self.ns_str, encoding='utf-8')
```


## Complete Example

```python
# Setup
# Fixtures: symlinked_tmpdir

# Workflow
'\n        Test nested namespace packages\n        Create namespace packages in the following tree :\n            site-packages-1/pkg1/pkg2\n            site-packages-2/pkg1/pkg2\n        Check both are in the _namespace_packages dict and that their __path__\n        is correct\n        '
real_tmpdir = symlinked_tmpdir.realpath()
tmpdir = symlinked_tmpdir
sys.path.append(str(tmpdir / 'site-pkgs2'))
site_dirs = (tmpdir / 'site-pkgs', tmpdir / 'site-pkgs2')
for site in site_dirs:
    pkg1 = site / 'pkg1'
    pkg2 = pkg1 / 'pkg2'
    pkg2.ensure_dir()
    (pkg1 / '__init__.py').write_text(self.ns_str, encoding='utf-8')
    (pkg2 / '__init__.py').write_text(self.ns_str, encoding='utf-8')
with pytest.warns(DeprecationWarning, match='pkg_resources.declare_namespace'):
    import pkg1
assert 'pkg1' in pkg_resources._namespace_packages
with pytest.warns(DeprecationWarning, match='pkg_resources.declare_namespace'):
    import pkg1.pkg2
assert 'pkg1.pkg2' in pkg_resources._namespace_packages
assert pkg_resources._namespace_packages['pkg1'] == ['pkg1.pkg2']
expected = [str(real_tmpdir / 'site-pkgs' / 'pkg1' / 'pkg2'), str(real_tmpdir / 'site-pkgs2' / 'pkg1' / 'pkg2')]
assert pkg1.pkg2.__path__ == expected
```

## Next Steps


---

*Source: test_resources.py:800 | Complexity: Advanced | Last updated: 2026-06-02*