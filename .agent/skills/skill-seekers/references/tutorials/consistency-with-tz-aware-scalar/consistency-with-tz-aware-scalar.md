# How To: Consistency With Tz Aware Scalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test consistency with tz aware scalar

## Prerequisites

**Required Modules:**
- `re`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = Series.to_frame(...)

```python
df = Series([Timestamp('2016-03-30 14:35:25', tz='Europe/Brussels')]).to_frame()
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df = pd.concat.reset_index(...)

```python
df = pd.concat([df, df]).reset_index(drop=True)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign expected = Timestamp(...)

```python
expected = Timestamp('2016-03-30 14:35:25+0200', tz='Europe/Brussels')
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result = value

```python
result = df[0][0]
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = value

```python
result = df.iloc[0, 0]
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign result = value

```python
result = df.loc[0, 0]
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign result = value

```python
result = df.iat[0, 0]
```

**Verification:**
```python
assert result == expected
```

### Step 8: Assign result = value

```python
result = df.at[0, 0]
```

**Verification:**
```python
assert result == expected
```

### Step 9: Assign result = value

```python
result = df[0].loc[0]
```

**Verification:**
```python
assert result == expected
```

### Step 10: Assign result = value

```python
result = df[0].at[0]
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = Series([Timestamp('2016-03-30 14:35:25', tz='Europe/Brussels')]).to_frame()
df = pd.concat([df, df]).reset_index(drop=True)
expected = Timestamp('2016-03-30 14:35:25+0200', tz='Europe/Brussels')
result = df[0][0]
assert result == expected
result = df.iloc[0, 0]
assert result == expected
result = df.loc[0, 0]
assert result == expected
result = df.iat[0, 0]
assert result == expected
result = df.at[0, 0]
assert result == expected
result = df[0].loc[0]
assert result == expected
result = df[0].at[0]
assert result == expected
```

## Next Steps


---

*Source: test_datetime.py:75 | Complexity: Advanced | Last updated: 2026-06-02*