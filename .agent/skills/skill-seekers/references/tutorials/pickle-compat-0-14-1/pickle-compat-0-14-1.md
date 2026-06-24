# How To: Pickle Compat 0 14 1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pickle compat 0 14 1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries.holiday`

**Setup Required:**
```python
# Fixtures: datapath
```

## Step-by-Step Guide

### Step 1: Assign hdays = value

```python
hdays = [datetime(2013, 1, 1) for ele in range(4)]
```

**Verification:**
```python
assert cday == cday0_14_1
```

### Step 2: Assign pth = datapath(...)

```python
pth = datapath('tseries', 'offsets', 'data', 'cday-0.14.1.pickle')
```

### Step 3: Assign cday0_14_1 = read_pickle(...)

```python
cday0_14_1 = read_pickle(pth)
```

### Step 4: Assign cday = CDay(...)

```python
cday = CDay(holidays=hdays)
```

**Verification:**
```python
assert cday == cday0_14_1
```


## Complete Example

```python
# Setup
# Fixtures: datapath

# Workflow
hdays = [datetime(2013, 1, 1) for ele in range(4)]
pth = datapath('tseries', 'offsets', 'data', 'cday-0.14.1.pickle')
cday0_14_1 = read_pickle(pth)
cday = CDay(holidays=hdays)
assert cday == cday0_14_1
```

## Next Steps


---

*Source: test_custom_business_day.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*