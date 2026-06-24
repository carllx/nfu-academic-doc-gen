# How To: To Records With Multindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to records with multindex

## Prerequisites

**Required Modules:**
- `collections`
- `email`
- `email.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = value

```python
index = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
```

**Verification:**
```python
assert 'bar' in r
```

### Step 2: Assign data = np.zeros(...)

```python
data = np.zeros((8, 4))
```

**Verification:**
```python
assert 'one' not in r
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(data, index=index)
```

### Step 4: Assign r = value

```python
r = df.to_records(index=True)['level_0']
```

**Verification:**
```python
assert 'bar' in r
```


## Complete Example

```python
# Workflow
index = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
data = np.zeros((8, 4))
df = DataFrame(data, index=index)
r = df.to_records(index=True)['level_0']
assert 'bar' in r
assert 'one' not in r
```

## Next Steps


---

*Source: test_to_records.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*