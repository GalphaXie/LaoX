#!/usr/bin/python3
# file: realtime_communication_model.py
# Created by Guang at 19-8-6
# description:

# *-* coding:utf8 *-*
# 即时通信模块， 参考参考

import random
import time


class Message(object):

    def __init__(self, msgarr=[], toacc=''):
        self.msgbody = msgarr # 此处为MsgDict对象实例的列表或者空列表
        self.toacc = toacc # toacc为字符串(单发)或者列表(批量发)
        self.msgrandom = random.randint(1, 1000000000)
        self.msgrequest = {
            'To_Account': toacc, # 消息接收方账号
            'MsgRandom': self.msgrandom, # 消息随机数，由随机函数产生
            'MsgBody': [t.msg for t in msgarr]
        }

    def del_option(self, option):
        if option in (set(self.msgrequest)-set(['To_Account', 'MsgRandom', 'MsgBody'])):
            self.__dict__.pop(option)
            self.msgrequest.pop(option)

    def append_msg(self, msg):
        self.msgbody.append(msg)
        self.msgrequest['MsgBody'].append(msg.msg)

    def insert_msg(self, index, msg):
        self.msgbody.insert(index, msg)
        self.msgrequest['MsgBody'].insert(msg.msg)

    def del_msg(self, index):
        if index in range(len(self.msgbody)):
            del self.msgbody[index]
            del sel.msgrequest['MsgBody'][index]

    def set_from(self, fromacc):
        # 指定消息的发送方，默认为服务器发送
        self.fromacc = fromacc
        self.msgrequest['From_Account'] = fromacc

    def set_to(self, toacc):
        # 指定消息的接收方，可以为String(单发),可以为List(批量发送)
        self.toacc = toacc
        self.msgrequest['To_Account'] = toacc

    def refresh_random(self):
        self.msgrandom = random.randint(1, 1000000000)
        self.msgrequest['MsgRandom'] = self.msgrandom, # 消息随机数，由随机函数产生

    def set_sync(self, sync):
        # 同步选项：1, 把消息同步到From_Account在线终端和漫游上
        #           2, 消息不同步至From_Account
        #           若不填写，默认情况下会将消息同步
        #           仅在单发单聊消息中可调用
        self.sync = sync
        self.msgrequest['SyncOtherMachine'] = sync

    def set_timestamp(self):
        # 设置消息时间戳，unix时间, 仅在单发单聊消息中可以调用
        self.timestamp = int(time.time())
        self.msgrequest['MsgTimeStamp'] = self.timestamp

    def set_offlinepush(self, pushflag=0, desc='', ext='', sound=''):
        # 仅适用于APNa推送，不适用于安卓厂商推送
        self.msgrequest['OfflinePushInfo'] = {
            'PushFlag': pushflag,
            'Desc': desc,
            'Ext': ext,
            'Sound': sound
        }


class MsgDict(object):

    def __init__(self, msgtype='', msgcontent={}):
        self.msgtype = msgtype
        self.msgcontent = msgcontent

    @property
    def msg(self):
        return {
            'MsgType': self.msgtype,
            'MsgContent': self.msgcontent
        }

    def set_content(self, content):
        self.msgcontent = content


class TextMsg(MsgDict):

    def __init__(self, text='', msgtype='TIMTextElem'):
        self.text = text
        content = {'Text': text}
        super(TextMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_text(self, text):
        self.text = text
        self.msgcontent['Text'] = text


class LocationMsg(MsgDict):

    def __init__(self, desc='', latitude=0, longitude=0, msgtype='TIMLocationElem'):
        self.desc = desc
        self.latitude = latitude
        self.longitude = longitude
        content = {
            'Desc': desc,  # 地理位置描述信息, String
            'Latitude': latitude, # 纬度, Number
            'Longitude': longitude # 经度, Number
        }
        super(LocationMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_desc(self, desc):
        self.desc = desc
        self.msgcontent['Desc'] = desc

    def set_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.msgcontent['Latitude'] = latitude
        self.msgcontent['Longitude'] = longitude

    def set_latitude(self, latitude):
        self.latitude = latitude
        self.msgcontent['Latitude'] = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude
        self.msgcontent['Longitude'] = longitude


class FaceMsg(MsgDict):

    def __init__(self, index=1, data='', msgtype='TIMFaceElem'):
        self.index = index
        self.data = data
        content = {
            'Index': index, # 表情索引，用户自定义, Number
            'Data': data # 额外数据, String
        }
        super(TextMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_index(self, index):
        self.index = index
        self.msgcontent['Index'] = index

    def set_data(self, data):
        self.data = data
        self.msgcontent['Data'] = data


class CustomMsg(MsgDict):

    def __init__(self, data='', desc='', ext='', sound='', msgtype='TIMCustomElem'):
        self.data = data
        self.desc = desc
        self.ext = ext
        self.sound = sound
        content = {
            'Data': data, # 自定义消息数据。不作为APNS的payload中字段下发，故从payload中无法获取Data字段, String
            'Desc': desc, # 自定义消息描述，当接收方为iphone后台在线时，做ios离线Push时文本展示
            'Ext': ext, # 扩展字段，当接收方为ios系统且应用处在后台时，此字段作为APNS请求包Payloads中的ext键值下发，Ext的协议格式由业务方确定，APNS只做透传
            'Sound': sound # 自定义APNS推送铃声
        }
        super(CustomMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_data(self, data):
        self.data = data
        self.msgcontent['Data'] = data

    def set_desc(self, desc):
        self.desc = desc
        self.msgcontent['Desc'] = desc

    def set_ext(self, ext):
        self.ext = ext
        self.msgcontent['Ext'] = ext

    def set_sound(self, sound):
        self.sound = sound
        self.msgcontent['Sound'] = sound


class SoundMsg(MsgDict):

    def __init__(self, uuid='', size=0, second=0, msgtype='TIMSoundElem'):
        self.uuid = uuid
        self.size = size
        self.second = second
        content = {
            'UUID': uuid, # 语音序列号，后台用于索引语音的键值，String
            'Size': size, # 语音数据大小, Number
            'Second': second # 语音时长，单位秒 Number
        }
        super(SoundMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_uuid(self, uuid):
        self.uuid = uuid
        self.msgcontent['UUID'] = uuid

    def set_size(self, size):
        self.size = size
        self.msgcontent['Size'] = size

    def set_second(self, second):
        self.second = second
        self.msgcontent['Second'] = second


class ImageMsg(MsgDict):

    def __init__(self, uuid='', imgformat=0, imginfo=[], msgtype='TIMImageElem'):
        self.uuid = uuid
        self.imgformat = imgformat
        self.imginfo = imginfo
        content = {
            'UUID': uuid, # 图片序列号，后台用于索引语音的键值，String
            'ImageFormat': imgformat, # 图片格式， BMP=1, JPG=2, GIF=3, 其他=0, Number
            'ImageInfoArray': [t.info for t in imginfo] # 原图，缩略图或者大图下载信息, Array
        }
        super(ImageMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_uuid(self, uuid):
        self.uuid = uuid
        self.msgcontent['UUID'] = uuid

    def set_format(self, imgformat):
        self.imgformat = imgformat
        self.msgcontent['ImageFormat'] = imgformat

    def append_info(self, info):
        # info 为ImageInfo对象实例
        self.imginfo.append(info)
        self.msgcontnet['ImageInfoArray'].append(info.info)

    def insert_info(self, index, info):
        self.imginfo.insert(index, info)
        self.msgcontent['ImageInfoArray'].insert(index, info.info)

    def del_info(self, index):
        del self.imginfo[index]
        del self.msgcontent['ImageInfoArray'][index]


class FileMsg(MsgDict):

    def __init__(self, uuid='', size=0, name='', msgtype='TIMFileElem'):
        self.uuid = uuid
        self.size = size
        self.name = name
        content = {
            'UUID': uuid, # 文件序列号，后台用于索引语音的键值，String
            'FileSize': size, # 文件数据大小, Number
            'FileName': name # 文件名称/路径， String
        }
        super(FileMsg, self).__init__(msgtype=msgtype, msgcontent=content)

    def set_uuid(self, uuid):
        self.uuid = uuid
        self.msgcontent['UUID'] = UUID

    def set_size(self, size):
        self.size = size
        self.msgcontent['FileSize'] = size

    def set_name(self, name):
        self.name = name
        self.msgcontent['FileName'] = name


class ImageInfo(object):

    def __init__(self, itype=1, size=0, width=0, height=0, url=''):
        #图片类型， 1-原图， 2-大图， 3-缩略图, 0-其他
        self.itype = itype
        # 图片数据大小,Number
        self.size = size
        # 图片宽度,Number
        self.width = width
        # 图片高度, Number
        self.height = height
        # 图片下载地址,String
        self.url = url

    @property
    def info(self):
        return {
            'Type': self.itype,
            'Size': self.size,
            'Width': self.width,
            'Height': self.height,
            'URL': self.url
        }

    def set_type(self, itype):
        self.itype = itype

    def set_size(self, size):
        self.size = size

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_url(self, url):
        self.url = url