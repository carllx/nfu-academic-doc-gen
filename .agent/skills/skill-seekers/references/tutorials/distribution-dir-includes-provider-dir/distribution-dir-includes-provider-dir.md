# How To: Distribution Dir Includes Provider Dir

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test distribution dir includes provider dir

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

### Step 1: Assign d = pkg_resources.Distribution(...)

```python
d = pkg_resources.Distribution()
```

**Verification:**
```python
assert 'test_attr' not in before
```

### Step 2: Assign before = d.__dir__(...)

```python
before = d.__dir__()
```

**Verification:**
```python
assert len(after) == len(before) + 1
```

### Step 3: Assign d._provider.test_attr = None

```python
d._provider.test_attr = None
```

**Verification:**
```python
assert 'test_attr' in after
```

### Step 4: Assign after = d.__dir__(...)

```python
after = d.__dir__()
```

**Verification:**
```python
assert len(after) == len(before) + 1
```


## Complete Example

```python
# Workflow
d = pkg_resources.Distribution()
before = d.__dir__()
assert 'test_attr' not in before
d._provider.test_attr = None
after = d.__dir__()
assert len(after) == len(before) + 1
assert 'test_attr' in after
```

## Next Steps


---

*Source: test_resources.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*