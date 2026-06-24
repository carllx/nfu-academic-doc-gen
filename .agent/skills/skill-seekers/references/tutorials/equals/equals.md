# How To: Equals

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`

**Setup Required:**
```python
# Fixtures: closed
```

## Step-by-Step Guide

### Step 1: Assign expected = IntervalIndex.from_breaks(...)

```python
expected = IntervalIndex.from_breaks(np.arange(5), closed=closed)
```

**Verification:**
```python
assert expected.equals(expected)
```

### Step 2: Assign expected_name1 = IntervalIndex.from_breaks(...)

```python
expected_name1 = IntervalIndex.from_breaks(np.arange(5), closed=closed, name='foo')
```

**Verification:**
```python
assert expected.equals(expected.copy())
```

### Step 3: Assign expected_name2 = IntervalIndex.from_breaks(...)

```python
expected_name2 = IntervalIndex.from_breaks(np.arange(5), closed=closed, name='bar')
```

**Verification:**
```python
assert not expected.equals(expected.astype(object))
```

### Step 4: Assign expected_other_closed = IntervalIndex.from_breaks(...)

```python
expected_other_closed = IntervalIndex.from_breaks(np.arange(5), closed=other_closed)
```

**Verification:**
```python
assert not expected.equals(np.array(expected))
```


## Complete Example

```python
# Setup
# Fixtures: closed

# Workflow
expected = IntervalIndex.from_breaks(np.arange(5), closed=closed)
assert expected.equals(expected)
assert expected.equals(expected.copy())
assert not expected.equals(expected.astype(object))
assert not expected.equals(np.array(expected))
assert not expected.equals(list(expected))
assert not expected.equals([1, 2])
assert not expected.equals(np.array([1, 2]))
assert not expected.equals(date_range('20130101', periods=2))
expected_name1 = IntervalIndex.from_breaks(np.arange(5), closed=closed, name='foo')
expected_name2 = IntervalIndex.from_breaks(np.arange(5), closed=closed, name='bar')
assert expected.equals(expected_name1)
assert expected_name1.equals(expected_name2)
for other_closed in {'left', 'right', 'both', 'neither'} - {closed}:
    expected_other_closed = IntervalIndex.from_breaks(np.arange(5), closed=other_closed)
    assert not expected.equals(expected_other_closed)
```

## Next Steps


---

*Source: test_equals.py:10 | Complexity: Intermediate | Last updated: 2026-06-02*