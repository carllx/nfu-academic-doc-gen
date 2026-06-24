# How To: Scientific No Exponent

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test scientific no exponent

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers_all_precisions
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame.from_dict(...)

```python
df = DataFrame.from_dict({'w': ['2e'], 'x': ['3E'], 'y': ['42e'], 'z': ['632E']})
```

### Step 2: Assign data = df.to_csv(...)

```python
data = df.to_csv(index=False)
```

### Step 3: Assign unknown = all_parsers_all_precisions

```python
parser, precision = all_parsers_all_precisions
```

### Step 4: Assign df_roundtrip = parser.read_csv(...)

```python
df_roundtrip = parser.read_csv(StringIO(data), float_precision=precision)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_roundtrip, df)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers_all_precisions

# Workflow
df = DataFrame.from_dict({'w': ['2e'], 'x': ['3E'], 'y': ['42e'], 'z': ['632E']})
data = df.to_csv(index=False)
parser, precision = all_parsers_all_precisions
df_roundtrip = parser.read_csv(StringIO(data), float_precision=precision)
tm.assert_frame_equal(df_roundtrip, df)
```

## Next Steps


---

*Source: test_float.py:33 | Complexity: Intermediate | Last updated: 2026-06-02*