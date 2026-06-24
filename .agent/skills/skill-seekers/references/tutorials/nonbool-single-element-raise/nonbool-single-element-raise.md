# How To: Nonbool Single Element Raise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nonbool single element raise

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: data
```

## Step-by-Step Guide

### Step 1: Assign msg_warn = 'Series.bool is now deprecated and will be removed in future version of pandas'

```python
msg_warn = 'Series.bool is now deprecated and will be removed in future version of pandas'
```

### Step 2: Assign msg_err1 = 'The truth value of a Series is ambiguous'

```python
msg_err1 = 'The truth value of a Series is ambiguous'
```

### Step 3: Assign msg_err2 = 'bool cannot act on a non-boolean single element Series'

```python
msg_err2 = 'bool cannot act on a non-boolean single element Series'
```

### Step 4: Assign series = Series(...)

```python
series = Series([data])
```

### Step 5: Call bool()

```python
bool(series)
```

### Step 6: Call series.bool()

```python
series.bool()
```


## Complete Example

```python
# Setup
# Fixtures: data

# Workflow
msg_warn = 'Series.bool is now deprecated and will be removed in future version of pandas'
msg_err1 = 'The truth value of a Series is ambiguous'
msg_err2 = 'bool cannot act on a non-boolean single element Series'
series = Series([data])
with pytest.raises(ValueError, match=msg_err1):
    bool(series)
with tm.assert_produces_warning(FutureWarning, match=msg_warn):
    with pytest.raises(ValueError, match=msg_err2):
        series.bool()
```

## Next Steps


---

*Source: test_series.py:92 | Complexity: Intermediate | Last updated: 2026-06-02*