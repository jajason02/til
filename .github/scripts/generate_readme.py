"""
TIL README 자동 생성 스크립트
til/ 하위 폴더를 스캔해서 README.md 목록을 자동으로 업데이트합니다.
"""

import os
from pathlib import Path
from datetime import datetime

# 무시할 폴더/파일
IGNORE = {'.github', 'README.md', '.git'}

# 카테고리 표시 이름
CATEGORY_NAMES = {
    'python':    'Python',
    'django':    'Django',
    'ai':        'AI / ML',
    'web':       'Web (HTML/CSS)',
    'algorithm': 'Algorithm',
    'etc':       'ETC',
}

ROOT = Path(__file__).parent.parent.parent  # til/ 루트


def get_title(filepath: Path) -> str:
    """마크다운 파일 첫 번째 # 제목을 읽어옵니다. 없으면 파일명 사용."""
    try:
        with open(filepath, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
    except Exception:
        pass
    return filepath.stem.replace('-', ' ').replace('_', ' ').title()


def get_date(filepath: Path) -> str:
    """마크다운 파일에서 날짜(> 2025-xx-xx 형식)를 읽어옵니다. 없으면 빈 문자열."""
    try:
        with open(filepath, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('> ') and len(line) >= 12:
                    candidate = line[2:12]
                    try:
                        datetime.strptime(candidate, '%Y-%m-%d')
                        return candidate
                    except ValueError:
                        pass
    except Exception:
        pass
    return ''


def collect() -> dict:
    """카테고리별 TIL 파일 목록을 수집합니다."""
    data = {}
    for category in sorted(ROOT.iterdir()):
        if category.name in IGNORE or not category.is_dir():
            continue
        files = sorted(category.glob('*.md'), reverse=True)
        if not files:
            continue
        data[category.name] = [
            {
                'title': get_title(f),
                'date':  get_date(f),
                'path':  f.relative_to(ROOT),
            }
            for f in files
        ]
    return data


def render(data: dict) -> str:
    total = sum(len(v) for v in data.values())

    lines = [
        '# TIL — Today I Learned\n',
        '공부하면서 배운 것들을 간단히 기록합니다.  ',
        '코드 스니펫, 개념 정리, 막혔던 것과 해결 방법 위주로 남깁니다.\n',
        f'> 총 **{total}개** 기록\n',
        '---\n',
        '## 목차\n',
    ]

    # 목차
    for cat, entries in data.items():
        display = CATEGORY_NAMES.get(cat, cat.title())
        anchor = display.lower().replace(' ', '-').replace('/', '').replace('(', '').replace(')', '')
        lines.append(f'- [{display} ({len(entries)})](#{anchor})')

    lines.append('')

    # 본문
    for cat, entries in data.items():
        display = CATEGORY_NAMES.get(cat, cat.title())
        lines.append(f'---\n\n## {display}\n')
        lines.append('| 제목 | 날짜 |')
        lines.append('|:---|:---|')
        for e in entries:
            date_str = e['date'] if e['date'] else '-'
            lines.append(f"| [{e['title']}]({e['path']}) | {date_str} |")
        lines.append('')

    lines.append('---\n')
    lines.append('<p align="right"><em>"가독성 우선, 효율성 체크, 기록의 힘"</em></p>')

    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    data = collect()
    readme = render(data)
    output_path = ROOT / 'README.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(readme)
    print(f"README.md 업데이트 완료 — 총 {sum(len(v) for v in data.values())}개")
