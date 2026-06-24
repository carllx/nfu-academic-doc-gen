# How To: Info Categorical Column Smoke Test

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test info categorical column smoke test

## Prerequisites

**Required Modules:**
- `io`
- `re`
- `string`
- `sys`
- `textwrap`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign n = 2500

```python
n = 2500
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'int64': np.random.default_rng(2).integers(100, size=n, dtype=int)})
```

### Step 3: Assign unknown = Series.astype(...)

```python
df['category'] = Series(np.array(list('abcdefghij')).take(np.random.default_rng(2).integers(0, 10, size=n, dtype=int))).astype('category')
```

### Step 4: Call df.isna()

```python
df.isna()
```

### Step 5: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 6: Call df.info()

```python
df.info(buf=buf)
```

### Step 7: Assign df2 = value

```python
df2 = df[df['category'] == 'd']
```

### Step 8: Assign buf = StringIO(...)

```python
buf = StringIO()
```

### Step 9: Call df2.info()

```python
df2.info(buf=buf)
```


## Complete Example

```python
# Workflow
n = 2500
df = DataFrame({'int64': np.random.default_rng(2).integers(100, size=n, dtype=int)})
df['category'] = Series(np.array(list('abcdefghij')).take(np.random.default_rng(2).integers(0, 10, size=n, dtype=int))).astype('category')
df.isna()
buf = StringIO()
df.info(buf=buf)
df2 = df[df['category'] == 'd']
buf = StringIO()
df2.info(buf=buf)
```

## Next Steps


---

*Source: test_info.py:56 | Complexity: Advanced | Last updated: 2026-06-02*