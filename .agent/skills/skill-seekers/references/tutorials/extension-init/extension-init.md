# How To: Extension Init

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extension init

## Prerequisites

**Required Modules:**
- `os`
- `pathlib`
- `warnings`
- `distutils.extension`
- `pytest`
- `test.support.warnings_helper`


## Step-by-Step Guide

### Step 1: Assign ext = Extension(...)

```python
ext = Extension('name', [])
```

**Verification:**
```python
assert ext.name == 'name'
```

### Step 2: Assign ext = Extension(...)

```python
ext = Extension('name', ['file1', 'file2'])
```

**Verification:**
```python
assert ext.sources == ['file1', 'file2']
```

### Step 3: Assign ext = Extension(...)

```python
ext = Extension('name', [pathlib.Path('file1'), pathlib.Path('file2')])
```

**Verification:**
```python
assert ext.sources == ['file1', 'file2']
```

### Step 4: Assign ext = Extension(...)

```python
ext = Extension('name', ('file1', 'file2'))
```

**Verification:**
```python
assert ext.sources == ['file1', 'file2']
```

### Step 5: Assign ext = Extension(...)

```python
ext = Extension('name', {'file1', 'file2'})
```

**Verification:**
```python
assert sorted(ext.sources) == ['file1', 'file2']
```

### Step 6: Assign ext = Extension(...)

```python
ext = Extension('name', iter(['file1', 'file2']))
```

**Verification:**
```python
assert ext.sources == ['file1', 'file2']
```

### Step 7: Assign ext = Extension(...)

```python
ext = Extension('name', [pathlib.Path('file1'), 'file2'])
```

**Verification:**
```python
assert ext.sources == ['file1', 'file2']
```

### Step 8: Call Extension()

```python
Extension(1, [])
```

**Verification:**
```python
assert getattr(ext, attr) == []
```

### Step 9: Call Extension()

```python
Extension('name', 'file')
```

**Verification:**
```python
assert ext.language is None
```

### Step 10: Call Extension()

```python
Extension('name', ['file', 1])
```

**Verification:**
```python
assert ext.optional is None
```

### Step 11: Call warnings.simplefilter()

```python
warnings.simplefilter('always')
```

**Verification:**
```python
assert len(w.warnings) == 1
```

### Step 12: Assign ext = Extension(...)

```python
ext = Extension('name', ['file1', 'file2'], chic=True)
```

**Verification:**
```python
assert str(w.warnings[0].message) == "Unknown Extension options: 'chic'"
```


## Complete Example

```python
# Workflow
with pytest.raises(TypeError):
    Extension(1, [])
ext = Extension('name', [])
assert ext.name == 'name'
with pytest.raises(TypeError):
    Extension('name', 'file')
with pytest.raises(TypeError):
    Extension('name', ['file', 1])
ext = Extension('name', ['file1', 'file2'])
assert ext.sources == ['file1', 'file2']
ext = Extension('name', [pathlib.Path('file1'), pathlib.Path('file2')])
assert ext.sources == ['file1', 'file2']
ext = Extension('name', ('file1', 'file2'))
assert ext.sources == ['file1', 'file2']
ext = Extension('name', {'file1', 'file2'})
assert sorted(ext.sources) == ['file1', 'file2']
ext = Extension('name', iter(['file1', 'file2']))
assert ext.sources == ['file1', 'file2']
ext = Extension('name', [pathlib.Path('file1'), 'file2'])
assert ext.sources == ['file1', 'file2']
for attr in ('include_dirs', 'define_macros', 'undef_macros', 'library_dirs', 'libraries', 'runtime_library_dirs', 'extra_objects', 'extra_compile_args', 'extra_link_args', 'export_symbols', 'swig_opts', 'depends'):
    assert getattr(ext, attr) == []
assert ext.language is None
assert ext.optional is None
with check_warnings() as w:
    warnings.simplefilter('always')
    ext = Extension('name', ['file1', 'file2'], chic=True)
assert len(w.warnings) == 1
assert str(w.warnings[0].message) == "Unknown Extension options: 'chic'"
```

## Next Steps


---

*Source: test_extension.py:63 | Complexity: Advanced | Last updated: 2026-06-02*