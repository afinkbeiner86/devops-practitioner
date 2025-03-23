from user import User
from post import Post

app_user_one = User("qq@qq.com", "Qiu Qiu", "supersafe", "Developer")
app_user_two = User("aa@aa.com", "James Bond", "supersecret", "00 Agent")

app_user_one.change_job_title("Senior Developer")
app_user_one.get_user_info()
app_user_two.get_user_info()

app_post_1 = Post(app_user_two.name, "Again, on a secret mission today.")
app_post_1.get_post_info()