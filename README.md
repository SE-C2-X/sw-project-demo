<h1>新成员环境搭建指南</h1>
<h4>一、涉及到的软件工具</h4>
<ol>
<li>Ollama（浏览器搜索即可，一个开源大模型平台）</li>

<li>根据你自己的电脑配置，在Ollama网站里选一个大模型(左上角models)——模型具体配置要求可上网查询
<img width="337" height="250" title="ollama" src="https://github.com/user-attachments/assets/e9c81cd8-ff69-4261-8009-a940ea6fc3b6" />
<li>一个软件开发平台（IDEA、VSCode……）</li>
<li>浏览器（推荐edge和chrome）</li>
<li>python环境（版本建议3.8-3.11）</li>
</ol>
<br>
<h4>二、大模型安装步骤</h4>
<li>在官网选一个大模型（我们使用的是deepseek-r1:7b）</li>
<li>安装操作：https://apifox.com/apiskills/ollama-deploy/  看到步骤3就够</li>
<br>
<h4>三、运行项目</h4>
<li>启动大模型（cmd: ollama run +你的大模型名字）</li>
<li>开发平台中打开项目文件夹</li>
<ol>
<li>创建虚拟环境，可看这个网站https://www.runoob.com/python3/python-venv.html</li>
<li>安装依赖，如果有问题换成国内镜像网站试试</li>
<img width="522" height="181" title="项目依赖" src="https://github.com/user-attachments/assets/3f77dc23-fb1d-48d4-8512-76adb2c3068a" />
<li>终端启动虚拟环境：  .\venv\Scripts\activate</li>
<li>启动项目： python.app.py</li>
<li>浏览器（打开方式）打开前端文件index.html
</ol>



