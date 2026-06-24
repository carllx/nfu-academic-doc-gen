# How To: Provides Extras Deterministic Order

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test provides extras deterministic order

## Prerequisites

**Required Modules:**
- `os`
- `re`
- `urllib.parse`
- `urllib.request`
- `pytest`
- `setuptools`
- `setuptools.dist`
- `fixtures`
- `test_find_packages`
- `textwrap`
- `distutils.errors`


## Step-by-Step Guide

### Step 1: Assign attrs = dict(...)

```python
attrs = dict(extras_require=dict(a=['foo'], b=['bar']))
```

**Verification:**
```python
assert list(dist.metadata.provides_extras) == ['a', 'b']
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

**Verification:**
```python
assert list(dist.metadata.provides_extras) == ['b', 'a']
```

### Step 3: Assign unknown = dict(...)

```python
attrs['extras_require'] = dict(reversed(attrs['extras_require'].items()))
```

### Step 4: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

**Verification:**
```python
assert list(dist.metadata.provides_extras) == ['b', 'a']
```


## Complete Example

```python
# Workflow
attrs = dict(extras_require=dict(a=['foo'], b=['bar']))
dist = Distribution(attrs)
assert list(dist.metadata.provides_extras) == ['a', 'b']
attrs['extras_require'] = dict(reversed(attrs['extras_require'].items()))
dist = Distribution(attrs)
assert list(dist.metadata.provides_extras) == ['b', 'a']
```

## Next Steps


---

*Source: test_dist.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*