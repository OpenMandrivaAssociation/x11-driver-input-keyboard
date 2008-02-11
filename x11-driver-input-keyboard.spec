Name: x11-driver-input-keyboard
Version: 1.2.2
Release: %mkrel 10
Summary: Xorg input driver for keyboards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.4
BuildRequires: x11-server-devel >= 1.4-6mdv
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: x11-server < 1.4

# git format-patch 10792dc1eebf9f718e0cad0b425a8b8307a7ebc7..mandriva
Patch1: 0001-Sun-bug-6425775-Xserver-is-blocked-when-a-program-r.patch
Patch2: 0002-Update-kbd-man-page-to-say-it-has-replaced-keyboard.patch
Patch3: 0003-Don-t-sleep-1-on-VT-entry.patch
Patch4: 0004-Fix-parameters-order-for-printWsType.patch
Patch5: 0005-lnx-Automatically-inherit-the-vt-s-numlock-and-caps.patch
Patch6: 0006-Add-support-for-the-SAVE_CONTEXT-Mandriva-patch.patch
Patch7: 0007-Update-leds-properly-based-on-console-state.patch

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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/kbd_drv.la
%{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.*
