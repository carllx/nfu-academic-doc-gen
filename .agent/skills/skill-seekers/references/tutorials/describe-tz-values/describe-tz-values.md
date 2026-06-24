# How To: Describe Tz Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe tz values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
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

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(range(5))
```

### Step 3: Assign start = Timestamp(...)

```python
start = Timestamp(2018, 1, 1)
```

### Step 4: Assign end = Timestamp(...)

```python
end = Timestamp(2018, 1, 5)
```

### Step 5: Assign s2 = Series(...)

```python
s2 = Series(date_range(start, end, tz=tz))
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'s1': s1, 's2': s2})
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'s1': [5, 2, 0, 1, 2, 3, 4, 1.581139], 's2': [5, Timestamp(2018, 1, 3).tz_localize(tz), start.tz_localize(tz), s2[1], s2[2], s2[3], end.tz_localize(tz), np.nan]}, index=['count', 'mean', 'min', '25%', '50%', '75%', 'max', 'std'])
```

### Step 8: Assign result = df.describe(...)

```python
result = df.describe(include='all')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = tz_naive_fixture
s1 = Series(range(5))
start = Timestamp(2018, 1, 1)
end = Timestamp(2018, 1, 5)
s2 = Series(date_range(start, end, tz=tz))
df = DataFrame({'s1': s1, 's2': s2})
expected = DataFrame({'s1': [5, 2, 0, 1, 2, 3, 4, 1.581139], 's2': [5, Timestamp(2018, 1, 3).tz_localize(tz), start.tz_localize(tz), s2[1], s2[2], s2[3], end.tz_localize(tz), np.nan]}, index=['count', 'mean', 'min', '25%', '50%', '75%', 'max', 'std'])
result = df.describe(include='all')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:252 | Complexity: Advanced | Last updated: 2026-06-02*