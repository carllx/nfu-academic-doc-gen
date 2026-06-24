# How To: Distribution Dir Ignores Provider Dir Leading Underscore

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test distribution dir ignores provider dir leading underscore

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
assert '_test_attr' not in before
```

### Step 2: Assign before = d.__dir__(...)

```python
before = d.__dir__()
```

**Verification:**
```python
assert len(after) == len(before)
```

### Step 3: Assign d._provider._test_attr = None

```python
d._provider._test_attr = None
```

**Verification:**
```python
assert '_test_attr' not in after
```

### Step 4: Assign after = d.__dir__(...)

```python
after = d.__dir__()
```

**Verification:**
```python
assert len(after) == len(before)
```


## Complete Example

```python
# Workflow
d = pkg_resources.Distribution()
before = d.__dir__()
assert '_test_attr' not in before
d._provider._test_attr = None
after = d.__dir__()
assert len(after) == len(before)
assert '_test_attr' not in after
```

## Next Steps


---

*Source: test_resources.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*