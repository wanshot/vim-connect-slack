# coding: utf-8
import os
import vim
import time
import codecs
import shelve
import requests


def exception(func):
    """ Connection Error """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            print "ConnectionError"
        except requests.exceptions.Timeout:
            print "Timeout"
        except requests.exceptions.HTTPError:
            print "HTTPError"
    return wrapper


class SlackContribute:

    __post_api_url = 'https://slack.com/api/chat.postMessage'
    __postfile_api_url = 'https://slack.com/api/files.upload'
    __delete = 'https://slack.com/api/chat.delete'

    @exception
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

    @exception
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
    if isinstance(info, dict):
        return SlackContribute().post(info, text)
    else:
        print info


def post_snippet(info, content, opt):
    """ File Post """
    if isinstance(info, dict):
        return SlackContribute().snippet(info, content, opt)
    else:
        print info


class SlackBrowse:
    __group_list_api_url = "https://slack.com/api/groups.list"
    __channel_list_api_url = "https://slack.com/api/channels.list"
    __history_api_url = "https://slack.com/api/channels.history"
    __user_info_api_url = "https://slack.com/api/users.info"
    __users_list = "https://slack.com/api/users.list"

    def channels(self, info, db_path, ch_id, ch_name):
        """
        API Document:
        https://api.slack.com/methods/channels.list
        """

        line = 0
        channel_list = Database().channels(db_path)

        with codecs.open("__SlackChannels__", "w", "utf-8") as f:
            for i, d in enumerate(channel_list):
                if d.get("id") == ch_id:
                    line = i
                    ch_name = d.get("name")
                if d.get("purpose"):
                    f.write("@" + "{0:<20}".format(d.get("name")) + "#" + " " + d.get("purpose")[:60] + "\n")
                else:
                    f.write("@" + "{0:<20}".format(d.get("name")) + "#" + "\n")
        return line, ch_name

    def choice_ch(self, info, ch, db_path):

        ch_name = ch[1:20].strip()
        channel_list = Database().channels(db_path)
        channel_id = [d.get("id") for d in channel_list if d.get("name") == ch_name]

        vim.command(':let g:Channel = "%s"' % channel_id[0])
        vim.command(':let g:ChannelName = "%s"' % ch_name)

    @exception
    def history(self, info, count, db_path):
        """
        API Document
        https://api.slack.com/methods/channels.history
        """
        history_api_info = {
            'token': info.get("token"),
            'channel': info.get("channel"),
            'count': count
        }

        res = requests.get(self.__history_api_url, params=history_api_info)

        if res.json().get("ok"):
            if os.path.isfile(db_path + "/slack_data.db"):
                user_list = Database().members(db_path)
                for d in res.json().get("messages"):
                    name = [dic.get("name") for dic in user_list if dic.get("id") == d.get("user")]
                    try:
                        print name[0] + " : " + d.get("text")
                    except IndexError:
                        print "BOT" + " : " + d.get("text")
            else:
                for d in res.json().get("messages"):
                    print d.get("user") + " : " + d.get("text")
        else:
            print "Setting Error. Plz refer to this URL https://api.slack.com/web'"


def show_channels(info, db_path, ch_id, ch_name):
    """
    Show SlackChannels
    Available in SlackMode
    """
    if os.path.isfile(db_path + "/slack_data.db"):
        if isinstance(info, dict):
            (line_num, ch_name) = SlackBrowse().channels(info, db_path, ch_id, ch_name)
            vim.command('call RenderSlackChannelsBuffer()')
            vim.command('setlocal nomodifiable')
            vim.command('sign define channel text=>> texthl=Search')
            if line_num == 0:
                pass
            else:
                vim.command('exe ":sign place 2 line={} name=channel file=" . expand("%:p")'.format(line_num + 1))
        else:
            print info
    else:
        print 'Plz run the "SlackMode"'


def choice_channel(info, ch, db_path):
    """
    return SlackChannel-ID
    Available in SlackMode
    """
    if os.path.isfile(db_path + "/slack_data.db"):
        if isinstance(info, dict):
            return SlackBrowse().choice_ch(info, ch, db_path)
        else:
            print info
    else:
        print 'Plz run the "SlackMode"'


def show_history(info, count, db_path):
    """ Show Channel History """
    if isinstance(info, dict):
        return SlackBrowse().history(info, count, db_path)
    else:
        print info


class Database:

    __users_list_api = "https://slack.com/api/users.list"
    __channels_list_api = "https://slack.com/api/channels.list"

    def mode_on(self, autoload_path, info):
        """
        Running Mode On and checks the existence of DB , creating DB
        If the database exists, it will insert the API Data
        """
        if isinstance(info, dict):

            if os.path.isfile(autoload_path + "/slack_data.db"):
                os.remove(autoload_path + "/slack_data.db")
            else:
                pass

            db = shelve.open(autoload_path + '/slack_data')
            try:
                db["ml"] = _get_member_list(self.__users_list_api, info)
                time.sleep(1)
                db["cl"] = _get_channel_list(self.__channels_list_api, info)
            finally:
                db.close()
                print "SlackMode Enable"
        else:
            print info

    def members(self, autoload_path):
        """ load members """
        db = shelve.open(autoload_path + '/slack_data')
        return db["ml"]

    def channels(self, autoload_path):
        """ Load Channels """
        db = shelve.open(autoload_path + '/slack_data')
        return db["cl"]


def _get_member_list(url, info):
    """ Get [{"id":user_id, "name":user_name}...] """
    res = requests.get(url, params=info)
    return [{"id": d.get("id"), "name": d.get("name")} for d in res.json().get("members")]


def _get_channel_list(url, info):
    """ Get [{"id":channel_id, "name":channel_name, "purpose":purpose}...] """
    res = requests.get(url, params=info)
    return [
        {
            "id": d.get("id"),
            "name": d.get("name"),
            "purpose": d.get("purpose")["value"]
        } for d in res.json().get("channels")]
