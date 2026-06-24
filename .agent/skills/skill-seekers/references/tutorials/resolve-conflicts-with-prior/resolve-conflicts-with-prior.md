# How To: Resolve Conflicts With Prior

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: A ContextualVersionConflict should be raised when a requirement
conflicts with a prior requirement for a different package.

## Prerequisites

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


## Step-by-Step Guide

### Step 1: '\n        A ContextualVersionConflict should be raised when a requirement\n        conflicts with a prior requirement for a different package.\n        '

```python
'\n        A ContextualVersionConflict should be raised when a requirement\n        conflicts with a prior requirement for a different package.\n        '
```

**Verification:**
```python
assert vc.value.report() == msg
```

### Step 2: Assign ws = WorkingSet(...)

```python
ws = WorkingSet([])
```

### Step 3: Assign md = Metadata(...)

```python
md = Metadata(('depends.txt', 'Baz==1.0'))
```

### Step 4: Assign Foo = Distribution.from_filename(...)

```python
Foo = Distribution.from_filename('/foo_dir/Foo-1.0.egg', metadata=md)
```

### Step 5: Call ws.add()

```python
ws.add(Foo)
```

### Step 6: Assign md = Metadata(...)

```python
md = Metadata(('depends.txt', 'Baz==2.0'))
```

### Step 7: Assign Bar = Distribution.from_filename(...)

```python
Bar = Distribution.from_filename('/foo_dir/Bar-1.0.egg', metadata=md)
```

### Step 8: Call ws.add()

```python
ws.add(Bar)
```

### Step 9: Assign Baz = Distribution.from_filename(...)

```python
Baz = Distribution.from_filename('/foo_dir/Baz-1.0.egg')
```

### Step 10: Call ws.add()

```python
ws.add(Baz)
```

### Step 11: Assign Baz = Distribution.from_filename(...)

```python
Baz = Distribution.from_filename('/foo_dir/Baz-2.0.egg')
```

### Step 12: Call ws.add()

```python
ws.add(Baz)
```

### Step 13: Assign msg = 'Baz 1.0 is installed but Baz==2.0 is required by '

```python
msg = 'Baz 1.0 is installed but Baz==2.0 is required by '
```

**Verification:**
```python
assert vc.value.report() == msg
```

### Step 14: Call ws.resolve()

```python
ws.resolve(parse_requirements('Foo\nBar\n'))
```


## Complete Example

```python
# Workflow
'\n        A ContextualVersionConflict should be raised when a requirement\n        conflicts with a prior requirement for a different package.\n        '
ws = WorkingSet([])
md = Metadata(('depends.txt', 'Baz==1.0'))
Foo = Distribution.from_filename('/foo_dir/Foo-1.0.egg', metadata=md)
ws.add(Foo)
md = Metadata(('depends.txt', 'Baz==2.0'))
Bar = Distribution.from_filename('/foo_dir/Bar-1.0.egg', metadata=md)
ws.add(Bar)
Baz = Distribution.from_filename('/foo_dir/Baz-1.0.egg')
ws.add(Baz)
Baz = Distribution.from_filename('/foo_dir/Baz-2.0.egg')
ws.add(Baz)
with pytest.raises(VersionConflict) as vc:
    ws.resolve(parse_requirements('Foo\nBar\n'))
msg = 'Baz 1.0 is installed but Baz==2.0 is required by '
msg += repr(set(['Bar']))
assert vc.value.report() == msg
```

## Next Steps


---

*Source: test_resources.py:385 | Complexity: Advanced | Last updated: 2026-06-02*