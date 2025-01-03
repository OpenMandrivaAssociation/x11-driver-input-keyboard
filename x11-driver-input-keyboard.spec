Name:		x11-driver-input-keyboard
Version:	2.1.0
Release:	1
Summary:	Xorg input driver for keyboards
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.xz
Patch0:		xf86-input-keyboard-1.6.2-link-against-xi.patch
BuildRequires:	x11-proto-devel >= 1.4
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xi)
Conflicts:	x11-server < 1.4

Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)
Requires:	udev

%description
This package provide Xorg input driver for keyboards.  The "keyboard" driver is
the standard OS-provided keyboard interface.  It is is built-in to the core X
server, and multiple instances are not supported. A loadable driver, kbd, is
available, and is planned to replace the keyboard driver in a future release of
the Xorg server.

%prep
%setup -qn xf86-input-keyboard-%{version}
%autopatch -p1
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.4*
