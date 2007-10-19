Name: x11-driver-input-keyboard
Version: 1.2.2
Release: %mkrel 3
Summary: Xorg input driver for keyboards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

Patch1: xf86-input-keyboard-1.2.2-save-context.patch

BuildRequires: x11-proto-devel >= 1.4
BuildRequires: x11-server-devel >= 1.4
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: x11-server < 1.4

%description
This package provide Xorg input driver for keyboards.  The "keyboard" driver is
the standard OS-provided keyboard interface.  It is is built-in to the core X
server, and multiple instances are not supported. A loadable driver, kbd, is
available, and is planned to replace the keyboard driver in a future release of
the Xorg server.

%prep
%setup -q -n xf86-input-keyboard-%{version}
%patch1 -p1 -b .save-context

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

