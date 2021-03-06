# 项目介绍

本项目是一个基于 [Mitmproxy](https://mitmproxy.org/) 的脚本，通过拦截网络请求，直接使用本地数据实现接口 mock。

# 使用方法

## 配置信息
mock 接口的 host 与 其开启状态配置
```
{
    "mockConfig": [
        {
            "host": "www.example.com",
            "enable": true,
            "dir":"www.example.com"
        }
    ]
}
```

## mock 数据放置
在 datas 目录下建一个 host 对应的目录 `www.example.com`，然后根据需要 mock 接口的 path 建相应的目录与文件。以下面的目录结构为例，实际 mock 的接口是 http://www.example.com/hello 和 http://www.example.com/test/aa。
```
datas
└── www.example.com
    ├── hello
    └── test
        └── aa
```

## mitmproxy 加载脚本
[mitmproxy 安装](https://docs.mitmproxy.org/stable/overview-installation/)

```
# 需要在本项目根目录下执行
mitmproxy -p [port] --listen-host [ip] -s mock.py
```

## 手机设置
手机和电脑连接到同一网络下，将手机的代理配置为电脑。

接下来就可以正常使用了。