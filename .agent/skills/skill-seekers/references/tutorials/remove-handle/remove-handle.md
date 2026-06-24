# How To: Remove Handle

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test remove_handle() from casual.py with specially crafted edge cases

## Prerequisites

**Required Modules:**
- `typing`
- `pytest`
- `nltk.tokenize`
- `nltk.tokenize.simple`
- `nltk.corpus`


## Step-by-Step Guide

### Step 1: '\n        Test remove_handle() from casual.py with specially crafted edge cases\n        '

```python
'\n        Test remove_handle() from casual.py with specially crafted edge cases\n        '
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign tokenizer = TweetTokenizer(...)

```python
tokenizer = TweetTokenizer(strip_handles=True)
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign test1 = '@twitter hello @twi_tter_. hi @12345 @123news'

```python
test1 = '@twitter hello @twi_tter_. hi @12345 @123news'
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = value

```python
expected = ['hello', '.', 'hi']
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test1)
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign test2 = '@n`@n~@n(@n)@n-@n=@n+@n\\@n|@n[@n]@n{@n}@n;@n:@n\'@n"@n/@n?@n.@n,@n<@n>@n @n\n@n ñ@n.ü@n.ç@n.'

```python
test2 = '@n`@n~@n(@n)@n-@n=@n+@n\\@n|@n[@n]@n{@n}@n;@n:@n\'@n"@n/@n?@n.@n,@n<@n>@n @n\n@n ñ@n.ü@n.ç@n.'
```

**Verification:**
```python
assert result == expected
```

### Step 7: Assign expected = value

```python
expected = ['`', '~', '(', ')', '-', '=', '+', '\\', '|', '[', ']', '{', '}', ';', ':', "'", '"', '/', '?', '.', ',', '<', '>', 'ñ', '.', 'ü', '.', 'ç', '.']
```

**Verification:**
```python
assert result == expected
```

### Step 8: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test2)
```

**Verification:**
```python
assert result == expected
```

### Step 9: Assign test3 = 'a@n j@n z@n A@n L@n Z@n 1@n 4@n 7@n 9@n 0@n _@n !@n @@n #@n $@n %@n &@n *@n'

```python
test3 = 'a@n j@n z@n A@n L@n Z@n 1@n 4@n 7@n 9@n 0@n _@n !@n @@n #@n $@n %@n &@n *@n'
```

### Step 10: Assign expected = value

```python
expected = ['a', '@n', 'j', '@n', 'z', '@n', 'A', '@n', 'L', '@n', 'Z', '@n', '1', '@n', '4', '@n', '7', '@n', '9', '@n', '0', '@n', '_', '@n', '!', '@n', '@', '@n', '#', '@n', '$', '@n', '%', '@n', '&', '@n', '*', '@n']
```

### Step 11: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test3)
```

**Verification:**
```python
assert result == expected
```

### Step 12: Assign test4 = '@n!a @n#a @n$a @n%a @n&a @n*a'

```python
test4 = '@n!a @n#a @n$a @n%a @n&a @n*a'
```

### Step 13: Assign expected = value

```python
expected = ['!', 'a', '#', 'a', '$', 'a', '%', 'a', '&', 'a', '*', 'a']
```

### Step 14: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test4)
```

**Verification:**
```python
assert result == expected
```

### Step 15: Assign test5 = '@n!@n @n#@n @n$@n @n%@n @n&@n @n*@n @n@n @@n @n@@n @n_@n @n7@n @nj@n'

```python
test5 = '@n!@n @n#@n @n$@n @n%@n @n&@n @n*@n @n@n @@n @n@@n @n_@n @n7@n @nj@n'
```

### Step 16: Assign expected = value

```python
expected = ['!', '@n', '#', '@n', '$', '@n', '%', '@n', '&', '@n', '*', '@n', '@n', '@n', '@', '@n', '@n', '@', '@n', '@n_', '@n', '@n7', '@n', '@nj', '@n']
```

### Step 17: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test5)
```

**Verification:**
```python
assert result == expected
```

### Step 18: Assign test6 = '@abcdefghijklmnopqrstuvwxyz @abcdefghijklmno1234 @abcdefghijklmno_ @abcdefghijklmnoendofhandle'

```python
test6 = '@abcdefghijklmnopqrstuvwxyz @abcdefghijklmno1234 @abcdefghijklmno_ @abcdefghijklmnoendofhandle'
```

### Step 19: Assign expected = value

```python
expected = ['pqrstuvwxyz', '1234', '_', 'endofhandle']
```

### Step 20: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test6)
```

**Verification:**
```python
assert result == expected
```

### Step 21: Assign test7 = '@abcdefghijklmnop@abcde @abcdefghijklmno@abcde @abcdefghijklmno_@abcde @abcdefghijklmno5@abcde'

```python
test7 = '@abcdefghijklmnop@abcde @abcdefghijklmno@abcde @abcdefghijklmno_@abcde @abcdefghijklmno5@abcde'
```

### Step 22: Assign expected = value

```python
expected = ['p', '@abcde', '@abcdefghijklmno', '@abcde', '_', '@abcde', '5', '@abcde']
```

### Step 23: Assign result = tokenizer.tokenize(...)

```python
result = tokenizer.tokenize(test7)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
'\n        Test remove_handle() from casual.py with specially crafted edge cases\n        '
tokenizer = TweetTokenizer(strip_handles=True)
test1 = '@twitter hello @twi_tter_. hi @12345 @123news'
expected = ['hello', '.', 'hi']
result = tokenizer.tokenize(test1)
assert result == expected
test2 = '@n`@n~@n(@n)@n-@n=@n+@n\\@n|@n[@n]@n{@n}@n;@n:@n\'@n"@n/@n?@n.@n,@n<@n>@n @n\n@n ñ@n.ü@n.ç@n.'
expected = ['`', '~', '(', ')', '-', '=', '+', '\\', '|', '[', ']', '{', '}', ';', ':', "'", '"', '/', '?', '.', ',', '<', '>', 'ñ', '.', 'ü', '.', 'ç', '.']
result = tokenizer.tokenize(test2)
assert result == expected
test3 = 'a@n j@n z@n A@n L@n Z@n 1@n 4@n 7@n 9@n 0@n _@n !@n @@n #@n $@n %@n &@n *@n'
expected = ['a', '@n', 'j', '@n', 'z', '@n', 'A', '@n', 'L', '@n', 'Z', '@n', '1', '@n', '4', '@n', '7', '@n', '9', '@n', '0', '@n', '_', '@n', '!', '@n', '@', '@n', '#', '@n', '$', '@n', '%', '@n', '&', '@n', '*', '@n']
result = tokenizer.tokenize(test3)
assert result == expected
test4 = '@n!a @n#a @n$a @n%a @n&a @n*a'
expected = ['!', 'a', '#', 'a', '$', 'a', '%', 'a', '&', 'a', '*', 'a']
result = tokenizer.tokenize(test4)
assert result == expected
test5 = '@n!@n @n#@n @n$@n @n%@n @n&@n @n*@n @n@n @@n @n@@n @n_@n @n7@n @nj@n'
expected = ['!', '@n', '#', '@n', '$', '@n', '%', '@n', '&', '@n', '*', '@n', '@n', '@n', '@', '@n', '@n', '@', '@n', '@n_', '@n', '@n7', '@n', '@nj', '@n']
result = tokenizer.tokenize(test5)
assert result == expected
test6 = '@abcdefghijklmnopqrstuvwxyz @abcdefghijklmno1234 @abcdefghijklmno_ @abcdefghijklmnoendofhandle'
expected = ['pqrstuvwxyz', '1234', '_', 'endofhandle']
result = tokenizer.tokenize(test6)
assert result == expected
test7 = '@abcdefghijklmnop@abcde @abcdefghijklmno@abcde @abcdefghijklmno_@abcde @abcdefghijklmno5@abcde'
expected = ['p', '@abcde', '@abcdefghijklmno', '@abcde', '_', '@abcde', '5', '@abcde']
result = tokenizer.tokenize(test7)
assert result == expected
```

## Next Steps


---

*Source: test_tokenize.py:468 | Complexity: Advanced | Last updated: 2026-06-02*