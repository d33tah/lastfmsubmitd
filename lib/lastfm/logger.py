import os
import logging

def getlog(name, logfile, debug=False):
    if debug:
        level = logging.DEBUG
    else:
        level = logging.INFO

    log = logging.getLogger(name)
    log.setLevel(level)

    format = logging.Formatter(
        '%(asctime)s %(name)s[%(process)s] %(levelname)s: %(message)s')

    logfile = logging.FileHandler(logfile)
    logfile.setLevel(level)
    logfile.setFormatter(format)
    log.addHandler(logfile)

    os.chmod(logfile, 0664)

    return log

def short_name(track):
    return '%s - %s [%d:%02d]' % ((track['artist'], track['title']) +
        divmod(track['length'], 60))
