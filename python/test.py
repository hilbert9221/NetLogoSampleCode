import pyNetLogo


def test():
    netlogo = pyNetLogo.NetLogoLink(
        netlogo_home='/home/rotopia/Downloads/NetLogo-6.2.1/',
        netlogo_version='6.2',
        # jvmargs: ['-Dkey=value', ...]
        # jvmargs=['-Djava.library.path=/home/rotopia/R/x86_64-pc-linux-gnu-library/4.1/rJava/jri'],
        )
    netlogo.load_model('../netlogo/model.nlogo')
    netlogo.command('setup')
    netlogo.command('repeat 1 [ go ]')
    netlogo.kill_workspace()


if __name__ == '__main__':
    test()
