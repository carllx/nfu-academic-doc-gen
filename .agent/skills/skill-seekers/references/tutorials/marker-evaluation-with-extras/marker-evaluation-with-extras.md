# How To: Marker Evaluation With Extras

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Extras are also evaluated as markers at resolution time.

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

### Step 1: 'Extras are also evaluated as markers at resolution time.'

```python
'Extras are also evaluated as markers at resolution time.'
```

**Verification:**
```python
assert list(ws.resolve(parse_requirements('Foo'), ad)) == [Foo]
```

### Step 2: Assign ad = pkg_resources.Environment(...)

```python
ad = pkg_resources.Environment([])
```

**Verification:**
```python
assert res == [Foo, quux]
```

### Step 3: Assign ws = WorkingSet(...)

```python
ws = WorkingSet([])
```

### Step 4: Assign Foo = Distribution.from_filename(...)

```python
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.dist-info', metadata=Metadata(('METADATA', "Provides-Extra: baz\nRequires-Dist: quux; extra=='baz'")))
```

### Step 5: Call ad.add()

```python
ad.add(Foo)
```

**Verification:**
```python
assert list(ws.resolve(parse_requirements('Foo'), ad)) == [Foo]
```

### Step 6: Assign quux = Distribution.from_filename(...)

```python
quux = Distribution.from_filename('/foo_dir/quux-1.0.dist-info')
```

### Step 7: Call ad.add()

```python
ad.add(quux)
```

### Step 8: Assign res = list(...)

```python
res = list(ws.resolve(parse_requirements('Foo[baz]'), ad))
```

**Verification:**
```python
assert res == [Foo, quux]
```


## Complete Example

```python
# Workflow
'Extras are also evaluated as markers at resolution time.'
ad = pkg_resources.Environment([])
ws = WorkingSet([])
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.dist-info', metadata=Metadata(('METADATA', "Provides-Extra: baz\nRequires-Dist: quux; extra=='baz'")))
ad.add(Foo)
assert list(ws.resolve(parse_requirements('Foo'), ad)) == [Foo]
quux = Distribution.from_filename('/foo_dir/quux-1.0.dist-info')
ad.add(quux)
res = list(ws.resolve(parse_requirements('Foo[baz]'), ad))
assert res == [Foo, quux]
```

## Next Steps


---

*Source: test_resources.py:252 | Complexity: Advanced | Last updated: 2026-06-02*