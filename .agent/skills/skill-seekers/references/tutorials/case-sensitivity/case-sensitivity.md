# How To: Case Sensitivity

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test case sensitivity

## Prerequisites

**Required Modules:**
- `time`
- `datetime`
- `pytest`
- `numpy`
- `numpy.lib._iotools`
- `numpy.testing`
- `numpy._core.numeric`


## Step-by-Step Guide

### Step 1: 'Test case sensitivity'

```python
'Test case sensitivity'
```

**Verification:**
```python
assert_equal(test, ['A', 'a', 'b', 'c'])
```

### Step 2: Assign names = value

```python
names = ['A', 'a', 'b', 'c']
```

**Verification:**
```python
assert_equal(test, ['A', 'A_1', 'B', 'C'])
```

### Step 3: Assign test = NameValidator.validate(...)

```python
test = NameValidator().validate(names)
```

**Verification:**
```python
assert_equal(test, ['A', 'A_1', 'B', 'C'])
```

### Step 4: Call assert_equal()

```python
assert_equal(test, ['A', 'a', 'b', 'c'])
```

**Verification:**
```python
assert_equal(test, ['a', 'a_1', 'b', 'c'])
```

### Step 5: Assign test = NameValidator.validate(...)

```python
test = NameValidator(case_sensitive=False).validate(names)
```

**Verification:**
```python
assert_raises(ValueError, NameValidator, case_sensitive='foobar')
```

### Step 6: Call assert_equal()

```python
assert_equal(test, ['A', 'A_1', 'B', 'C'])
```

### Step 7: Assign test = NameValidator.validate(...)

```python
test = NameValidator(case_sensitive='upper').validate(names)
```

### Step 8: Call assert_equal()

```python
assert_equal(test, ['A', 'A_1', 'B', 'C'])
```

### Step 9: Assign test = NameValidator.validate(...)

```python
test = NameValidator(case_sensitive='lower').validate(names)
```

### Step 10: Call assert_equal()

```python
assert_equal(test, ['a', 'a_1', 'b', 'c'])
```

### Step 11: Call assert_raises()

```python
assert_raises(ValueError, NameValidator, case_sensitive='foobar')
```


## Complete Example

```python
# Workflow
'Test case sensitivity'
names = ['A', 'a', 'b', 'c']
test = NameValidator().validate(names)
assert_equal(test, ['A', 'a', 'b', 'c'])
test = NameValidator(case_sensitive=False).validate(names)
assert_equal(test, ['A', 'A_1', 'B', 'C'])
test = NameValidator(case_sensitive='upper').validate(names)
assert_equal(test, ['A', 'A_1', 'B', 'C'])
test = NameValidator(case_sensitive='lower').validate(names)
assert_equal(test, ['a', 'a_1', 'b', 'c'])
assert_raises(ValueError, NameValidator, case_sensitive='foobar')
```

## Next Steps


---

*Source: test__iotools.py:89 | Complexity: Advanced | Last updated: 2026-06-02*