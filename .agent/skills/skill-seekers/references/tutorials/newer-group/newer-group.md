# How To: Newer Group

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test newer group

## Prerequisites

**Required Modules:**
- `os`
- `types`
- `distutils._modified`
- `distutils.errors`
- `distutils.tests`
- `pytest`


## Step-by-Step Guide

### Step 1: Assign tmpdir = self.mkdtemp(...)

```python
tmpdir = self.mkdtemp()
```

**Verification:**
```python
assert newer_group([one, two, three], old_file)
```

### Step 2: Assign sources = os.path.join(...)

```python
sources = os.path.join(tmpdir, 'sources')
```

**Verification:**
```python
assert not newer_group([one, two, old_file], three)
```

### Step 3: Call os.mkdir()

```python
os.mkdir(sources)
```

**Verification:**
```python
assert not newer_group([one, two, old_file], three, missing='ignore')
```

### Step 4: Assign one = os.path.join(...)

```python
one = os.path.join(sources, 'one')
```

**Verification:**
```python
assert newer_group([one, two, old_file], three, missing='newer')
```

### Step 5: Assign two = os.path.join(...)

```python
two = os.path.join(sources, 'two')
```

### Step 6: Assign three = os.path.join(...)

```python
three = os.path.join(sources, 'three')
```

### Step 7: Assign old_file = os.path.abspath(...)

```python
old_file = os.path.abspath(__file__)
```

### Step 8: Call self.write_file()

```python
self.write_file(one)
```

### Step 9: Call self.write_file()

```python
self.write_file(two)
```

### Step 10: Call self.write_file()

```python
self.write_file(three)
```

**Verification:**
```python
assert newer_group([one, two, three], old_file)
```

### Step 11: Call os.remove()

```python
os.remove(one)
```

**Verification:**
```python
assert not newer_group([one, two, old_file], three, missing='ignore')
```

### Step 12: Call newer_group()

```python
newer_group([one, two, old_file], three)
```


## Complete Example

```python
# Workflow
tmpdir = self.mkdtemp()
sources = os.path.join(tmpdir, 'sources')
os.mkdir(sources)
one = os.path.join(sources, 'one')
two = os.path.join(sources, 'two')
three = os.path.join(sources, 'three')
old_file = os.path.abspath(__file__)
self.write_file(one)
self.write_file(two)
self.write_file(three)
assert newer_group([one, two, three], old_file)
assert not newer_group([one, two, old_file], three)
os.remove(one)
with pytest.raises(OSError):
    newer_group([one, two, old_file], three)
assert not newer_group([one, two, old_file], three, missing='ignore')
assert newer_group([one, two, old_file], three, missing='newer')
```

## Next Steps


---

*Source: test_modified.py:69 | Complexity: Advanced | Last updated: 2026-06-02*