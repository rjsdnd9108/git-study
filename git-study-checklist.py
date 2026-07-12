# main 브랜치 최초 버전 (레포장이 커밋)
# 규칙: 팀원 4명 모두 STATUS 딕셔너리의 "마지막 줄 바로 위"에
#       자기 완료 항목을 한 줄씩 추가합니다.

STATUS = { # STATUS 딕셔너리
    "레포_세팅": "완료 (장건웅)",
    # ↓↓↓ 여기 바로 아래 한 줄만 자신의 이름으로 추가하세요 ↓↓↓
}

def print_progress():
    print("=== Git 스터디 진행 체크리스트 ===")
    for task, status in STATUS.items():
        print(f"- {task}: {status}")

if __name__ == "__main__":
    print_progress()