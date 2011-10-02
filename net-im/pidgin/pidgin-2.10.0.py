metadata = """
summary @ GTK instant messenger
license @ GPL-2
homepage @ http://pidgin.im
src_url @ http://downloads.sourceforge.net/$name/$fullname.tar.bz2
options @ gstreamer meanwhile tcl spell avahi python perl dbus sasl gtk ncurses zeroconf msn myspace networkmanager gnutls
"""

depends = """
runtime @ sys-libs/glibc x11-libs/startup-notification x11-misc/libxss
        x11-themes/hicolor-icon-theme app-misc/ca-certificates dev-util/intltool
"""

opt_runtime = """
dbus @ sys-apps/dbus
        dev-python/dbus-python
        dev-libs/dbus-glib
spell @ app-text/gtkspell
ncurses @ sys-libs/ncurses
        dbus @ x11-libs/gtk+
                x11-libs/libSM
gnutls @ net-libs/gnutls
msn @ net-libs/gnutls
gtk @ x11-libs/gtk+
sasl @ dev-libs/cyrus-sasl
meanwhile @ net-libs/meanwhile
gstreamer @ media-libs/gstreamer
networkmanager @ net-misc/networkmanager
tcl @ dev-lang/tcl
"""

# FIXME: the options and configure function will be improved. Take a look at msn for example: http://goo.gl/ps05p

get("main/gnome2_utils")

def prepare():
 #   patch("nm09-more.patch", level=1)
    patch("pidgin-2.7.4-icq-html-regression.patch")

def configure():
    conf("--disable-mono",
    "--disable-schemas-install",
    "--disable-avahi",
    "--disable-doxygen",
    config_enable("networkmanager", "nm"),
    "--with-system-ssl-certs=/etc/ssl/certs",
    "--disable-vv",
    config_enable("gstreamer"),
    "--disable-tcl",
    config_enable("gtk", "gtkui"),
    config_enable("dbus"),
    config_enable("spell", "gtkspell"),
    config_enable("ncurses", "consoleui"),
    config_enable("meanwhile"),
    config_enable("gnutls"),
    config_enable("sasl", "cyrus-sasl"),
    config_enable("tcl"))


def install():
    export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    raw_install("DESTDIR=%s" % install_dir)

def post_install():
    gnome2_icon_cache_update()
