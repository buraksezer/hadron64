metadata = """
summary @ Vi IMproved, an advanced text editor
homepage @ http://www.vim.org
license @ GPL-2
src_url @ ftp://ftp.vim.org/pub/vim/unix/vim-7.3.tar.bz2
http://hadronproject.org/distfiles/vim-patches-$version.tar.gz
arch @ ~x86
"""

depends = """
common @ sys-libs/ncurses dev-lang/python dev-lang/perl
"""

srcdir = "vim73"

def prepare():
    echo('#define SYS_VIMRC_FILE "/etc/vimrc"', "src/feature.h")
    items = ls("%s/vim-patches-%s" % (dirname(build_dir), version))
    if items:
        notify("applying vim-patches-%s" % version)
        items.sort()
        for item in items:
            patch(item, location="%s/vim-patches-%s" % (dirname(build_dir), version))

def configure():
    conf("--with-modified-by=Hadron",
            "--with-compiledby=Hadron",
            "--enable-multibyte",
            "--enable-pythoninterp",
            "--enable-perlinterp",
            "--with-features=huge",
            "--with-tlib=ncurses",
            "--with-x=no",
            "--enable-gui=no",
            "--enable-cscope",
            "--disable-python3interp", 
            "--disable-rubyinterp",
            "--disable-luainterp")

def install():
    raw_install("VIMRCLOC=/etc DESTDIR=%s install" % install_dir)
    copy("%s/vimrc" % filesdir, "/etc/vimrc")