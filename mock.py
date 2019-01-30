from mitmproxy import http
from urllib import parse
import json
import os

base_dir = os.getcwd()

def getMockData(host, path):
    with open(base_dir + "/config.json", "r") as config_f:
        config = json.load(config_f)

    for item in config.get("mockConfig"):
        if item.get("host") == host and item.get("enable"):
            with open(base_dir + "/datas/"+host+path, "r") as data:
                return data.read()
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