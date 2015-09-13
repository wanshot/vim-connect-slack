# coding: utf-8
import requests
from vim import *


class Slack:

    __post_api_url = 'https://slack.com/api/chat.postMessage'
    __postfile_api_url = 'https://slack.com/api/files.upload'
    __delete = 'https://slack.com/api/chat.delete'
    __group_list_api_url = "https://slack.com/api/groups.list"
    __channel_list_api_url = "https://slack.com/api/channels.list"
    __history_api_url = "https://slack.com/api/channels.history"
    __user_info_api_url = "https://slack.com/api/users.info"

    def __init__(self):
        pass

    def post(self, info, text):
        """
        API Document:
        https://api.slack.com/methods/files.upload
        """

        post_api_info = {
            'token': info.get('token'),
            'channel': info.get('channel'),
            'text': text,
            'as_user': 'true',
            'username': info.get('username'),
            'unfurl_links': 'false'
        }

        requests.post(self.__post_api_url, params=post_api_info)

    def snippet(self, info, content, opt):
        """
        API Document:
        https://api.slack.com/methods/files.list
        """

        snippet_api_info = {
            'token': info.get("token"),
            'filetype': opt[0],
            'title': opt[1],
            'channels': info.get("channel"),
            'content': content
        }

        requests.post(self.__postfile_api_url, params=snippet_api_info)

    def channel(self, info):
        """
        API Document:
        https://api.slack.com/methods/channels.list
        """

        channels_api_info = {
            'token': info.get('token')
            }

        res = requests.get(self.__channel_list_api_url, params=channels_api_info)

        json_data = res.json().get("channels")
        for info in json_data:
            print info.get("name") + " : " + info.get("id")

    def history(self, info, count):
        history_api_info = {
            'token': info.get("token"),
            'channel': info.get("channel"),
            'count': count
        }

        res = requests.get(self.__history_api_url, params=history_api_info)

        for info in res.json().get("messages"):
            print info.get("user") + " : " + info.get("text")


def post(info, text):
    """ Post """
    return Slack().post(info, text)


def post_snippet(info, content, opt):
    """ File Post """
    return Slack().snippet(info, content, opt)


def show_channels(info):
    """ Show SlackChannels  """
    return Slack().channel(info)


def show_history(info, count):
    """ Show Channel History """
    return Slack().history(info, count)
