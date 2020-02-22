from werkzeug import generate_password_hash,check_password_hash
class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password_hash=self.save_password(password)
    def check_email(self,email):
        return self.email==email
    def save_password(self,password):
        return generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
def main():
    userlist=[]
    print('hello')
    while 1 :
        choose=int(input('''
        请选择：
        1、注册
        2、登录
        3、退出
        ：
'''))
        if choose==1:
            name=input('请出入名字：')
            email=input('请输入邮箱：')
            password=input('请输入密码：')
            newuser=User(name,email,password)
            userlist.append(newuser)
        if choose==2:
            email=input('请输入邮箱：')
            password=input('请输入密码：')
            inlist=False
            for user in userlist:
                if user.check_email(email):
                    inlist=True
                    if user.check_password(password):
                        print('登录成功')
                    else:
                        print('用户名错误')
                break
            if inlist==False:
                print('请输入正确email:')
        if choose==3:
            break
if __name__=='__main__':
    main()
