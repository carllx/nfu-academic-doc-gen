# How To: Str Cat Align Mixed Inputs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test str cat align mixed inputs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`

**Setup Required:**
```python
# Fixtures: join
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a', 'b', 'c', 'd'])
```

### Step 2: Assign t = Series(...)

```python
t = Series(['d', 'a', 'e', 'b'], index=[3, 0, 4, 1])
```

### Step 3: Assign d = concat(...)

```python
d = concat([t, t], axis=1)
```

### Step 4: Assign expected_outer = Series(...)

```python
expected_outer = Series(['aaa', 'bbb', 'c--', 'ddd', '-ee'])
```

### Step 5: Assign expected = value

```python
expected = expected_outer.loc[s.index.join(t.index, how=join)]
```

### Step 6: Assign result = s.str.cat(...)

```python
result = s.str.cat([t, t], join=join, na_rep='-')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = s.str.cat(...)

```python
result = s.str.cat(d, join=join, na_rep='-')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign u = np.array(...)

```python
u = np.array(['A', 'B', 'C', 'D'])
```

### Step 11: Assign expected_outer = Series(...)

```python
expected_outer = Series(['aaA', 'bbB', 'c-C', 'ddD', '-e-'])
```

### Step 12: Assign rhs_idx = value

```python
rhs_idx = t.index.intersection(s.index) if join == 'inner' else t.index.union(s.index) if join == 'outer' else t.index.append(s.index.difference(t.index))
```

### Step 13: Assign expected = value

```python
expected = expected_outer.loc[s.index.join(rhs_idx, how=join)]
```

### Step 14: Assign result = s.str.cat(...)

```python
result = s.str.cat([t, u], join=join, na_rep='-')
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 16: Assign rgx = 'If `others` contains arrays or lists \\(or other list-likes.*'

```python
rgx = 'If `others` contains arrays or lists \\(or other list-likes.*'
```

### Step 17: Assign z = value

```python
z = Series(['1', '2', '3']).values
```

### Step 18: Call s.str.cat()

```python
s.str.cat([t, list(u)], join=join)
```

### Step 19: Call s.str.cat()

```python
s.str.cat(z, join=join)
```

### Step 20: Call s.str.cat()

```python
s.str.cat([t, z], join=join)
```


## Complete Example

```python
# Setup
# Fixtures: join

# Workflow
s = Series(['a', 'b', 'c', 'd'])
t = Series(['d', 'a', 'e', 'b'], index=[3, 0, 4, 1])
d = concat([t, t], axis=1)
expected_outer = Series(['aaa', 'bbb', 'c--', 'ddd', '-ee'])
expected = expected_outer.loc[s.index.join(t.index, how=join)]
result = s.str.cat([t, t], join=join, na_rep='-')
tm.assert_series_equal(result, expected)
result = s.str.cat(d, join=join, na_rep='-')
tm.assert_series_equal(result, expected)
u = np.array(['A', 'B', 'C', 'D'])
expected_outer = Series(['aaA', 'bbB', 'c-C', 'ddD', '-e-'])
rhs_idx = t.index.intersection(s.index) if join == 'inner' else t.index.union(s.index) if join == 'outer' else t.index.append(s.index.difference(t.index))
expected = expected_outer.loc[s.index.join(rhs_idx, how=join)]
result = s.str.cat([t, u], join=join, na_rep='-')
tm.assert_series_equal(result, expected)
with pytest.raises(TypeError, match='others must be Series,.*'):
    s.str.cat([t, list(u)], join=join)
rgx = 'If `others` contains arrays or lists \\(or other list-likes.*'
z = Series(['1', '2', '3']).values
with pytest.raises(ValueError, match=rgx):
    s.str.cat(z, join=join)
with pytest.raises(ValueError, match=rgx):
    s.str.cat([t, z], join=join)
```

## Next Steps


---

*Source: test_cat.py:294 | Complexity: Advanced | Last updated: 2026-06-02*