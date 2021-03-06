from mitmproxy import http
from mitmproxy import ctx
from urllib import parse
import json
import os

base_dir = os.getcwd()

def getMockData(host, path):
    try:
        with open(base_dir + "/config.json", "r") as config_f:
            config = json.load(config_f)
    except IOError:
        ctx.log.error("Please start mitmproxy at root dir of MitmMock or Check config file")
        return None

    for item in config.get("mockConfig"):
        if item.get("host") == host and item.get("enable"):
            try:
                with open(base_dir + "/datas/" + item.get("dir") + path, "r") as data:
                    return data.read()
            except IOError:
                ctx.log.info("Not support " + path + " for " + host)
    return None

def request(flow: http.HTTPFlow) -> None:
    uri = parse.urlparse(flow.request.url)
    data = getMockData(uri.netloc, uri.path)
    if data != None:
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            # b"{\"errno\":1,\"data\":{}}",  # (optional) content
            data,
            {"Content-Type": "text/json"}  # (optional) headers
        )