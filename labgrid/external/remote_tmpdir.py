"""
    RemoteTmpdir is a class that maintains a temporary directory on a
    remote linux system.
    Ex. when copying a test script or binary to DUT, RemoteTmpdir assists
    to prevent pollution of the target.

    RemoteTmpdir is to be created in a fixture, which can take care of a
    testmodule in a subdirectory. Recommended scope is function, to avoid
    polution between tests.

    See examples/remote_tmpdir
"""

import os


class RemoteTmpdir:

    # scriptdir is a directory relative to pytest root
    def __init__(self, shell, basedir=None, filetransfer=None):
        stdout = shell.run_check("mktemp -d")
        assert len(stdout) == 1
        self.path = stdout[0] + '/'
        if filetransfer is None:
            filetransfer = shell
        self.filetransfer = filetransfer
        self.basedir = basedir

        if self.basedir is not None and os.path.isfile(self.basedir):
            raise Exception("RemoteTmpdir: {} is not a directory".format(
                            self.basedir))


    ## Copy a file or contents of directory the created tmdir
    # path   file or directory to copy
    #        does not create sub directories, but copies all files
    def put(self, *items):
        for path in items:
            # resolve relative paths
            if not os.path.isabs(path) and self.basedir is not None:
                path = os.path.join(self.basedir, path)

            if os.path.isfile(path):
                remotepath = self.path + os.path.basename(path)
                self.filetransfer.put(path, remotepath)
            else:
                # then it is a whole directory to copy
                for filename in os.listdir(path):
                    localpath = os.path.join(path, filename)
                    remotepath = self.path + filename
                    if os.path.isfile(localpath):
                        self.filetransfer.put(localpath, remotepath)

    def get(self, *files, localdir=None):
        for path in files:
            remotepath = self.path + str(path)
            assert localdir or self.basedir, "RemoteTmpdir does not have basedir set, use localdir= in get"
            self.filetransfer.get(remotepath, localdir or self.basedir)
