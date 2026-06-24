# How To: Excluded Subpackages

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test excluded subpackages

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `shutil`
- `stat`
- `warnings`
- `pathlib`
- `unittest.mock`
- `jaraco.path`
- `pytest`
- `setuptools`
- `setuptools.dist`
- `textwrap`

**Setup Required:**
```python
# Fixtures: tmpdir_cwd
```

## Step-by-Step Guide

### Step 1: Call jaraco.path.build()

```python
jaraco.path.build(EXAMPLE_WITH_MANIFEST)
```

**Verification:**
```python
assert (build_dir / 'mypkg/__init__.py').exists()
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution({'script_name': '%PEP 517%'})
```

**Verification:**
```python
assert (build_dir / 'mypkg/resource_file.txt').exists()
```

### Step 3: Call dist.parse_config_files()

```python
dist.parse_config_files()
```

**Verification:**
```python
assert not (build_dir / f).exists()
```

### Step 4: Assign build_py = dist.get_command_obj(...)

```python
build_py = dist.get_command_obj('build_py')
```

### Step 5: Assign msg = "Python recognizes 'mypkg\\.tests' as an importable package"

```python
msg = "Python recognizes 'mypkg\\.tests' as an importable package"
```

### Step 6: Assign build_dir = Path(...)

```python
build_dir = Path(dist.get_command_obj('build_py').build_lib)
```

**Verification:**
```python
assert (build_dir / 'mypkg/__init__.py').exists()
```

### Step 7: Call pytest.xfail()

```python
pytest.xfail('#3260')
```

### Step 8: Call build_py.finalize_options()

```python
build_py.finalize_options()
```

### Step 9: Call build_py.run()

```python
build_py.run()
```

### Step 10: Call warnings.filterwarnings()

```python
warnings.filterwarnings('ignore', "'encoding' argument not specified", module='distutils.text_file')
```

**Verification:**
```python
assert not (build_dir / f).exists()
```


## Complete Example

```python
# Setup
# Fixtures: tmpdir_cwd

# Workflow
jaraco.path.build(EXAMPLE_WITH_MANIFEST)
dist = Distribution({'script_name': '%PEP 517%'})
dist.parse_config_files()
build_py = dist.get_command_obj('build_py')
msg = "Python recognizes 'mypkg\\.tests' as an importable package"
with pytest.warns(SetuptoolsDeprecationWarning, match=msg):
    if os.getenv('SETUPTOOLS_USE_DISTUTILS') == 'stdlib':
        warnings.filterwarnings('ignore', "'encoding' argument not specified", module='distutils.text_file')
    build_py.finalize_options()
    build_py.run()
build_dir = Path(dist.get_command_obj('build_py').build_lib)
assert (build_dir / 'mypkg/__init__.py').exists()
assert (build_dir / 'mypkg/resource_file.txt').exists()
for f in ['mypkg/tests/__init__.py', 'mypkg/tests/test_mypkg.py', 'mypkg/tests/test_file.txt', 'mypkg/tests']:
    with pytest.raises(AssertionError):
        assert not (build_dir / f).exists()
pytest.xfail('#3260')
```

## Next Steps


---

*Source: test_build_py.py:160 | Complexity: Advanced | Last updated: 2026-06-02*