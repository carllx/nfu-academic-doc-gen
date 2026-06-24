# How To: Check Specifier

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check specifier

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

### Step 1: Assign attrs = value

```python
attrs = {'name': 'foo', 'python_requires': '>=3.0, !=3.1'}
```

### Step 2: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

### Step 3: Call check_specifier()

```python
check_specifier(dist, attrs, attrs['python_requires'])
```

### Step 4: Assign attrs = value

```python
attrs = {'name': 'foo', 'python_requires': ['>=3.0', '!=3.1']}
```

### Step 5: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```

### Step 6: Call check_specifier()

```python
check_specifier(dist, attrs, attrs['python_requires'])
```

### Step 7: Assign attrs = value

```python
attrs = {'name': 'foo', 'python_requires': '>=invalid-version'}
```

### Step 8: Assign dist = Distribution(...)

```python
dist = Distribution(attrs)
```


## Complete Example

```python
# Workflow
attrs = {'name': 'foo', 'python_requires': '>=3.0, !=3.1'}
dist = Distribution(attrs)
check_specifier(dist, attrs, attrs['python_requires'])
attrs = {'name': 'foo', 'python_requires': ['>=3.0', '!=3.1']}
dist = Distribution(attrs)
check_specifier(dist, attrs, attrs['python_requires'])
attrs = {'name': 'foo', 'python_requires': '>=invalid-version'}
with pytest.raises(DistutilsSetupError):
    dist = Distribution(attrs)
```

## Next Steps


---

*Source: test_dist.py:143 | Complexity: Advanced | Last updated: 2026-06-02*