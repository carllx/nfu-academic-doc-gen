# How To: Prob T A Given S

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test prob t a given s

## Prerequisites

**Required Modules:**
- `unittest`
- `collections`
- `nltk.translate`
- `nltk.translate.ibm_model`


## Step-by-Step Guide

### Step 1: Assign src_sentence = value

```python
src_sentence = ['ich', 'esse', 'ja', 'gern', 'räucherschinken']
```

### Step 2: Assign trg_sentence = value

```python
trg_sentence = ['i', 'love', 'to', 'eat', 'smoked', 'ham']
```

### Step 3: Assign corpus = value

```python
corpus = [AlignedSent(trg_sentence, src_sentence)]
```

### Step 4: Assign alignment_info = AlignmentInfo(...)

```python
alignment_info = AlignmentInfo((0, 1, 4, 0, 2, 5, 5), [None] + src_sentence, ['UNUSED'] + trg_sentence, None)
```

### Step 5: Assign translation_table = defaultdict(...)

```python
translation_table = defaultdict(lambda: defaultdict(float))
```

### Step 6: Assign unknown = 0.98

```python
translation_table['i']['ich'] = 0.98
```

### Step 7: Assign unknown = 0.98

```python
translation_table['love']['gern'] = 0.98
```

### Step 8: Assign unknown = 0.98

```python
translation_table['to'][None] = 0.98
```

### Step 9: Assign unknown = 0.98

```python
translation_table['eat']['esse'] = 0.98
```

### Step 10: Assign unknown = 0.98

```python
translation_table['smoked']['räucherschinken'] = 0.98
```

### Step 11: Assign unknown = 0.98

```python
translation_table['ham']['räucherschinken'] = 0.98
```

### Step 12: Assign alignment_table = defaultdict(...)

```python
alignment_table = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(float))))
```

### Step 13: Assign unknown = 0.97

```python
alignment_table[0][3][5][6] = 0.97
```

### Step 14: Assign unknown = 0.97

```python
alignment_table[1][1][5][6] = 0.97
```

### Step 15: Assign unknown = 0.97

```python
alignment_table[2][4][5][6] = 0.97
```

### Step 16: Assign unknown = 0.97

```python
alignment_table[4][2][5][6] = 0.97
```

### Step 17: Assign unknown = 0.96

```python
alignment_table[5][5][5][6] = 0.96
```

### Step 18: Assign unknown = 0.96

```python
alignment_table[5][6][5][6] = 0.96
```

### Step 19: Assign model2 = IBMModel2(...)

```python
model2 = IBMModel2(corpus, 0)
```

### Step 20: Assign model2.translation_table = translation_table

```python
model2.translation_table = translation_table
```

### Step 21: Assign model2.alignment_table = alignment_table

```python
model2.alignment_table = alignment_table
```

### Step 22: Assign probability = model2.prob_t_a_given_s(...)

```python
probability = model2.prob_t_a_given_s(alignment_info)
```

### Step 23: Assign lexical_translation = value

```python
lexical_translation = 0.98 * 0.98 * 0.98 * 0.98 * 0.98 * 0.98
```

### Step 24: Assign alignment = value

```python
alignment = 0.97 * 0.97 * 0.97 * 0.97 * 0.96 * 0.96
```

### Step 25: Assign expected_probability = value

```python
expected_probability = lexical_translation * alignment
```

### Step 26: Call self.assertEqual()

```python
self.assertEqual(round(probability, 4), round(expected_probability, 4))
```


## Complete Example

```python
# Workflow
src_sentence = ['ich', 'esse', 'ja', 'gern', 'räucherschinken']
trg_sentence = ['i', 'love', 'to', 'eat', 'smoked', 'ham']
corpus = [AlignedSent(trg_sentence, src_sentence)]
alignment_info = AlignmentInfo((0, 1, 4, 0, 2, 5, 5), [None] + src_sentence, ['UNUSED'] + trg_sentence, None)
translation_table = defaultdict(lambda: defaultdict(float))
translation_table['i']['ich'] = 0.98
translation_table['love']['gern'] = 0.98
translation_table['to'][None] = 0.98
translation_table['eat']['esse'] = 0.98
translation_table['smoked']['räucherschinken'] = 0.98
translation_table['ham']['räucherschinken'] = 0.98
alignment_table = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(float))))
alignment_table[0][3][5][6] = 0.97
alignment_table[1][1][5][6] = 0.97
alignment_table[2][4][5][6] = 0.97
alignment_table[4][2][5][6] = 0.97
alignment_table[5][5][5][6] = 0.96
alignment_table[5][6][5][6] = 0.96
model2 = IBMModel2(corpus, 0)
model2.translation_table = translation_table
model2.alignment_table = alignment_table
probability = model2.prob_t_a_given_s(alignment_info)
lexical_translation = 0.98 * 0.98 * 0.98 * 0.98 * 0.98 * 0.98
alignment = 0.97 * 0.97 * 0.97 * 0.97 * 0.96 * 0.96
expected_probability = lexical_translation * alignment
self.assertEqual(round(probability, 4), round(expected_probability, 4))
```

## Next Steps


---

*Source: test_ibm2.py:45 | Complexity: Advanced | Last updated: 2026-06-02*