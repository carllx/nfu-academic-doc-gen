# How To: Unimplemented Dtypes Table Columns

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unimplemented dtypes table columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `io`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.io.pytables`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
```

### Step 2: Assign unknown = 'foo'

```python
df['obj1'] = 'foo'
```

### Step 3: Assign unknown = 'bar'

```python
df['obj2'] = 'bar'
```

### Step 4: Assign unknown = datetime.date(...)

```python
df['datetime1'] = datetime.date(2001, 1, 2)
```

### Step 5: Assign df = df._consolidate(...)

```python
df = df._consolidate()
```

### Step 6: Assign dtypes = value

```python
dtypes = [('date', datetime.date(2001, 1, 2))]
```

### Step 7: Assign msg = unknown.join(...)

```python
msg = '|'.join([re.escape('Cannot serialize the column [datetime1]\nbecause its data contents are not [string] but [date] object dtype'), re.escape('[date] is not implemented as a table column')])
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
```

### Step 9: Assign unknown = f

```python
df[n] = f
```

### Step 10: Assign msg = re.escape(...)

```python
msg = re.escape(f'[{n}] is not implemented as a table column')
```

### Step 11: Call store.append()

```python
store.append('df_unimplemented', df)
```

### Step 12: Call store.append()

```python
store.append(f'df1_{n}', df)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
with ensure_clean_store(setup_path) as store:
    dtypes = [('date', datetime.date(2001, 1, 2))]
    for n, f in dtypes:
        df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
        df[n] = f
        msg = re.escape(f'[{n}] is not implemented as a table column')
        with pytest.raises(TypeError, match=msg):
            store.append(f'df1_{n}', df)
df = DataFrame(1.1 * np.arange(120).reshape((30, 4)), columns=Index(list('ABCD'), dtype=object), index=Index([f'i-{i}' for i in range(30)], dtype=object))
df['obj1'] = 'foo'
df['obj2'] = 'bar'
df['datetime1'] = datetime.date(2001, 1, 2)
df = df._consolidate()
with ensure_clean_store(setup_path) as store:
    msg = '|'.join([re.escape('Cannot serialize the column [datetime1]\nbecause its data contents are not [string] but [date] object dtype'), re.escape('[date] is not implemented as a table column')])
    with pytest.raises(TypeError, match=msg):
        store.append('df_unimplemented', df)
```

## Next Steps


---

*Source: test_errors.py:62 | Complexity: Advanced | Last updated: 2026-06-02*