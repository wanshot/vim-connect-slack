# coding: utf-8
import requests
from vim import *


class SlackContribute:

    __post_api_url = 'https://slack.com/api/chat.postMessage'
    __postfile_api_url = 'https://slack.com/api/files.upload'
    __delete = 'https://slack.com/api/chat.delete'

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

        return requests.post(self.__post_api_url, params=post_api_info)

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

        return requests.post(self.__postfile_api_url, params=snippet_api_info)


def post(info, text):
    """ Post """
    return SlackContribute().post(info, text)


def post_snippet(info, content, opt):
    """ File Post """
    return SlackContribute().snippet(info, content, opt)


class SlackBrowse:
    __group_list_api_url = "https://slack.com/api/groups.list"
    __channel_list_api_url = "https://slack.com/api/channels.list"
    __history_api_url = "https://slack.com/api/channels.history"
    __user_info_api_url = "https://slack.com/api/users.info"
    __users_list = "https://slack.com/api/users.list"

    def channels(self, info):
        """
        API Document:
        https://api.slack.com/methods/channels.list
        """

        channels_api_info = {
            'token': info.get('token')
            }

        res = requests.get(self.__channel_list_api_url, params=channels_api_info)

        for d in res.json().get("channels"):
            print d.get("name") + " : " + d.get("id")

    def history(self, info, count):
        history_api_info = {
            'token': info.get("token"),
            'channel': info.get("channel"),
            'count': count
        }

        res = requests.get(self.__history_api_url, params=history_api_info)

        for d in res.json().get("messages"):
            print d.get("user") + " : " + d.get("text")

    def channel_name(self, info):

        channels_api_info = {
            'token': info.get('token')
            }

        res = requests.get(self.__channel_list_api_url, params=channels_api_info)
        result = [d.get("name") for d in res.json().get("channels") if d.get("id") == info.get("channel")]
        channel_name = "Unset Channel" if len(result) == 0 else result[0]
        print channel_name


def show_channels(info):
    """ Show SlackChannels  """
    return SlackBrowse().channels(info)


def show_history(info, count):
    """ Show Channel History """
    return SlackBrowse().history(info, count)


def get_channel_name(info):
    return SlackBrowse().channel_name(info)
