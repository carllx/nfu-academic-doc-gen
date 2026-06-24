# How To: Pivot With Non Observable Dropna

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot with non observable dropna

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`

**Setup Required:**
```python
# Fixtures: dropna
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Categorical([np.nan, 'low', 'high', 'low', 'high'], categories=['low', 'high'], ordered=True), 'B': [0.0, 1.0, 2.0, 3.0, 4.0]})
```

### Step 2: Assign msg = 'The default value of observed=False is deprecated'

```python
msg = 'The default value of observed=False is deprecated'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'B': values}, index=Index(Categorical.from_codes(codes, categories=['low', 'high'], ordered=dropna), name='A'))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.pivot_table(...)

```python
result = df.pivot_table(index='A', values='B', dropna=dropna)
```

### Step 6: Assign values = value

```python
values = [2.0, 3.0]
```

### Step 7: Assign codes = value

```python
codes = [0, 1]
```

### Step 8: Assign values = value

```python
values = [2.0, 3.0, 0.0]
```

### Step 9: Assign codes = value

```python
codes = [0, 1, -1]
```


## Complete Example

```python
# Setup
# Fixtures: dropna

# Workflow
df = DataFrame({'A': Categorical([np.nan, 'low', 'high', 'low', 'high'], categories=['low', 'high'], ordered=True), 'B': [0.0, 1.0, 2.0, 3.0, 4.0]})
msg = 'The default value of observed=False is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.pivot_table(index='A', values='B', dropna=dropna)
if dropna:
    values = [2.0, 3.0]
    codes = [0, 1]
else:
    values = [2.0, 3.0, 0.0]
    codes = [0, 1, -1]
expected = DataFrame({'B': values}, index=Index(Categorical.from_codes(codes, categories=['low', 'high'], ordered=dropna), name='A'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pivot.py:246 | Complexity: Advanced | Last updated: 2026-06-02*