Name: x11-driver-input-keyboard
Version: 1.1.1
Release: %mkrel 1
Summary: Xorg input driver for keyboards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
Patch0: x11-driver-input-keyboard-leds_status.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
This package provide Xorg input driver for keyboards.  The "keyboard" driver is
the standard OS-provided keyboard interface.  It is is built-in to the core X
server, and multiple instances are not supported. A loadable driver, kbd, is
available, and is planned to replace the keyboard driver in a future release of
the Xorg server.

%prep
%setup -q -n xf86-input-keyboard-%{version}
%patch0 -p1 -b .leds

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/keyboard_drv.la
%{_libdir}/xorg/modules/input/keyboard_drv.so
%{_libdir}/xorg/modules/input/kbd_drv.la
%{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.4.bz2
%{_mandir}/man4/keyboard.4.bz2


