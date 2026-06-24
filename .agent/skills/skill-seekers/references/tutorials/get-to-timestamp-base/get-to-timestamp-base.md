# How To: Get To Timestamp Base

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get to timestamp base

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`

**Setup Required:**
```python
# Fixtures: freqstr, exp_freqstr
```

## Step-by-Step Guide

### Step 1: Assign off = to_offset(...)

```python
off = to_offset(freqstr)
```

**Verification:**
```python
assert result_code == exp_code
```

### Step 2: Assign per = Period._from_ordinal(...)

```python
per = Period._from_ordinal(1, off)
```

### Step 3: Assign exp_code = value

```python
exp_code = to_offset(exp_freqstr)._period_dtype_code
```

### Step 4: Assign result_code = per._dtype._get_to_timestamp_base(...)

```python
result_code = per._dtype._get_to_timestamp_base()
```

**Verification:**
```python
assert result_code == exp_code
```


## Complete Example

```python
# Setup
# Fixtures: freqstr, exp_freqstr

# Workflow
off = to_offset(freqstr)
per = Period._from_ordinal(1, off)
exp_code = to_offset(exp_freqstr)._period_dtype_code
result_code = per._dtype._get_to_timestamp_base()
assert result_code == exp_code
```

## Next Steps


---

*Source: test_freq_code.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*