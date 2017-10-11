''' Exceptions raise by Apps.
'''
class ChannelError(Exception):
    """ Base class for all exceptions

    Only to be invoked when only a more specific error is not available.
    """
    def __repr__(self):
        return "Hostname{0}, Reason:{1}".format(self.hostname, self.reason)

    def __str__(self):
        return self.__repr__()


class BadHostKeyException(ChannelError):
    ''' SSH channel could not be created since server's host keys could not
    be verified

    Contains:
    reason(string)
    e (paramiko exception object)
    hostname (string)
    '''

    def __init__(self, e, hostname):
        super().__init__()
        self.reason = "SSH channel could not be created since server's host keys could not be verified"
        self.hostname = hostname
        self.e = e

class BadScriptPath(ChannelError):
    ''' An error raised during execution of an app.
    What this exception contains depends entirely on context
    Contains:
    reason(string)
    e (paramiko exception object)
    hostname (string)
    '''

    def __init__(self, e, hostname):
        super().__init__()
        self.reason = "Inaccessible remote script dir. Specify script_dir"
        self.hostname = hostname
        self.e = e

class BadPermsScriptPath(ChannelError):
    ''' User does not have permissions to access the script_dir on the remote site

    Contains:
    reason(string)
    e (paramiko exception object)
    hostname (string)
    '''

    def __init__(self, e, hostname):
        super().__init__()
        self.reason = "User does not have permissions to access the script_dir"
        self.hostname = hostname
        self.e = e


class AuthException(ChannelError):
    ''' An error raised during execution of an app.
    What this exception contains depends entirely on context
    Contains:
    reason(string)
    e (paramiko exception object)
    hostname (string)
    '''

    def __init__(self, e, hostname):
        super().__init__()
        self.reason = "Authentication to remote server failed"
        self.hostname = hostname
        self.e = e

class SSHException(ChannelError):
    ''' if there was any other error connecting or establishing an SSH session

    Contains:
    reason(string)
    e (paramiko exception object)
    hostname (string)
    '''

    def __init__(self,e, hostname):
        super().__init__()
        self.reason = "Error connecting or establishing an SSH session"
        self.hostname = hostname
        self.e = e
