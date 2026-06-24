# How To: All Adaptors Produce Non Empty Package

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test all adaptors produce non empty package

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `tempfile`
- `time`
- `unittest`
- `pathlib`
- `pytest`
- `skill_seekers.cli.adaptors`
- `skill_seekers.cli.adaptors.base`

**Setup Required:**
```python
self.temp_dir = tempfile.TemporaryDirectory()
self.output_dir = Path(self.temp_dir.name) / 'output'
self.output_dir.mkdir()
skill_dir = Path(self.temp_dir.name) / 'bench-skill'
skill_dir.mkdir()
(skill_dir / 'SKILL.md').write_text('# Test Skill\n\n' + 'Content. ' * 200)
(skill_dir / 'references').mkdir()
for i in range(5):
    (skill_dir / 'references' / f'ref_{i}.md').write_text(f'# Ref {i}\n\nContent. ' * 300)
self.skill_dir = skill_dir
```

## Step-by-Step Guide

### Step 1: Assign metadata = SkillMetadata(...)

```python
metadata = SkillMetadata(name='test-bench', description='Benchmark test')
```

### Step 2: Assign platforms = value

```python
platforms = ['claude', 'gemini', 'openai', 'markdown', 'langchain', 'llama-index', 'opencode', 'minimax', 'deepseek', 'kimi', 'qwen', 'openrouter', 'together', 'fireworks', 'ibm-bob']
```

### Step 3: Assign adaptor = get_adaptor(...)

```python
adaptor = get_adaptor(platform)
```

### Step 4: Call adaptor.format_skill_md()

```python
adaptor.format_skill_md(self.skill_dir, metadata)
```

### Step 5: Assign pkg = adaptor.package(...)

```python
pkg = adaptor.package(self.skill_dir, self.output_dir)
```

### Step 6: Call self.assertTrue()

```python
self.assertTrue(pkg.exists(), f'{platform} package not created')
```

### Step 7: Call self.assertGreater()

```python
self.assertGreater(pkg.stat().st_size, 0, f'{platform} package is empty')
```


## Complete Example

```python
# Setup
self.temp_dir = tempfile.TemporaryDirectory()
self.output_dir = Path(self.temp_dir.name) / 'output'
self.output_dir.mkdir()
skill_dir = Path(self.temp_dir.name) / 'bench-skill'
skill_dir.mkdir()
(skill_dir / 'SKILL.md').write_text('# Test Skill\n\n' + 'Content. ' * 200)
(skill_dir / 'references').mkdir()
for i in range(5):
    (skill_dir / 'references' / f'ref_{i}.md').write_text(f'# Ref {i}\n\nContent. ' * 300)
self.skill_dir = skill_dir

# Workflow
metadata = SkillMetadata(name='test-bench', description='Benchmark test')
platforms = ['claude', 'gemini', 'openai', 'markdown', 'langchain', 'llama-index', 'opencode', 'minimax', 'deepseek', 'kimi', 'qwen', 'openrouter', 'together', 'fireworks', 'ibm-bob']
for platform in platforms:
    adaptor = get_adaptor(platform)
    adaptor.format_skill_md(self.skill_dir, metadata)
    pkg = adaptor.package(self.skill_dir, self.output_dir)
    self.assertTrue(pkg.exists(), f'{platform} package not created')
    self.assertGreater(pkg.stat().st_size, 0, f'{platform} package is empty')
```

## Next Steps


---

*Source: test_adaptor_benchmarks.py:404 | Complexity: Intermediate | Last updated: 2026-06-02*