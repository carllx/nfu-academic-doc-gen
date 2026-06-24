# How To: Array Output

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array output

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `pytest`
- `numpy`
- `numpy.f2py.tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: length
```

## Step-by-Step Guide

### Step 1: Assign fsuffix = length

```python
fsuffix = length
```

**Verification:**
```python
assert_array_equal(f(a), expected)
```

### Step 2: Assign f = getattr(...)

```python
f = getattr(self.module, self.fprefix + '_array_output_' + fsuffix)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([{'1': 'a', '3': 'abc', 'star': 'abcde' * 3}[length], {'1': 'A', '3': 'ABC', 'star': 'ABCDE' * 3}[length]], dtype='S')
```

### Step 4: Assign a = np.array(...)

```python
a = np.array([list(s) for s in expected], dtype='u1')
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(f(a), expected)
```


## Complete Example

```python
# Setup
# Fixtures: length

# Workflow
fsuffix = length
f = getattr(self.module, self.fprefix + '_array_output_' + fsuffix)
expected = np.array([{'1': 'a', '3': 'abc', 'star': 'abcde' * 3}[length], {'1': 'A', '3': 'ABC', 'star': 'ABCDE' * 3}[length]], dtype='S')
a = np.array([list(s) for s in expected], dtype='u1')
assert_array_equal(f(a), expected)
```

## Next Steps


---

*Source: test_character.py:111 | Complexity: Intermediate | Last updated: 2026-06-02*