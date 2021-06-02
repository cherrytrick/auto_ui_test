# ui_auto unittest自动化测试框架

----

## 框架设计

* unittest单元测试框架,实现ui自动测试
* selenium自动化测试工具
* POM模型(Page Object Model页面对象模型设计)
* 可以复用框架，使用基类里面的方法，改变ini文件变量测试不同的事件
* 感谢  随风挥手https://home.cnblogs.com/u/wxhou/ 提供的架构思路

----

## 目录结构

    common                 ——公共类
    config                 ——配置文件和读取配置
    logs                   ——日志记录路径
    page                   ——基类（封装selenium方法）
    page_element           ——页面元素类
    page_object            ——页面对象类
    report                 ——报告文件
    TestCase               ——测试用例
    utils                  ——工具类
    run_case.py            ——总执行文件

----

## 运行

```shell
python run_case.py
```
```shell
pycharm addconfiguration为test_search.py
```

##技术总结

* selenium自动化测试，在Jenkins运行以后可以持续的进行回归测试，可以节省人力成本和增强测试的规范性
* POM模型可以UI层操作、业务流程与验证分离，结构清晰，便于维护复用。
* 定位元素时一定要确定元素的准确性，框架的很多错误基于元素定位不到而报错。python与java等静态语言相比，变量的灵活性
比较高，更加的灵活但更加不容易维护。多写注释时我的解决方法。
* 本系统时一个可以复用的框架，在基类里定义了很多示例没有使用的方法，根据业务需求对这些方法进行使用并进行变更。
* 本系统沿用了测试用例时百度搜索的经典方法。