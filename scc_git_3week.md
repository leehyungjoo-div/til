# TIL
오늘배운것 정리!

PR
🔥 작업내역을 프로젝트에 반영하는 것이 아니라 충분히 리뷰받고 최종적으로 프로젝트에 반영하는 단계입니다. 3단계 대신
사용한다고 생각하면 됩니다!
1단계. 누가 이 작업 할 것인지 정한다. - Issue
2단계. 각자 맡은 것을 작업한다. - Branch
3단계. 각자 작업을 프로젝트에 합친다. - merge
👉 (경우에 따라). 작업한 내용을 리뷰하고 최종적으로 프로젝트에 반영한다. - PR 후 merge

PR : (Pull Request, 풀리퀘스트) 는 내 작업내역을 바로 merge 하지 않고, 참여하고 있는 프로젝트에 내 작업(branch)를
merge해달라고 요청(Request) 를 먼저 보내는 것입니다.

Commit 관리하기!
amend : 작업하다가 commit 메시지에 오타가 났거나 파일을 까먹고 add(staging)하는 경우가 있겠죠?
이 때 최신의 commit을 수정하는 것을 amend(어맨드,고치기) 라고 합니다! amend 로는 가장 최신의 commit 만 고칠 수 있
다는 것을 꼭 기억하세요!

revert : 다른 사람들과 같이 협업하고 있다면 어떤 내용이 되돌려졌는지 기록으로 남기는 것도 중요합니다. 어떤 내용을 되돌렸는지 새로
운 commit을 남기는 것을 revert(리버트) 라고 합니다. 최신 commit 뿐만 아니라 이전에 했던 commit 도 revert 로 되돌릴
수 있답니다!

reset : reset (리셋)은 commit 했던 작업내역을 말 그대로 리셋시키는 것입니다.
'기억이 리셋되었다' 가 '기억이 없다'는 말인 것처럼요. 과거로 돌아가서 새로운 삶을 사는 것처럼 reset 이후에 작업내역은 없어
진 commit 기록과 관계없습니다.

stash : stash(스태시) 는 프로젝트의 변경사항을 임시적으로 보관해둘 때 사용합니다.
예를 들면, 다른 branch 로 체크아웃 하는 경우 현재 branch 의 변경사항이 사라지게 됩니다. 아직 작업 중이라서 commit 하지
않고 변경사항만 보관해두고 싶을 수 있겠죠? 이 때 commit 대신 stash 를 사용합니다.

👀 코드리뷰를 하는 이유!
코드의 품질을 높일 수 있다!
다른 사람의 눈으로 버그를 빠르게 발견할 수 있다!
서로의 지식을 나누면서, 더 나은 방법을 찾아낼 수 있습니다.
→ 내가 만든 코드가 아니라 팀의 코드의 품질을 높인다!
공유하거나 공개되면 안되는 파일들은 공개된 repo 즉, 공개 Github repo 에 올라가면 안되겠죠? Git 이 마치 이런 파일들을 없
는 것처럼 무시하게 하는 설정이 바로 .gitignore 입니다.
Github 프로젝트에서도 README.md 를 만들어 프로젝트 소개글을 적어둡니다. 프로젝트의 어마어마하게 많은 파일들을 하나하나
씩 다 읽어볼 수는 없으니 꼭 이런 소개 파일이 있는게 좋겠죠!


