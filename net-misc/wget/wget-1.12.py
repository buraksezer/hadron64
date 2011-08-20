metadata = """
summary @ A network utility to retrieve files from the Web
homepage @ http://www.gnu.org/software/wget/wget.html
license @ GPL-3
src_url @ ftp://ftp.gnu.org/gnu/$name/$fullname.tar.gz
arch @ ~x86
options @ ipv6 idn debug nls
"""

depends = """
runtime @ sys-libs/glibc
        dev-libs/openssl
"""
opt_runtime = """
idn @ net-dns/libidn
nls @ sys-devel/gettext
"""

def prepare():
    patch(level=1)

def configure():
    conf(
    "--with-ssl",
    "--enable-opie",
    "--enable-digest",
    "--enable-ntlm",
    config_enable("debug"),
    config_enable("ipv6"),
    config_enable("idn", "iri"),
    config_enable("nls"))

def install():
    raw_install("DESTDIR=%s install" % install_dir)
    insdoc("AUTHORS", "COPYING", "ChangeLog*", "NEWS", "README", "MAILING-LIST")
