Name: x11-driver-input-keyboard
Version: 1.2.2
Release: %mkrel 6
Summary: Xorg input driver for keyboards
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-input-keyboard xorg/drivers/xf86-input-keyboard
# cd xorg/drivers/xf86-input/keyboard
# git-archive --format=tar --prefix=xf86-input-keyboard-1.2.2/ xf86-input-keyboard-1.2.2 | bzip2 -9 > xf86-input-keyboard-1.2.2.tar.bz2
########################################################################
Source0: xf86-input-keyboard-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-input-keyboard-1.2.2..origin/mandriva+custom
Patch1: 0001-Remove-the-legacy-keyboard-driver-s-manpage.patch
Patch2: 0002-Sun-bug-6425775-Xserver-is-blocked-when-a-program-r.patch
Patch3: 0003-Update-kbd-man-page-to-say-it-has-replaced-keyboard.patch
Patch4: 0004-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch5: 0005-Add-support-for-the-SAVE_CONTEXT-patch-available-in.patch
Patch6: 0006-Missing-patch-to-avoid-problems-with-VT-switches.patch
Patch7: 0007-lnx-Automatically-inherit-the-vt-s-numlock-and-caps.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: x11-server < 1.4

%description
This package provide Xorg input driver for keyboards.  The "keyboard" driver is
the standard OS-provided keyboard interface.  It is is built-in to the core X
server, and multiple instances are not supported. A loadable driver, kbd, is
available, and is planned to replace the keyboard driver in a future release of
the Xorg server.

%prep
%setup -q -n xf86-input-keyboard-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/input/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.*
