# *-UTF-8-*
# @Time    : 2019/8/15 8:32
# @Author  : Zurich.Alcazar
# @Email   : 1178824808@qq.com
# @File    : bs4_learning.py
# @Software: PyCharm

from bs4 import BeautifulSoup


def init_soup():
    # python内置标准库：执行速度适中，文档容错能力强；
    soup = BeautifulSoup("<p>Hello</p>","html.parser")

    # 使用lxml 库解析，执行速度快，文档容错能力强，但是要求安装lxml扩展
    soup = BeautifulSoup("<p>Hello</p>","lxml")

    # 有最好的容错率，已浏览器的方式解析文档，生成HTML5格式的文档，但速度较慢；
    soup = BeautifulSoup("<p>Hello</p>","html5lib")

    # 支持解析xml，速度快，但是需要安装外部扩展；
    soup = BeautifulSoup("<p>Hello</p>","xml")
    print(soup.p.string)


def basic():
    html = """
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>文集精选</title>
        </head>
        <body>
            <p class="title" name="dromouse">
                <b>Zurich_Alacazar</b>
            </p>
            <p class="story">
                从前有座山，山上有座
                <a href="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565840005673&di=62c1016cfc220878086b827e609cffd9&imgtype=0&src=http%3A%2F%2Fnews.5068.com%2Fupfiles%2Fallimg%2F150131%2F8569_150131085538_1.jpg">城堡</a>，
                城堡里有个
                <a href="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565840137537&di=d101dc5429cbe5dba1dc4e4273f3ba20&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F17%2F54%2F88%2F058PICU58PICuCV_1024.jpg">国王</a>
                还有许多
                <a href="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3577049330,1894085967&fm=26&gp=0.jpg">王子公主</a>
            </p>
            <p class="story">
                故事待续...
            </p>
    """

    # 修复文档
    soup = BeautifulSoup(html,"lxml")
    print(soup.p.contents)

    # 节点选择

    # 打印
    print(soup.title)
    # 输出：
    print(type(soup.title))
    print(soup.title.string)
    # 打印head节点的html
    print(soup.head)
    # 获取第一个p标签；
    print(soup.p)

    ### 提取文档信息

    # 获取节点名称
    print(soup.title.name)
    # 获取属性值，字典类型；
    print(soup.p.attrs)
    print(soup.p.attrs["name"])

    # 获取文本内容，string属性；
    print(soup.p.b.string)

    # 嵌套选择
    print(soup.head.title)

    ### 关联选择

    # contents 属性：选取直接子节点
    print(soup.p.contents)

    #
# basic()


def basic2():
    html = """
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>童话故事</title>
        </head>
        <body>
            <p class="title" name="dromouse">
                <b>Zurich_Alacazar</b>
            </p>
            <p class="story">
                从前有座山，山上有座
                <a href="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565840005673&di=62c1016cfc220878086b827e609cffd9&imgtype=0&src=http%3A%2F%2Fnews.5068.com%2Fupfiles%2Fallimg%2F150131%2F8569_150131085538_1.jpg"><span>城堡</span></a>，
                城堡里有个
                <a href="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1565840137537&di=d101dc5429cbe5dba1dc4e4273f3ba20&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F17%2F54%2F88%2F058PICU58PICuCV_1024.jpg"><span>国王</span></a>
                还有许多
                <a href="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3577049330,1894085967&fm=26&gp=0.jpg">王子公主</a>
            </p>
            <p class="story">
                故事待续...
            </p>
    """

    # 修复文档
    soup = BeautifulSoup(html,"lxml")
    # 获取直接子节点,返回列表
    print(soup.p.contents)
    # 获取直接子节点，返回生成器；
    for i ,child in enumerate(soup.p.contents):
        print(i,child)
        # pass


    # 获取所有的子孙元素：descendants,返回类型为生成器；
    for descendants in soup.p.contents:
        print(descendants)
        print('------')


    # 获取直接父亲元素：parent属性；
    # 获取祖先元素：parents属性；
    # 获取兄弟元素：
    #       next_sibling  | previous_sibling :分别获取下一个兄弟元素和上一个兄弟元素；
    #       next_siblings | previous_siblings : 分别获取前面的兄弟元素和后面的兄弟元素；
# basic2()


def build():
    html ="""
        <div class="panel">
            <div class="panel-heading">
                <h4>HELLO WORD</h4>
            </div>
            <div class="panel-body">
                <ul class="list" id="list" name='elements'>
                            <li class="element">11</li>
                            <li class="element">22</li>
                            <li class="element">33</li>
                            <li class="element">44</li>
                </ul>
                <ul class="list list-small" id="list2">
                            <li class="element">1111111</li>
                            <li class="element">666</li>
                </ul>
            </div>
        </div>
    """
    soup = BeautifulSoup(html,"lxml")
    return soup

# find_all(name,attrs,text ,**kwargs,recusive)查找元素们

def test_find_all():
    soup = build()
    # 通过name 属性查找
    print(soup.find_all(name='ul'))
    print(type(soup.find_all(name='ul')[0]))
    print(soup.find_all(name='ul')[0].find_all(name='li'))

    # 通过属性查找
    print(soup.find_all(attrs={'id':'list','name':'elements'}))
    print(soup.find_all(id='list2'))

    # class是关键字，需要给一个下划线；
    print(soup.find_all(class_='list'))

    import  re
    # 通过文本查找

    print(soup.find_all(text=re.compile("^1+")))
    f = soup.find_all(text=re.compile("^1+"))
    print(type(f[0]))

    # find()  返回单个元素，即第一个匹配元素
    # find_parents()|find_parent  :
    # find_next_sibling()| find_next_sibling():
    # find_previous_sibling()| find previouos_sibling()
    # find_all_next() | find_next(): 返回节点后所有的（\第一个）符合条件的节点；

    # find_all_previous | find_previous(): 返回节点前所有的（\第一个）符合条件的节点；



    ### css 选择器：select()
    print(soup.select(".panel-body li"))
test_find_all()



