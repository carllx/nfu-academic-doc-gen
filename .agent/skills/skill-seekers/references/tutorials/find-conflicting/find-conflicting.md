# How To: Find Conflicting

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test find conflicting

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

### Step 1: Assign ws = WorkingSet(...)

```python
ws = WorkingSet([])
```

**Verification:**
```python
assert vc.value.report() == msg
```

### Step 2: Assign Foo = Distribution.from_filename(...)

```python
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.egg')
```

### Step 3: Call ws.add()

```python
ws.add(Foo)
```

### Step 4: Assign req = next(...)

```python
req = next(parse_requirements('Foo<1.2'))
```

### Step 5: Assign msg = 'Foo 1.2 is installed but Foo<1.2 is required'

```python
msg = 'Foo 1.2 is installed but Foo<1.2 is required'
```

**Verification:**
```python
assert vc.value.report() == msg
```

### Step 6: Call ws.find()

```python
ws.find(req)
```


## Complete Example

```python
# Workflow
ws = WorkingSet([])
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.egg')
ws.add(Foo)
req = next(parse_requirements('Foo<1.2'))
with pytest.raises(VersionConflict) as vc:
    ws.find(req)
msg = 'Foo 1.2 is installed but Foo<1.2 is required'
assert vc.value.report() == msg
```

## Next Steps


---

*Source: test_resources.py:371 | Complexity: Intermediate | Last updated: 2026-06-02*