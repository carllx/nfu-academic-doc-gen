# How To: Upgrademapper

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, mock, workflow, integration

## Overview

Workflow: Tests updatemapper

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

### Step 1: 'Tests updatemapper'

```python
'Tests updatemapper'
```

**Verification:**
```python
assert_equal(test, date(2001, 1, 1))
```

### Step 2: Assign dateparser = _bytes_to_date

```python
dateparser = _bytes_to_date
```

**Verification:**
```python
assert_equal(test, date(2009, 1, 1))
```

### Step 3: Assign _original_mapper = value

```python
_original_mapper = StringConverter._mapper[:]
```

**Verification:**
```python
assert_equal(test, date(2000, 1, 1))
```

### Step 4: Call StringConverter.upgrade_mapper()

```python
StringConverter.upgrade_mapper(dateparser, date(2000, 1, 1))
```

### Step 5: Assign convert = StringConverter(...)

```python
convert = StringConverter(dateparser, date(2000, 1, 1))
```

### Step 6: Assign test = convert(...)

```python
test = convert('2001-01-01')
```

### Step 7: Call assert_equal()

```python
assert_equal(test, date(2001, 1, 1))
```

### Step 8: Assign test = convert(...)

```python
test = convert('2009-01-01')
```

### Step 9: Call assert_equal()

```python
assert_equal(test, date(2009, 1, 1))
```

### Step 10: Assign test = convert(...)

```python
test = convert('')
```

### Step 11: Call assert_equal()

```python
assert_equal(test, date(2000, 1, 1))
```

### Step 12: Assign StringConverter._mapper = _original_mapper

```python
StringConverter._mapper = _original_mapper
```


## Complete Example

```python
# Workflow
'Tests updatemapper'
dateparser = _bytes_to_date
_original_mapper = StringConverter._mapper[:]
try:
    StringConverter.upgrade_mapper(dateparser, date(2000, 1, 1))
    convert = StringConverter(dateparser, date(2000, 1, 1))
    test = convert('2001-01-01')
    assert_equal(test, date(2001, 1, 1))
    test = convert('2009-01-01')
    assert_equal(test, date(2009, 1, 1))
    test = convert('')
    assert_equal(test, date(2000, 1, 1))
finally:
    StringConverter._mapper = _original_mapper
```

## Next Steps


---

*Source: test__iotools.py:206 | Complexity: Advanced | Last updated: 2026-06-02*