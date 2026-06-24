# How To: Constructor Name

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor name

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign orig = RangeIndex(...)

```python
orig = RangeIndex(10)
```

**Verification:**
```python
assert orig.name == 'original'
```

### Step 2: Assign orig.name = 'original'

```python
orig.name = 'original'
```

**Verification:**
```python
assert copy.name == 'copy'
```

### Step 3: Assign copy = RangeIndex(...)

```python
copy = RangeIndex(orig)
```

**Verification:**
```python
assert new.name == 'copy'
```

### Step 4: Assign copy.name = 'copy'

```python
copy.name = 'copy'
```

**Verification:**
```python
assert orig.name == 'original'
```

### Step 5: Assign new = Index(...)

```python
new = Index(copy)
```

**Verification:**
```python
assert copy.name == 'copy'
```

### Step 6: Assign new.name = 'new'

```python
new.name = 'new'
```

**Verification:**
```python
assert new.name == 'new'
```


## Complete Example

```python
# Workflow
orig = RangeIndex(10)
orig.name = 'original'
copy = RangeIndex(orig)
copy.name = 'copy'
assert orig.name == 'original'
assert copy.name == 'copy'
new = Index(copy)
assert new.name == 'copy'
new.name = 'new'
assert orig.name == 'original'
assert copy.name == 'copy'
assert new.name == 'new'
```

## Next Steps


---

*Source: test_constructors.py:126 | Complexity: Intermediate | Last updated: 2026-06-02*