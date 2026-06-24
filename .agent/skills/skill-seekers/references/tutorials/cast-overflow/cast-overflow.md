# How To: Cast Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cast overflow

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `warnings`
- `zoneinfo`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Call assert_raises()

```python
assert_raises(OverflowError, cast)
```

**Verification:**
```python
assert_raises(OverflowError, cast)
```

### Step 2: Call assert_raises()

```python
assert_raises(OverflowError, cast2)
```

**Verification:**
```python
assert_raises(OverflowError, cast2)
```

### Step 3: Call numpy.datetime64.astype()

```python
numpy.datetime64('1971-01-01 00:00:00.000000000000000').astype('<M8[D]')
```

### Step 4: Call numpy.datetime64.astype()

```python
numpy.datetime64('2014').astype('<M8[fs]')
```


## Complete Example

```python
# Workflow
def cast():
    numpy.datetime64('1971-01-01 00:00:00.000000000000000').astype('<M8[D]')
assert_raises(OverflowError, cast)

def cast2():
    numpy.datetime64('2014').astype('<M8[fs]')
assert_raises(OverflowError, cast2)
```

## Next Steps


---

*Source: test_datetime.py:950 | Complexity: Intermediate | Last updated: 2026-06-02*