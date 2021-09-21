import csv, os
from post import Post

# <1> 게시글 로딩하기

file_path = "data.csv"

# post 객체를 저장할 리스트
post_list = []

# data.csv 파일이 있다면
if os.path.exists(file_path): # file 있으면 True 반환
    # 게시글 로딩
    print("게시글 로딩중...")
    # 1. data.csv 파일을 읽는다.
    f = open(file_path, "r")
    reader = csv.reader(f)
    for data in reader:
        # 2. Post 인스턴스 생성 및 저장하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    # 파일 생성하기
    f = open(file_path, "w")
    f.close()

# <3> 게시글 쓰기 함수
def write_post():
    print("\n\n - 게시글 쓰기 -")
    title = input("제목을 입력해주세요>>>")
    content = input("내용을 입력해주세요>>>")
    id = post_list[-1].get_id()+1

    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")

            
# <4> 게시글 목록 함수
def list_post():
    print("\n\n - 게시글 목록 -")
    id_list = []
    for post in post_list:
        print("번호: ", post.get_id())
        print("제목: ", post.get_title())
        print("조회수: ", post.get_view_count())
        print("")
        id_list.append(post.get_id())

    while True:
        print("글 번호를 선택해 주세요. (메뉴로 돌아가려면 -1을 입력)")
        try:
            id = int(input(">>>"))
        except ValueError:
            print("숫자를 입력해주세요")
        else:
            if id in id_list :
                post_detail(id)
                break
            elif id == -1:
                break
            else:
                print("없는 글 번호입니다.")

# <5> 게시글 상세 확인하기
def post_detail(id):
    print("\n\n - 게시글 상세 -")

    for post in post_list:
        if post.get_id() == id:
            # 조회수 1 증가
            post.add_view_count()
            print("번호: ", post.get_id())
            print("제목: ", post.get_title())
            print("본문: ", post.get_content())
            print("조회수: ", post.get_view_count())
            target_post = post

    while True:
        print("수정: 1 삭제: 2 (메뉴로 돌아가려면 -1을 입력")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                edit_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해주세요")


# <6> 게시글 수정
def edit_post(target_post):
    print("\n\n - 게시글 수정 -")
    # 새로 제목, 본문 입력
    title = input("제목을 입력해주세요>>>")
    content = input("내용을 입력해주세요>>>")
    # set_post 메서드로 Post 객체 수정
    target_post.set_post(target_post.id, title, content, target_post.view_count)
    print("# 게시글이 수정되었습니다.")


# <7> 게시글 삭제
# post_list에서 해당 Post객체 삭제
def delete_post(target_post):
    post_list.remove(target_post)
    print("# 게시글이 삭제되었습니다.")


# <8> 게시글 저장
# post_list에 저장된 내용을 data.csv파일에 저장
def save():
    f = open(file_path, "w")
    writer = csv.writer(f)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("# 저장이 완료되었습니다.")
    print("# 프로그램 종료")


# <2> 메뉴 출력하기
while True:
    print("\n\n - euijin's blog -")
    print("- 메뉴를 선택해주세요 -")
    print("1. 게시글 쓰기\n2. 게시글 목록\n3. 프로그램 종료")
    try: # 예외가 발생할 수 있는 코드
        choice = int(input(">>>"))
    except ValueError: # 예외 발생시 실행할 코드
        print("숫자를 입력해주세요")
    else: # 예외 미발생시 실행할 코드
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            # 종료 전 게시글 저장
            save()
            break