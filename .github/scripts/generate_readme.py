"""
TIL README 자동 생성 스크립트
til/ 하위 폴더를 스캔해서 README.md 목록을 자동으로 업데이트합니다.
"""

import re
from pathlib import Path
from datetime import datetime

IGNORE = {'.github', 'README.md', 'TEMPLATE.md', '.git'}

CATEGORY_NAMES = {
    'python':    'Python',
    'django':    'Django',
    'ai':        'AI / ML',
    'web':       'Web',
    'algorithm': 'Algorithm',
    'etc':       'ETC',
}

ROOT = Path(__file__).parent.parent.parent


def to_anchor(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text


def get_title(filepath: Path) -> str:
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
                'path':  f.relative_to(ROOT).as_posix(),
            }
            for f in files
        ]
    return data


def render(data: dict) -> str:
    total = sum(len(v) for v in data.values())

    all_dates = [
        e['date']
        for entries in data.values()
        for e in entries
        if e['date']
    ]
    latest = max(all_dates) if all_dates else '-'

    # Stats 표
    lines = [
        '# TIL — Today I Learned\n',
        '공부하면서 배운 것들을 간단히 기록합니다.  ',
        '코드 스니펫, 개념 정리, 막혔던 것과 해결 방법 위주로 남깁니다.\n',
        '---\n',
        '## Stats\n',
        '| | |',
        '|:---|:---|',
        f'| Total | **{total}** |',
        f'| Categories | **{len(data)}** |',
        f'| Last updated | **{latest}** |',
        '\n---\n',
    ]

    # TOC — 한 줄로
    toc_parts = []
    for cat, entries in data.items():
        display = CATEGORY_NAMES.get(cat, cat.title())
        anchor  = to_anchor(display)
        toc_parts.append(f'[{display}](#{anchor}) &nbsp;·&nbsp; {len(entries)}')
    lines.append(' &nbsp;|&nbsp; '.join(toc_parts) + '\n')

    # 카테고리별 섹션 (링크 없는 순수 헤더)
    for cat, entries in data.items():
        display = CATEGORY_NAMES.get(cat, cat.title())

        lines.append(f'## {display} &nbsp; <sub>{len(entries)} notes</sub>\n')
        lines.append('| Title | Date |')
        lines.append('|:---|:---|')
        for e in entries:
            date_str = e['date'] if e['date'] else '-'
            lines.append(f'| [{e["title"]}]({e["path"]}) | {date_str} |')
        lines.append('')

    lines += [
        '---\n',
        '## Writing Guide\n',
        '- 파일명: `주제-요약.md` (예: `bfs-shortest-path.md`)',
        '- 날짜: 파일 상단 `> YYYY-MM-DD` 형식',
        '- 구성: **배운 것** / **막혔던 것·해결** / **참고**',
        '- 새 카테고리 폴더를 만들면 자동으로 README에 반영됨\n',
        '---\n',
        '<p align="right"><em>"가독성 우선, 효율성 체크, 기록의 힘"</em></p>\n',
    ]

    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    data   = collect()
    readme = render(data)

    with open(ROOT / 'README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    print(f'Done — {sum(len(v) for v in data.values())} notes')