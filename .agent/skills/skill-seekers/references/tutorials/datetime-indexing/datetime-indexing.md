# How To: Datetime Indexing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime indexing

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('1/1/2000', '1/7/2000')
```

**Verification:**
```python
assert s[stamp] == 0
```

### Step 2: Assign index = index.repeat(...)

```python
index = index.repeat(3)
```

**Verification:**
```python
assert s[stamp] == 0
```

### Step 3: Assign s = Series(...)

```python
s = Series(len(index), index=index)
```

### Step 4: Assign stamp = Timestamp(...)

```python
stamp = Timestamp('1/8/2000')
```

### Step 5: Assign unknown = 0

```python
s[stamp] = 0
```

**Verification:**
```python
assert s[stamp] == 0
```

### Step 6: Assign s = Series(...)

```python
s = Series(len(index), index=index)
```

### Step 7: Assign s = value

```python
s = s[::-1]
```

### Step 8: Assign unknown = 0

```python
s[stamp] = 0
```

**Verification:**
```python
assert s[stamp] == 0
```

### Step 9: s[stamp]

```python
s[stamp]
```

### Step 10: s[stamp]

```python
s[stamp]
```


## Complete Example

```python
# Workflow
index = date_range('1/1/2000', '1/7/2000')
index = index.repeat(3)
s = Series(len(index), index=index)
stamp = Timestamp('1/8/2000')
with pytest.raises(KeyError, match=re.escape(repr(stamp))):
    s[stamp]
s[stamp] = 0
assert s[stamp] == 0
s = Series(len(index), index=index)
s = s[::-1]
with pytest.raises(KeyError, match=re.escape(repr(stamp))):
    s[stamp]
s[stamp] = 0
assert s[stamp] == 0
```

## Next Steps


---

*Source: test_datetime.py:258 | Complexity: Advanced | Last updated: 2026-06-02*