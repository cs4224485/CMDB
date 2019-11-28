


def LinuxSysInfo():
    #print __file__
    from plugins.linux import sysinfo
    return sysinfo.collect()


def WindowsSysInfo():
    from plugins.windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()