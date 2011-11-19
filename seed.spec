%define major 0
%define libname %mklibname %{name} %major
%define develname %mklibname -d %{name}

Summary: GObject JavaScriptCore bridge
Name: seed
Version: 3.2.0
Release: 1
License: LGPLv3+ and GPLv3+
Group: Development/Other
Url: http://live.gnome.org/Seed
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: gnome-common
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(gnome-js-common)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.6.3
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkitgtk-3.0)
BuildRequires: readline-devel
BuildRequires: mpfr-devel

Requires: %{libname} = %{version}-%{release}

%description
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.

%package -n %{libname}
Group: System/Libraries
Summary: GObject JavaScriptCore bridge - shared library

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary: GObject JavaScriptCore bridge - development library
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This packages contains the headers and libraries for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--with-webkit=3.0

%make

%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -name *.la | xargs rm 

%files
%doc README AUTHORS
%{_bindir}/seed
%{_datadir}/seed-gtk3
%{_mandir}/man1/seed.1*
%{_libdir}/seed-gtk3

%files -n %{libname}
%{_libdir}/libseed-gtk3.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/libseed-gtk3.so
%{_libdir}/pkgconfig/seed.pc
%{_includedir}/seed-gtk3
%{_datadir}/gtk-doc/html/seed

