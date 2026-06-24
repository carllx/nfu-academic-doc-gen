# How To: Char

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test char

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`


## Step-by-Step Guide

### Step 1: Assign strings = value

```python
strings = np.array(['ab', 'cd', 'ef'], dtype='c').T
```

**Verification:**
```python
assert inp == pytest.approx(strings)
```

### Step 2: Assign unknown = self.module.char_test.change_strings(...)

```python
inp, out = self.module.char_test.change_strings(strings, strings.shape[1])
```

**Verification:**
```python
assert out == pytest.approx(expected)
```

### Step 3: Assign expected = strings.copy(...)

```python
expected = strings.copy()
```

### Step 4: Assign unknown = 'AAA'

```python
expected[1, :] = 'AAA'
```

**Verification:**
```python
assert out == pytest.approx(expected)
```


## Complete Example

```python
# Workflow
strings = np.array(['ab', 'cd', 'ef'], dtype='c').T
inp, out = self.module.char_test.change_strings(strings, strings.shape[1])
assert inp == pytest.approx(strings)
expected = strings.copy()
expected[1, :] = 'AAA'
assert out == pytest.approx(expected)
```

## Next Steps


---

*Source: test_string.py:12 | Complexity: Intermediate | Last updated: 2026-06-02*