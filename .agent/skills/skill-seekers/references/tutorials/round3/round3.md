# How To: Round3

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round3

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

### Step 2: Assign index = DatetimeIndex.as_unit(...)

```python
index = DatetimeIndex(['2016-10-17 12:00:00.00149'], tz=tz).as_unit('ns')
```

### Step 3: Assign result = index.round(...)

```python
result = index.round('ms')
```

### Step 4: Assign expected = DatetimeIndex.as_unit(...)

```python
expected = DatetimeIndex(['2016-10-17 12:00:00.001000'], tz=tz).as_unit('ns')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = tz_naive_fixture
index = DatetimeIndex(['2016-10-17 12:00:00.00149'], tz=tz).as_unit('ns')
result = index.round('ms')
expected = DatetimeIndex(['2016-10-17 12:00:00.001000'], tz=tz).as_unit('ns')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_round.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*