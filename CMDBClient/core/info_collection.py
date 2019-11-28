from plugins import plugin_api
import json, platform, sys


class InfoCollection(object):
    """收集硬件信息"""
    def __init__(self):
        pass

    def get_platform(self):

        os_platform = platform.system()

        return os_platform

    def collect(self):
        """收集硬件数据"""
        os_platform = self.get_platform()
        try:
            func = getattr(self, os_platform)
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError as e:
            sys.exit("Error:MadKing doens't support os [%s]! " % os_platform)

    def Linux(self):
        sys_info = plugin_api.LinuxSysInfo()

        return sys_info

    def Windows(self):
        sys_info = plugin_api.WindowsSysInfo()
        # f = file('data_tmp.txt','wb')
        # f.write(json.dumps(sys_info))
        # f.close()
        return sys_info

    def build_report_data(self, data):

        # add token info in here before send

        return data
