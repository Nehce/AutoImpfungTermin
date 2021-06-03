# AutoImpfungTermin

德国疫苗预约需要先抢到code，然后用code去预约可用的Termin。
两个crawler分别针对code和Termin。


## 环境配置
* python3
* selenium
* chromedriver

## 运行步骤
1. 正确配置环境；
2. 打开py文件源码;
3. 设置chromedriver路径 (driver_path = r"XXX\chromedriver");
4. 设置src，即需想要打疫苗的地区所对应的116117网站地址，如 src="https://001-iz.impfterminservice.de/impftermine/service?plz=75056" ;
5. 在information和personal data下填入个人信息；
6. 保存退出，运行py文件。
