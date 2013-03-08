Name:		x11-driver-input-keyboard
Version:	1.6.2
Release:	3
Summary:	Xorg input driver for keyboards
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
Patch0:		xf86-input-keyboard-1.6.2-link-against-xi.patch
BuildRequires:	x11-proto-devel >= 1.4
BuildRequires:	x11-server-devel >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xi)
Conflicts:	x11-server < 1.4

Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
This package provide Xorg input driver for keyboards.  The "keyboard" driver is
the standard OS-provided keyboard interface.  It is is built-in to the core X
server, and multiple instances are not supported. A loadable driver, kbd, is
available, and is planned to replace the keyboard driver in a future release of
the Xorg server.

%prep
%setup -qn xf86-input-keyboard-%{version}
#apply_patches

%build
autoreconf -fiv

%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.*
