# How To: Info Categorical Column Just Works

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info categorical column just works

## Prerequisites

**Required Modules:**
- `io`
- `string`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign n = 2500

```python
n = 2500
```

### Step 2: Assign data = np.array.take(...)

```python
data = np.array(list('abcdefghij')).take(np.random.default_rng(2).integers(0, 10, size=n, dtype=int))
```

### Step 3: Assign s = Series.astype(...)

```python
s = Series(data).astype('category')
```

### Step 4: Call s.isna()

```python
s.isna()
```

### Step 5: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 6: Call s.info()

```python
s.info(buf=buf)
```

### Step 7: Assign s2 = value

```python
s2 = s[s == 'd']
```

### Step 8: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 9: Call s2.info()

```python
s2.info(buf=buf)
```


## Complete Example

```python
# Workflow
n = 2500
data = np.array(list('abcdefghij')).take(np.random.default_rng(2).integers(0, 10, size=n, dtype=int))
s = Series(data).astype('category')
s.isna()
buf = StringIO()
s.info(buf=buf)
s2 = s[s == 'd']
buf = StringIO()
s2.info(buf=buf)
```

## Next Steps


---

*Source: test_info.py:24 | Complexity: Advanced | Last updated: 2026-06-02*