# How To: Expected Promotion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test expected promotion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `hypothesis`
- `pytest`
- `hypothesis`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: expected, dtypes, optional_dtypes, data
```

## Step-by-Step Guide

### Step 1: Assign optional = data.draw(...)

```python
optional = data.draw(strategies.lists(strategies.sampled_from(dtypes + optional_dtypes)))
```

**Verification:**
```python
assert res == expected
```

### Step 2: Assign all_dtypes = value

```python
all_dtypes = dtypes + optional
```

### Step 3: Assign dtypes_sample = data.draw(...)

```python
dtypes_sample = data.draw(strategies.permutations(all_dtypes))
```

### Step 4: Assign res = np.result_type(...)

```python
res = np.result_type(*dtypes_sample)
```

**Verification:**
```python
assert res == expected
```


## Complete Example

```python
# Setup
# Fixtures: expected, dtypes, optional_dtypes, data

# Workflow
optional = data.draw(strategies.lists(strategies.sampled_from(dtypes + optional_dtypes)))
all_dtypes = dtypes + optional
dtypes_sample = data.draw(strategies.permutations(all_dtypes))
res = np.result_type(*dtypes_sample)
assert res == expected
```

## Next Steps


---

*Source: test_nep50_promotions.py:200 | Complexity: Intermediate | Last updated: 2026-06-02*