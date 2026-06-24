# How To: Extractall

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extractall

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = ['dave@google.com', 'tdhock5@gmail.com', 'maudelaperriere@gmail.com', 'rob@gmail.com some text steve@gmail.com', 'a@b.com some text c@d.com and e@f.com', np.nan, '']
```

### Step 2: Assign expected_tuples = value

```python
expected_tuples = [('dave', 'google', 'com'), ('tdhock5', 'gmail', 'com'), ('maudelaperriere', 'gmail', 'com'), ('rob', 'gmail', 'com'), ('steve', 'gmail', 'com'), ('a', 'b', 'com'), ('c', 'd', 'com'), ('e', 'f', 'com')]
```

### Step 3: Assign pat = '\n    (?P<user>[a-z0-9]+)\n    @\n    (?P<domain>[a-z]+)\n    \\.\n    (?P<tld>[a-z]{2,4})\n    '

```python
pat = '\n    (?P<user>[a-z0-9]+)\n    @\n    (?P<domain>[a-z]+)\n    \\.\n    (?P<tld>[a-z]{2,4})\n    '
```

### Step 4: Assign expected_columns = value

```python
expected_columns = ['user', 'domain', 'tld']
```

### Step 5: Assign s = Series(...)

```python
s = Series(data, dtype=any_string_dtype)
```

### Step 6: Assign expected_index = MultiIndex.from_tuples(...)

```python
expected_index = MultiIndex.from_tuples([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2)], names=(None, 'match'))
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_tuples, expected_index, expected_columns, dtype=any_string_dtype)
```

### Step 8: Assign result = s.str.extractall(...)

```python
result = s.str.extractall(pat, flags=re.VERBOSE)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('single', 'Dave'), ('single', 'Toby'), ('single', 'Maude'), ('multiple', 'robAndSteve'), ('multiple', 'abcdef'), ('none', 'missing'), ('none', 'empty')])
```

### Step 11: Assign s = Series(...)

```python
s = Series(data, index=mi, dtype=any_string_dtype)
```

### Step 12: Assign expected_index = MultiIndex.from_tuples(...)

```python
expected_index = MultiIndex.from_tuples([('single', 'Dave', 0), ('single', 'Toby', 0), ('single', 'Maude', 0), ('multiple', 'robAndSteve', 0), ('multiple', 'robAndSteve', 1), ('multiple', 'abcdef', 0), ('multiple', 'abcdef', 1), ('multiple', 'abcdef', 2)], names=(None, None, 'match'))
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_tuples, expected_index, expected_columns, dtype=any_string_dtype)
```

### Step 14: Assign result = s.str.extractall(...)

```python
result = s.str.extractall(pat, flags=re.VERBOSE)
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign s = Series(...)

```python
s = Series(data, index=mi, dtype=any_string_dtype)
```

### Step 17: Assign s.index.names = value

```python
s.index.names = ('matches', 'description')
```

### Step 18: Assign expected_index.names = value

```python
expected_index.names = ('matches', 'description', 'match')
```

### Step 19: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected_tuples, expected_index, expected_columns, dtype=any_string_dtype)
```

### Step 20: Assign result = s.str.extractall(...)

```python
result = s.str.extractall(pat, flags=re.VERBOSE)
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
data = ['dave@google.com', 'tdhock5@gmail.com', 'maudelaperriere@gmail.com', 'rob@gmail.com some text steve@gmail.com', 'a@b.com some text c@d.com and e@f.com', np.nan, '']
expected_tuples = [('dave', 'google', 'com'), ('tdhock5', 'gmail', 'com'), ('maudelaperriere', 'gmail', 'com'), ('rob', 'gmail', 'com'), ('steve', 'gmail', 'com'), ('a', 'b', 'com'), ('c', 'd', 'com'), ('e', 'f', 'com')]
pat = '\n    (?P<user>[a-z0-9]+)\n    @\n    (?P<domain>[a-z]+)\n    \\.\n    (?P<tld>[a-z]{2,4})\n    '
expected_columns = ['user', 'domain', 'tld']
s = Series(data, dtype=any_string_dtype)
expected_index = MultiIndex.from_tuples([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2)], names=(None, 'match'))
expected = DataFrame(expected_tuples, expected_index, expected_columns, dtype=any_string_dtype)
result = s.str.extractall(pat, flags=re.VERBOSE)
tm.assert_frame_equal(result, expected)
mi = MultiIndex.from_tuples([('single', 'Dave'), ('single', 'Toby'), ('single', 'Maude'), ('multiple', 'robAndSteve'), ('multiple', 'abcdef'), ('none', 'missing'), ('none', 'empty')])
s = Series(data, index=mi, dtype=any_string_dtype)
expected_index = MultiIndex.from_tuples([('single', 'Dave', 0), ('single', 'Toby', 0), ('single', 'Maude', 0), ('multiple', 'robAndSteve', 0), ('multiple', 'robAndSteve', 1), ('multiple', 'abcdef', 0), ('multiple', 'abcdef', 1), ('multiple', 'abcdef', 2)], names=(None, None, 'match'))
expected = DataFrame(expected_tuples, expected_index, expected_columns, dtype=any_string_dtype)
result = s.str.extractall(pat, flags=re.VERBOSE)
tm.assert_frame_equal(result, expected)
s = Series(data, index=mi, dtype=any_string_dtype)
s.index.names = ('matches', 'description')
expected_index.names = ('matches', 'description', 'match')
expected = DataFrame(expected_tuples, expected_index, expected_columns, dtype=any_string_dtype)
result = s.str.extractall(pat, flags=re.VERBOSE)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:397 | Complexity: Advanced | Last updated: 2026-06-02*