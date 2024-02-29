# 环境安装

## 安装Anaconda

1. **下载Anaconda安装包：**
   - 访问[Anaconda官网](https://www.anaconda.com/download)下载适用于Mac的Anaconda安装器。
2. **安装Anaconda：**
   - 打开下载的安装包并遵循安装向导的指示完成安装。默认情况下，Anaconda会安装在你的用户目录下。
3. **验证安装：**
   - 打开终端（Terminal），输入`conda list`。如果Anaconda已正确安装，此命令将列出已安装的包。

## 配置VS Code以使用Anaconda

1. **安装Python扩展：**
   - 打开VS Code，转到扩展视图（点击侧边栏的方块图标或使用快捷键`Cmd+Shift+X`）。
   - 搜索“Python”，然后安装由Microsoft发布的Python扩展。
2. **配置Python解释器：**
   - 打开VS Code中的一个Python文件或创建一个新的Python文件。
   - 点击状态栏底部的Python解释器版本，或通过命令面板（`Cmd+Shift+P`，然后输入`Python: Select Interpreter`）选择解释器。

## 安装依赖

1. 打开项目代码后，在终端输入` pip install -r requirements.txt` 安装所需的依赖。



# 程序配置

打开` config.py` 文件，mnemoic = 助记词， create_amount =  需要创建的钱包数量



# 程序运行

1. 在vs code中打开`main.py` 文件，右键-> 运行Python -> 在终端中运行Python文件
2. 创建的钱包保存在 `data/output`目录下。
