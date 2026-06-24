# How To: Mismatched Start End Freq Raises

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mismatched start end freq raises

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign depr_msg = 'Period with BDay freq is deprecated'

```python
depr_msg = 'Period with BDay freq is deprecated'
```

### Step 2: Assign msg = "'w' is deprecated and will be removed in a future version."

```python
msg = "'w' is deprecated and will be removed in a future version."
```

### Step 3: Assign msg = 'start and end must have same freq'

```python
msg = 'start and end must have same freq'
```

### Step 4: Assign end_w = Period(...)

```python
end_w = Period('2006-12-31', '1w')
```

### Step 5: Assign start_b = Period(...)

```python
start_b = Period('02-Apr-2005', 'B')
```

### Step 6: Assign end_b = Period(...)

```python
end_b = Period('2005-05-01', 'B')
```

### Step 7: Call period_range()

```python
period_range(start=start_b, end=end_b)
```

### Step 8: Call period_range()

```python
period_range(start=start_b, end=end_w)
```


## Complete Example

```python
# Workflow
depr_msg = 'Period with BDay freq is deprecated'
msg = "'w' is deprecated and will be removed in a future version."
with tm.assert_produces_warning(FutureWarning, match=msg):
    end_w = Period('2006-12-31', '1w')
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    start_b = Period('02-Apr-2005', 'B')
    end_b = Period('2005-05-01', 'B')
msg = 'start and end must have same freq'
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(FutureWarning, match=depr_msg):
        period_range(start=start_b, end=end_w)
with tm.assert_produces_warning(FutureWarning, match=depr_msg):
    period_range(start=start_b, end=end_b)
```

## Next Steps


---

*Source: test_period_range.py:182 | Complexity: Advanced | Last updated: 2026-06-02*