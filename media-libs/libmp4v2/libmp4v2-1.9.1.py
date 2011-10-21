metadata ="""
summary @ MPEG4 library extracted from MPEG4IP, usually used in 3D sound systems.
homepage @ http://code.google.com/p/mp4v2
license @ MPL-1.1
src_url @ http://mp4v2.googlecode.com/files/mp4v2-1.9.1.tar.bz2
options @ static-libs utils
arch @ ~x86
"""

srcdir = "mp4v2-1.9.1"

def configure():
    raw_configure("--prefix=/usr",
            "--disable-dependency-tracking",
            "--disable-gch",
            config_enable("static-libs", "static"),
            config_enable("utils", "util"))

def install():
    raw_install("DESTDIR=%s" % install_dir)
    insdoc("COPYING", "INSTALL", "README", "doc/*")
    if opt('examples'):
        makedirs("%s/examples" % docdir)
        insinto("examples/*.c", "%s/examples/" % docdir)
        insinto("examples/*.h", "%s/examples/" % docdir)
 


