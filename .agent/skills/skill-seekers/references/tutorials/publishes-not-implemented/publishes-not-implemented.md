# How To: Publishes Not Implemented

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test publishes not implemented

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas._config.config`
- `pandas`

**Setup Required:**
```python
# Fixtures: ip
```

## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_product(...)

```python
midx = MultiIndex.from_product([['A', 'B'], ['a', 'b', 'c']])
```

**Verification:**
```python
assert set(formatted[0].keys()) == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, len(midx))), columns=midx)
```

### Step 3: Assign opt = cf.option_context(...)

```python
opt = cf.option_context('display.html.table_schema', True)
```

### Step 4: Assign expected = value

```python
expected = {'text/plain', 'text/html'}
```

**Verification:**
```python
assert set(formatted[0].keys()) == expected
```

### Step 5: Assign formatted = ip.instance.display_formatter.format(...)

```python
formatted = ip.instance(config=ip.config).display_formatter.format(df)
```


## Complete Example

```python
# Setup
# Fixtures: ip

# Workflow
midx = MultiIndex.from_product([['A', 'B'], ['a', 'b', 'c']])
df = DataFrame(np.random.default_rng(2).standard_normal((5, len(midx))), columns=midx)
opt = cf.option_context('display.html.table_schema', True)
with opt:
    formatted = ip.instance(config=ip.config).display_formatter.format(df)
expected = {'text/plain', 'text/html'}
assert set(formatted[0].keys()) == expected
```

## Next Steps


---

*Source: test_ipython_compat.py:42 | Complexity: Intermediate | Last updated: 2026-06-02*