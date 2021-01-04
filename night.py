from helium import *

start_chrome("https://ehall.jlu.edu.cn/jlu_portal")#界面可见
#start_chrome("https://ehall.jlu.edu.cn/jlu_portal", headless=True)#界面不可见
write('在此输入用户名', into='请输入邮箱')
write('在此输入密码', into='请输入密码')
click(S('#login-submit'))#根据id寻找按钮
go_to("https://ehall.jlu.edu.cn/jlu_portal/guide?id=2EFFFFFF-F8FA-4BFA-8FFD-856BF98F8FF1")
#上面需要复制自己在正常页面下登录后的网址(此处已做混淆处理)
click(Button("在线办理"))#根据名称寻找按钮
cell = S(".command_button_content")
highlight(cell)
click(cell)#以上三行根据class寻找按钮
click(Button("好"))
kill_browser()
