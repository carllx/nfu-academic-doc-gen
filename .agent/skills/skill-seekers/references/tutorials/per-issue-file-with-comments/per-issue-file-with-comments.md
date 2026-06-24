# How To: Per Issue File With Comments

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: Per-issue file includes comments section.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `shutil`
- `tempfile`
- `unittest`
- `datetime`
- `pathlib`
- `unittest.mock`
- `github`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`

**Setup Required:**
```python
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()
```

## Step-by-Step Guide

### Step 1: 'Per-issue file includes comments section.'

```python
'Per-issue file includes comments section.'
```

### Step 2: Assign issues = value

```python
issues = [{'number': 7, 'title': 'Question', 'state': 'open', 'labels': [], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/test/repo/issues/7', 'body': 'How do I configure X?', 'comments': [{'author': 'maintainer', 'created_at': '2023-01-03T00:00:00', 'body': 'You can configure X by editing config.yaml'}, {'author': 'user123', 'created_at': '2023-01-04T00:00:00', 'body': 'Thanks, that worked!'}]}]
```

### Step 3: Assign converter = self._setup_converter(...)

```python
converter = self._setup_converter(issues)
```

### Step 4: Call converter._generate_issues_reference()

```python
converter._generate_issues_reference()
```

### Step 5: Assign filepath = os.path.join(...)

```python
filepath = os.path.join(converter.skill_dir, 'references', 'issues', 'test-test-repo-7.md')
```

### Step 6: Assign content = Path.read_text(...)

```python
content = Path(filepath).read_text()
```

### Step 7: Call self.assertIn()

```python
self.assertIn('## Comments (2)', content)
```

### Step 8: Call self.assertIn()

```python
self.assertIn('### maintainer', content)
```

### Step 9: Call self.assertIn()

```python
self.assertIn('You can configure X by editing config.yaml', content)
```

### Step 10: Call self.assertIn()

```python
self.assertIn('### user123', content)
```

### Step 11: Call self.assertIn()

```python
self.assertIn('Thanks, that worked!', content)
```


## Complete Example

```python
# Setup
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()

# Workflow
'Per-issue file includes comments section.'
issues = [{'number': 7, 'title': 'Question', 'state': 'open', 'labels': [], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/test/repo/issues/7', 'body': 'How do I configure X?', 'comments': [{'author': 'maintainer', 'created_at': '2023-01-03T00:00:00', 'body': 'You can configure X by editing config.yaml'}, {'author': 'user123', 'created_at': '2023-01-04T00:00:00', 'body': 'Thanks, that worked!'}]}]
converter = self._setup_converter(issues)
converter._generate_issues_reference()
filepath = os.path.join(converter.skill_dir, 'references', 'issues', 'test-test-repo-7.md')
content = Path(filepath).read_text()
self.assertIn('## Comments (2)', content)
self.assertIn('### maintainer', content)
self.assertIn('You can configure X by editing config.yaml', content)
self.assertIn('### user123', content)
self.assertIn('Thanks, that worked!', content)
```

## Next Steps


---

*Source: test_github_scraper.py:1471 | Complexity: Advanced | Last updated: 2026-06-02*