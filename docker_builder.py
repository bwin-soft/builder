#!/usr/local/bin/python3.6
# coding: utf-8

# ##### 镜像构建脚本

# In[79]:


import docker
import json
client = docker.from_env()
REGISTRY = "registry.cn-shenzhen.aliyuncs.com/bwin/"
def login(username="lihong@namiao",password="BpmPortal123",registry="registry.cn-shenzhen.aliyuncs.com"):
    user = username
    pwd = password
    reg = registry
    #print(user,pwd,reg)
    login = client.login(username=user,password=pwd,registry=reg)
    #print (login.get('Status'))
    #ok = login[u"Status"] == u"Login Succeeded"
    #return ok
login() # login to aliyun registry
login(username="lihongwansui",password="Internet111",registry="https://index.docker.io/v1/") # login to docker hub


# In[80]:


def load_versions():
    with open('configration.json') as cfg_file:  
        cfg = json.load(cfg_file)
        return cfg
def update_versions(cfg):
    with open('configration.json', 'w') as outfile:  
        json.dump(cfg, outfile)
        
versions = load_versions()
if len(versions) == 0:
    cfg = {"1":1,"2":1,"3":1,"4":1,"5":1,"6":"1.0"}
    update_versions(cfg)
    versions = load_versions()
    print(versions)


# In[81]:


print(" \n      1.tomcat7 + jdk8; \n      2.nginx + tomcat7 + jdk8;\n      3.front service; \n      4.trade service; \n      5.wechat service; \n      6.nginx loadbalance for coin \n")


# In[88]:


choice = input("选择要创建的镜像: ") 
if choice in versions:
    print("当前版本号:{}".format(versions[choice]))
else:
    print("选择错误！")
    #exit
version = input("输入新版本号:")


# In[83]:


def build_image(image_name,registry,tg,docker_path):
    build_ok = True
    try:
        print("开始创建-{}-镜像......".format(image_name))
        image = client.images.build(path=docker_path,tag="{}:{}".format(registry,tg),rm=True,pull=True,quiet=False)
        print("镜像构建完成 -({})".format(image.tag))
    except docker.errors.BuildError as be:
        build_ok = False
        print("镜像构建错误: {0}".format(be))
    except docker.errors.APIError as ae:
        build_ok = False
        print("镜像构建错误: {0}".format(ae))
    except TypeError as te:
        build_ok = False
        print("镜像构建错误: {0}".format(te))
    versions[choice] = tg
    update_versions(versions)
    return build_ok



# In[87]:


if choice == "1":
    build_ok = build_image("tomcat_7_jdk8","registry.cn-shenzhen.aliyuncs.com/bwin/tomcat_7_jdk8",version,"./tomcat_7_jdk8")
    if build_ok:
        print("构建成功，准备push到镜像仓库......")
        try:
            for line in client.images.push(repository="registry.cn-shenzhen.aliyuncs.com/bwin/tomcat_7_jdk8",tag=version,stream=True,auth_config={"username":"lihong@namiao","password":"BpmPortal123"}):
                print(line)
            print("push 完成，请检查push结果。")
        except:
            print("push 失败！")
if choice == "2":
    build_ok = build_image("nginx_tomcat_7_jdk8","registry.cn-shenzhen.aliyuncs.com/bwin/nginx_tomcat",version,"./nginx_tomcat_7_jdk8")
    if build_ok:
        print("构建成功，准备push到镜像仓库......")
        try:
            for line in client.images.push(repository="registry.cn-shenzhen.aliyuncs.com/bwin/nginx_tomcat",tag=version,stream=True,auth_config={"username":"lihong@namiao","password":"BpmPortal123"}):
                print(line)
            print("push 完成，请检查push结果。")
        except:
            print("push 失败！")
if choice == "3":
    build_ok = build_image("front_service","registry.cn-shenzhen.aliyuncs.com/bwin/front_service",version,"./front_service")
    if build_ok:
        print("构建成功，准备push到镜像仓库......")
        try:
            for line in client.images.push(repository="registry.cn-shenzhen.aliyuncs.com/bwin/front_service",tag=version,stream=True,auth_config={"username":"lihong@namiao","password":"BpmPortal123"}):
                print(line)
            print("push 完成，请检查push结果。")
        except:
            print("push 失败！")
if choice == "4":
    build_ok = build_image("trade_service","registry.cn-shenzhen.aliyuncs.com/bwin/trade_service",version,"./trade_service")
    if build_ok:
        print("构建成功，准备push到镜像仓库......")
        try:
            for line in client.images.push(repository="registry.cn-shenzhen.aliyuncs.com/bwin/trade_service",tag=version,stream=True,auth_config={"username":"lihong@namiao","password":"BpmPortal123"}):
                print(line)
            print("push 完成，请检查push结果。")
        except:
            print("push 失败！")
if choice == "5":
    build_ok = build_image("wechat_service","registry.cn-shenzhen.aliyuncs.com/bwin/wechat_service",version,"./wechat_service")
    if build_ok:
        print("构建成功，准备push到镜像仓库......")
        try:
            for line in client.images.push(repository="registry.cn-shenzhen.aliyuncs.com/bwin/wechat_service",tag=version,stream=True,auth_config={"username":"lihong@namiao","password":"BpmPortal123"}):
                print(line)
            print("push 完成，请检查push结果。")
        except:
            print("push 失败！")
if choice == "6":
    build_ok = build_image("nginx_lb_coin","registry.cn-shenzhen.aliyuncs.com/bwin/nginx_lb_coin",version,"./nginx_lb_coin")
    if build_ok:
        print("构建成功，准备push到镜像仓库......")
        try:
            for line in client.images.push(repository="registry.cn-shenzhen.aliyuncs.com/bwin/nginx_lb_coin",tag=version,stream=True,auth_config={"username":"lihong@namiao","password":"BpmPortal123"}):
                print(line)
            print("push 完成，请检查push结果。")
        except:
            print("push 失败！")
