# Jenkins 테스트 환경과 GitLab 트리거 분리

> 2026-07-29

## 배운 것

**테스트와 이미지 빌드는 역할을 분리해야 한다.**

- Jenkins 테스트 단계에서 임시 MySQL Compose 컨테이너를 기동하고 전체 테스트를 실행했다. 테스트가 끝난 뒤 컨테이너와 볼륨을 정리하면 실행 환경을 재현 가능하게 유지할 수 있다.
- Dockerfile은 배포 이미지를 만드는 데 집중하는 편이 안전하다. 이미지 빌드 과정에서 테스트까지 중복 실행하면 테스트용 DB 컨테이너의 생명주기와 맞지 않아 연결 실패가 생길 수 있다.

**CI 트리거는 배포 단위에 맞게 제한해야 한다.**

- GitLab Build Trigger의 `Allow all branches` 설정은 다른 파트의 MR도 Jenkins Job을 실행시킬 수 있다.
- 파트별 `*/dev` 브랜치 필터와 MR 머지 이벤트를 기준으로 트리거를 구성하면 불필요한 빌드를 줄이고, 실패 원인을 해당 파트의 변경으로 좁힐 수 있다.

## 막혔던 것 / 해결

- MySQL 기반 테스트로 전환한 뒤 Dockerfile 내부 테스트가 Jenkins 테스트와 중복 실행되어 DB 연결 오류가 발생했다.
- Dockerfile의 중복 테스트를 제거하고 Jenkins에서 `MySQL 기동 → 테스트 → 정리`를 담당하도록 분리했다. 이후 테스트, 이미지 빌드, 배포, 헬스 체크가 정상 완료되는 것을 확인했다.

## 참고

- Jenkins Pipeline
- Docker Compose
- GitLab Build Trigger
