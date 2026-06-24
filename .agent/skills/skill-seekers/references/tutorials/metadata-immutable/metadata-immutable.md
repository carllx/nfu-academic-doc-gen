# How To: Metadata Immutable

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test metadata immutable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
levels, codes = (idx.levels, idx.codes)
```

### Step 2: Assign mutable_regex = re.compile(...)

```python
mutable_regex = re.compile('does not support mutable operations')
```

### Step 3: Assign names = value

```python
names = idx.names
```

### Step 4: Assign unknown = value

```python
levels[0] = levels[0]
```

### Step 5: Assign unknown = value

```python
levels[0][0] = levels[0][0]
```

### Step 6: Assign unknown = value

```python
codes[0] = codes[0]
```

### Step 7: Assign unknown = value

```python
codes[0][0] = codes[0][0]
```

### Step 8: Assign unknown = value

```python
names[0] = names[0]
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
levels, codes = (idx.levels, idx.codes)
mutable_regex = re.compile('does not support mutable operations')
with pytest.raises(TypeError, match=mutable_regex):
    levels[0] = levels[0]
with pytest.raises(TypeError, match=mutable_regex):
    levels[0][0] = levels[0][0]
with pytest.raises(TypeError, match=mutable_regex):
    codes[0] = codes[0]
with pytest.raises(ValueError, match='assignment destination is read-only'):
    codes[0][0] = codes[0][0]
names = idx.names
with pytest.raises(TypeError, match=mutable_regex):
    names[0] = names[0]
```

## Next Steps


---

*Source: test_integrity.py:216 | Complexity: Advanced | Last updated: 2026-06-02*