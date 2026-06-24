# How To: Multilevel Name Print

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multilevel name print

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: lexsorted_two_level_string_multiindex
```

## Step-by-Step Guide

### Step 1: Assign index = lexsorted_two_level_string_multiindex

```python
index = lexsorted_two_level_string_multiindex
```

**Verification:**
```python
assert repr(ser) == expected
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(len(index)), index=index, name='sth')
```

### Step 3: Assign expected = value

```python
expected = ['first  second', 'foo    one       0', '       two       1', '       three     2', 'bar    one       3', '       two       4', 'baz    two       5', '       three     6', 'qux    one       7', '       two       8', '       three     9', 'Name: sth, dtype: int64']
```

### Step 4: Assign expected = unknown.join(...)

```python
expected = '\n'.join(expected)
```

**Verification:**
```python
assert repr(ser) == expected
```


## Complete Example

```python
# Setup
# Fixtures: lexsorted_two_level_string_multiindex

# Workflow
index = lexsorted_two_level_string_multiindex
ser = Series(range(len(index)), index=index, name='sth')
expected = ['first  second', 'foo    one       0', '       two       1', '       three     2', 'bar    one       3', '       two       4', 'baz    two       5', '       three     6', 'qux    one       7', '       two       8', '       three     9', 'Name: sth, dtype: int64']
expected = '\n'.join(expected)
assert repr(ser) == expected
```

## Next Steps


---

*Source: test_formats.py:34 | Complexity: Intermediate | Last updated: 2026-06-02*