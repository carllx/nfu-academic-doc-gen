# How To: Append

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign result = unknown.append(...)

```python
result = idx[:3].append(idx[3:])
```

**Verification:**
```python
assert result.equals(idx)
```

### Step 2: Assign foos = value

```python
foos = [idx[:1], idx[1:3], idx[3:]]
```

**Verification:**
```python
assert result.equals(idx)
```

### Step 3: Assign result = unknown.append(...)

```python
result = foos[0].append(foos[1:])
```

**Verification:**
```python
assert result.equals(idx)
```

### Step 4: Assign result = idx.append(...)

```python
result = idx.append([])
```

**Verification:**
```python
assert result.equals(idx)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
result = idx[:3].append(idx[3:])
assert result.equals(idx)
foos = [idx[:1], idx[1:3], idx[3:]]
result = foos[0].append(foos[1:])
assert result.equals(idx)
result = idx.append([])
assert result.equals(idx)
```

## Next Steps


---

*Source: test_reshape.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*