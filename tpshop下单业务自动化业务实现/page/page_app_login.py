import page

from base.base import Base

'''
    将操作步骤进行封装+业务组合方法
'''


class PageAppLogin(Base):
    # 1、点击 我的
    def page_app_click_me(self):
        self.base_click(page.app_login_me)

    # 2、点击 登录头像
    def page_app_click_head(self):
        self.base_click(page.app_login_link)

    # 3、输入用户名
    def page_app_input_username(self, username):
        self.base_input(page.app_username, username)

    # 4、输入密码
    def page_app_input_pwd(self, pwd):
        self.base_input(page.app_pwd, pwd)

    # 5、点击勾选协议
    def page_app_click_pro(self):
        self.base_click(page.app_pro)

    # 6、点击登录按钮
    def page_app_click_login(self):
        self.base_click(page.app_login_btn)

    # 7、获取登录昵称
    def page_app_get_nickname(self):
        return self.base_get_text(page.app_nickname)

    # 8、组合业务方法
    def page_app_login(self, username='1223313', pwd='333333', ):
        self.page_app_click_me()
        self.page_app_click_head()
        self.page_app_input_username(username)
        self.page_app_input_pwd(pwd)
        self.page_app_click_pro()
        self.page_app_click_login()
