# How To: Changing Names

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test changing names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign view = idx.view(...)

```python
view = idx.view()
```

**Verification:**
```python
assert [level.name for level in idx.levels] == ['first', 'second']
```

### Step 2: Assign copy = idx.copy(...)

```python
copy = idx.copy()
```

### Step 3: Assign shallow_copy = idx._view(...)

```python
shallow_copy = idx._view()
```

### Step 4: Assign new_names = value

```python
new_names = [name + 'a' for name in idx.names]
```

### Step 5: Assign idx.names = new_names

```python
idx.names = new_names
```

### Step 6: Call check_level_names()

```python
check_level_names(idx, ['firsta', 'seconda'])
```

### Step 7: Call check_level_names()

```python
check_level_names(view, ['first', 'second'])
```

### Step 8: Call check_level_names()

```python
check_level_names(copy, ['first', 'second'])
```

### Step 9: Call check_level_names()

```python
check_level_names(shallow_copy, ['first', 'second'])
```

### Step 10: Assign shallow_copy.names = value

```python
shallow_copy.names = [name + 'c' for name in shallow_copy.names]
```

### Step 11: Call check_level_names()

```python
check_level_names(idx, ['firsta', 'seconda'])
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
assert [level.name for level in idx.levels] == ['first', 'second']
view = idx.view()
copy = idx.copy()
shallow_copy = idx._view()
new_names = [name + 'a' for name in idx.names]
idx.names = new_names
check_level_names(idx, ['firsta', 'seconda'])
check_level_names(view, ['first', 'second'])
check_level_names(copy, ['first', 'second'])
check_level_names(shallow_copy, ['first', 'second'])
shallow_copy.names = [name + 'c' for name in shallow_copy.names]
check_level_names(idx, ['firsta', 'seconda'])
```

## Next Steps


---

*Source: test_names.py:29 | Complexity: Advanced | Last updated: 2026-06-02*