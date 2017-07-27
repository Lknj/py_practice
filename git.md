##
先在页面创建一个库
## 安装git客户端
下载安装完成后，在任何文件夹下，点鼠标右键会多出一些菜单，如**Git Bash Here**，**Git GUI Here**等，说明安装成功
## 配置Git
比如我们把本地仓库建立在D:\workpace\play文件夹下，进入play文件夹，鼠标右键操作如下步骤：
>* 在本地仓库右键选择Git Bash，输入git init命令，会多出一个.git文件，表示本地git创建成功
>* 在本地创建ssh key，输入ssh-keygen -t rsa -C "your_email@youremail.com",（""里是你的邮箱），回车，会在文人文件id_rsa上生成ssh key。
>* 然后系统会要求输入密码，直接回车跳过，表示不设密码，重复密码同上，之后提示你ssh key生成成功。
>* 进入提示的地址查看ssh key文件，复制id_rsa.pub文件里的全部内容，回到github网站，进入Account Settings，选择SSH Keys，Add SSH Key，粘贴key。
>* 测试是否key配置成功，git bash下输入ssh -T git@github.com,回车会看到you've successful......表明已经成功。
>* 接下来就是把本地仓库传到github上去，再次之前要设置username和email，因为github每次都会记录他们，输入git config --global user.name "your name",回车，git config --global user.email "your_email@youremail.com"，回车
>* 添加远程地址，输入 git remote add origin git@github.com:yourName/yourRepo.git，，，后面的yourName和yourRepo表示你在github的用户名和刚才新建的仓库，加完之后进入.git，打开config，这里会多出一个remote “origin”内容，这就是刚才添加的远程地址，也可以直接修改config来配置远程地址。
>* 提交上传
>* 在本地仓库添加一些文件，比如Happy.txt
>* 在命令行输入命令 git add Happy.txt，回车
>* git commint -m "first commit"
>* 上传到github 
>* git push origin master，git push命令会将本地仓库推送到远程服务器。。。git pull命令相反。
>* 注：首次提交，先git pull下，修改完代码后，使用git status可以查看文件的差别，使用git add 添加要commit的文件。