# How To: Asfreq Near Zero Weekly

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq near zero weekly

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign per1 = value

```python
per1 = Period('0001-01-01', 'D') + 6
```

**Verification:**
```python
assert week1 != week2
```

### Step 2: Assign per2 = value

```python
per2 = Period('0001-01-01', 'D') - 6
```

**Verification:**
```python
assert week1.asfreq('D', 'E') >= per1
```

### Step 3: Assign week1 = per1.asfreq(...)

```python
week1 = per1.asfreq('W')
```

**Verification:**
```python
assert week2.asfreq('D', 'S') <= per2
```

### Step 4: Assign week2 = per2.asfreq(...)

```python
week2 = per2.asfreq('W')
```

**Verification:**
```python
assert week1 != week2
```


## Complete Example

```python
# Workflow
per1 = Period('0001-01-01', 'D') + 6
per2 = Period('0001-01-01', 'D') - 6
week1 = per1.asfreq('W')
week2 = per2.asfreq('W')
assert week1 != week2
assert week1.asfreq('D', 'E') >= per1
assert week2.asfreq('D', 'S') <= per2
```

## Next Steps


---

*Source: test_asfreq.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*