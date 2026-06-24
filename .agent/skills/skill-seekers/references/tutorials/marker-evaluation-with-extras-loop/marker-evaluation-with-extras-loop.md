# How To: Marker Evaluation With Extras Loop

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test marker evaluation with extras loop

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

### Step 1: Assign ad = pkg_resources.Environment(...)

```python
ad = pkg_resources.Environment([])
```

**Verification:**
```python
assert res == [a, c, b, foo]
```

### Step 2: Assign ws = WorkingSet(...)

```python
ws = WorkingSet([])
```

### Step 3: Assign a = Distribution.from_filename(...)

```python
a = Distribution.from_filename('/foo_dir/a-0.2.dist-info', metadata=Metadata(('METADATA', 'Requires-Dist: c[a]')))
```

### Step 4: Assign b = Distribution.from_filename(...)

```python
b = Distribution.from_filename('/foo_dir/b-0.3.dist-info', metadata=Metadata(('METADATA', 'Requires-Dist: c[b]')))
```

### Step 5: Assign c = Distribution.from_filename(...)

```python
c = Distribution.from_filename('/foo_dir/c-1.0.dist-info', metadata=Metadata(('METADATA', "Provides-Extra: a\nRequires-Dist: b;extra=='a'\nProvides-Extra: b\nRequires-Dist: foo;extra=='b'")))
```

### Step 6: Assign foo = Distribution.from_filename(...)

```python
foo = Distribution.from_filename('/foo_dir/foo-0.1.dist-info')
```

### Step 7: Assign res = list(...)

```python
res = list(ws.resolve(parse_requirements('a'), ad))
```

**Verification:**
```python
assert res == [a, c, b, foo]
```

### Step 8: Call ad.add()

```python
ad.add(dist)
```


## Complete Example

```python
# Workflow
ad = pkg_resources.Environment([])
ws = WorkingSet([])
a = Distribution.from_filename('/foo_dir/a-0.2.dist-info', metadata=Metadata(('METADATA', 'Requires-Dist: c[a]')))
b = Distribution.from_filename('/foo_dir/b-0.3.dist-info', metadata=Metadata(('METADATA', 'Requires-Dist: c[b]')))
c = Distribution.from_filename('/foo_dir/c-1.0.dist-info', metadata=Metadata(('METADATA', "Provides-Extra: a\nRequires-Dist: b;extra=='a'\nProvides-Extra: b\nRequires-Dist: foo;extra=='b'")))
foo = Distribution.from_filename('/foo_dir/foo-0.1.dist-info')
for dist in (a, b, c, foo):
    ad.add(dist)
res = list(ws.resolve(parse_requirements('a'), ad))
assert res == [a, c, b, foo]
```

## Next Steps


---

*Source: test_resources.py:310 | Complexity: Advanced | Last updated: 2026-06-02*