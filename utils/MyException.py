class IdException(BaseException):  # 输入学号异常
    def __init__(self, s_id):
        self.s_id = s_id

    def __str__(self):
        return f"输入学号异常--->您输入：{self.s_id}"


class NameException(BaseException):  # 姓名异常
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"姓名输入异常--->您输入：{self.name}"