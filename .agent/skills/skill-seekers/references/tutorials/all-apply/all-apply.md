# How To: All Apply

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all apply

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: engine_and_raw
```

## Step-by-Step Guide

### Step 1: Assign unknown = engine_and_raw

```python
engine, raw = engine_and_raw
```

### Step 2: Assign df = value

```python
df = DataFrame({'A': date_range('20130101', periods=5, freq='s'), 'B': range(5)}).set_index('A') * 2
```

### Step 3: Assign er = df.rolling(...)

```python
er = df.rolling(window=1)
```

### Step 4: Assign r = df.rolling(...)

```python
r = df.rolling(window='1s')
```

### Step 5: Assign result = r.apply(...)

```python
result = r.apply(lambda x: 1, engine=engine, raw=raw)
```

### Step 6: Assign expected = er.apply(...)

```python
expected = er.apply(lambda x: 1, engine=engine, raw=raw)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: engine_and_raw

# Workflow
engine, raw = engine_and_raw
df = DataFrame({'A': date_range('20130101', periods=5, freq='s'), 'B': range(5)}).set_index('A') * 2
er = df.rolling(window=1)
r = df.rolling(window='1s')
result = r.apply(lambda x: 1, engine=engine, raw=raw)
expected = er.apply(lambda x: 1, engine=engine, raw=raw)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_apply.py:97 | Complexity: Intermediate | Last updated: 2026-06-02*