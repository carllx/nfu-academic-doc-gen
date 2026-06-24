# How To: Round Subsecond

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round subsecond

## Prerequisites

**Required Modules:**
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.period`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = Timestamp.round(...)

```python
result = Timestamp('2016-10-17 12:00:00.0015').round('ms')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = Timestamp(...)

```python
expected = Timestamp('2016-10-17 12:00:00.002000')
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = Timestamp.round(...)

```python
result = Timestamp('2016-10-17 12:00:00.00149').round('ms')
```

**Verification:**
```python
assert ts == ts.round(freq)
```

### Step 4: Assign expected = Timestamp(...)

```python
expected = Timestamp('2016-10-17 12:00:00.001000')
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign ts = Timestamp(...)

```python
ts = Timestamp('2016-10-17 12:00:00.0015')
```

### Step 6: Assign result = Timestamp.round(...)

```python
result = Timestamp('2016-10-17 12:00:00.001501031').round('10ns')
```

### Step 7: Assign expected = Timestamp(...)

```python
expected = Timestamp('2016-10-17 12:00:00.001501030')
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
result = Timestamp('2016-10-17 12:00:00.0015').round('ms')
expected = Timestamp('2016-10-17 12:00:00.002000')
assert result == expected
result = Timestamp('2016-10-17 12:00:00.00149').round('ms')
expected = Timestamp('2016-10-17 12:00:00.001000')
assert result == expected
ts = Timestamp('2016-10-17 12:00:00.0015')
for freq in ['us', 'ns']:
    assert ts == ts.round(freq)
result = Timestamp('2016-10-17 12:00:00.001501031').round('10ns')
expected = Timestamp('2016-10-17 12:00:00.001501030')
assert result == expected
```

## Next Steps


---

*Source: test_round.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*