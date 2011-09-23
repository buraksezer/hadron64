metadata = """
summary @ Lightweight Display Manager (part of LXDE)
homepage @ http://sourceforge.net/projects/lxdm/
license @ GPL
src_url @ http://downloads.sourceforge.net/lxde/$name-$version.tar.gz
arch @ ~x86
options @ nls debug
"""

depends = """
common @ sys-libs/pam sys-auth/consolekit x11-libs/libxcb
build @ dev-util/intltool dev-util/pkg-config
"""

opt_runtime = """
nls @ sys-devel/gettext
"""

def prepare():
    patch()
    autoreconf()
    if opt("nls"):
        system("intltoolize --force --copy --automake")
        #fix        strip-linguas -i "${S}/po" || die

def configure():
    conf(
    "--enable-password",
    "--with-pam",
    "--with-x",
    "--with-xconn=xcb",
    config_enable("debug"),
    config_enable("nls"))

def build():
    system("rm data/lxdm.conf")
    make()

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insfile("%s/lxdm.pam" % filesdir, "/etc/pam.d/lxdm")
    insexe("%s/lxdm-daemon" % filesdir, "/etc/rc.d/lxdm")

def post_install():
    system("sh %s/post_ins" % filesdir)

    #Check if exists in new version
    #http://projects.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/lxdm
    system("sed -i -e \"s/local\/libexec/lib\/lxdm/\" /etc/lxdm/lxdm.conf")

def post_remove():
    system("getent passwd lxdm >/dev/null 2>&1 && userdel lxdm")
    #TODO: check the next line, it fails. probably there is an error to create a group
    system("getent group lxdm >/dev/null 2>&1 && groupdel lxdm || /bin/true")
