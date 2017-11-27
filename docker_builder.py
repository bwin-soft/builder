#!/usr/local/bin/python3.6
# coding: utf-8

# ##### 镜像构建脚本
import docker
import json
import os
client = docker.from_env()
REGISTRY = "registry.cn-shenzhen.aliyuncs.com/bwin/"


def login(username="lihong@namiao",
          password="BpmPortal123",
          registry="registry.cn-shenzhen.aliyuncs.com"):
    user = username
    pwd = password
    reg = registry
    login = client.login(username=user, password=pwd, registry=reg)
    if 'Status' in login:
        ok = login["Status"] == "Login Succeeded"
        return ok
    return False


def update_config(current, newVersion):
    img, reg, ver, fn = current
    cfg = None
    with open(os.path.join(fn, 'image.conf'), 'r') as cfg_file:
        cfg = json.load(cfg_file)
        cfg["last_version"] = newVersion
    with open(os.path.join(fn, 'image.conf'), 'w') as cfg_file:
        json.dump(cfg, cfg_file)


def build_image(image_name, registry, tg, docker_path):
    build_ok = True
    try:
        print("开始创建-{}-镜像......".format(image_name))
        print("路径:", os.path.join('.', docker_path))
        print("仓库地址:", registry)
        print("版本:", tg)
        image = client.images.build(
            path=os.path.join('.', docker_path),
            tag="{}:{}".format(registry, tg),
            rm=True,
            pull=True,
            quiet=False)
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
    return build_ok


def run_task(name, registry, version, path):
    build_ok = build_image(name, registry, version, path)
    if build_ok:
        print("构建成功，准备push到镜像仓库......")
        try:
            for line in client.images.push(
                    repository=registry,
                    tag=version,
                    stream=True,
                    auth_config={
                        "username": "lihong@namiao",
                        "password": "BpmPortal123"
                    }):
                print(line)
            print("push 完成，请检查push结果。")
            return True
        except:
            print("push 失败！")
            return False
    else:
        return build_ok


print(login())  # login to aliyun registry
print(login(
    username="lihongwansui",
    password="Internet111",
    registry="https://index.docker.io/v1/"))  # login to docker hub

dirs = [
    fn for fn in os.listdir('.')
    if os.path.isdir(fn) and os.path.exists(os.path.join(fn, "image.conf"))
]
menus = {}
menu_idx = 1
for fn in dirs:
    with open(os.path.join(fn, 'image.conf')) as cfg_file:
        cfg = json.load(cfg_file)
        menus[str(menu_idx)] = ((cfg['image'], cfg['registry'],
                                 cfg['last_version'], fn))
    menu_idx += 1
for idx, de in menus.items():
    img, reg, ver, fn = de
    print(idx, ":", "[", img, "]", ",当前版本:", ver)

current = None
choice = input("选择要创建的镜像: ")
if choice in menus:
    current = menus[choice]
    print("当前版本号:{}".format(menus[choice][2]))
else:
    print("选择错误！")
    os._exit(0)
version = input("输入新版本号:")
if version:
    img, reg, ver, fn = current
    if run_task(img, reg, version, fn):
        # if True:
        update_config(current, version)
        print("制作镜像完成")
