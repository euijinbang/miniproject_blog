# post 모듈에 게시물 클래스 만들기 : 생성자와 메서드를 작성한다.
class Post:
    """
        게시물 클래스
        param id: 글번호
        param title: 글제목
        param content: 글내용
        param view_count: 조회수
    """
    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def add_view_count(self):
        self.view_count += 1

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title
    
    def get_content(self):
        return self.content
    
    def get_view_count(self):
        return self.view_count


if __name__ == "__main__":
    post = Post(1, "제목", "내용", 0)
    # post.set_post(1, "수정제목", "수정내용", 0)
    post.add_view_count()
    print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_id()}")