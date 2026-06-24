# How To: Marker Evaluation With Multiple Extras

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test marker evaluation with multiple extras

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
assert sorted(res) == [fred, quux, Foo]
```

### Step 2: Assign ws = WorkingSet(...)

```python
ws = WorkingSet([])
```

### Step 3: Assign Foo = Distribution.from_filename(...)

```python
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.dist-info', metadata=Metadata(('METADATA', "Provides-Extra: baz\nRequires-Dist: quux; extra=='baz'\nProvides-Extra: bar\nRequires-Dist: fred; extra=='bar'\n")))
```

### Step 4: Call ad.add()

```python
ad.add(Foo)
```

### Step 5: Assign quux = Distribution.from_filename(...)

```python
quux = Distribution.from_filename('/foo_dir/quux-1.0.dist-info')
```

### Step 6: Call ad.add()

```python
ad.add(quux)
```

### Step 7: Assign fred = Distribution.from_filename(...)

```python
fred = Distribution.from_filename('/foo_dir/fred-0.1.dist-info')
```

### Step 8: Call ad.add()

```python
ad.add(fred)
```

### Step 9: Assign res = list(...)

```python
res = list(ws.resolve(parse_requirements('Foo[baz,bar]'), ad))
```

**Verification:**
```python
assert sorted(res) == [fred, quux, Foo]
```


## Complete Example

```python
# Workflow
ad = pkg_resources.Environment([])
ws = WorkingSet([])
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.dist-info', metadata=Metadata(('METADATA', "Provides-Extra: baz\nRequires-Dist: quux; extra=='baz'\nProvides-Extra: bar\nRequires-Dist: fred; extra=='bar'\n")))
ad.add(Foo)
quux = Distribution.from_filename('/foo_dir/quux-1.0.dist-info')
ad.add(quux)
fred = Distribution.from_filename('/foo_dir/fred-0.1.dist-info')
ad.add(fred)
res = list(ws.resolve(parse_requirements('Foo[baz,bar]'), ad))
assert sorted(res) == [fred, quux, Foo]
```

## Next Steps


---

*Source: test_resources.py:289 | Complexity: Advanced | Last updated: 2026-06-02*