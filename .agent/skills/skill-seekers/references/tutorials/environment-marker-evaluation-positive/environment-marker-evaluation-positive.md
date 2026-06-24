# How To: Environment Marker Evaluation Positive

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test environment marker evaluation positive

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
assert list(res) == [Foo]
```

### Step 2: Assign ws = WorkingSet(...)

```python
ws = WorkingSet([])
```

### Step 3: Assign Foo = Distribution.from_filename(...)

```python
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.dist-info')
```

### Step 4: Call ad.add()

```python
ad.add(Foo)
```

### Step 5: Assign res = ws.resolve(...)

```python
res = ws.resolve(parse_requirements("Foo;python_version>='2'"), ad)
```

**Verification:**
```python
assert list(res) == [Foo]
```


## Complete Example

```python
# Workflow
ad = pkg_resources.Environment([])
ws = WorkingSet([])
Foo = Distribution.from_filename('/foo_dir/Foo-1.2.dist-info')
ad.add(Foo)
res = ws.resolve(parse_requirements("Foo;python_version>='2'"), ad)
assert list(res) == [Foo]
```

## Next Steps


---

*Source: test_resources.py:229 | Complexity: Intermediate | Last updated: 2026-06-02*