%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	0
%define libname %mklibname %{name}-gtk3_ %{major}
%define devname %mklibname -d %{name}-gtk3

Summary:	GObject JavaScriptCore bridge
Name:		seed
Version:	3.2.0
Release:	2
License:	LGPLv3+ and GPLv3+
Group:		Development/Other
Url:		http://live.gnome.org/Seed
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seed/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		seed-3.2.0-linkage.patch

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	mpfr-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gnome-js-common)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.3
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libffi)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(webkitgtk-3.0)

%description
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.

%package -n %{libname}
Group:		System/Libraries
Summary:	GObject JavaScriptCore bridge - shared library
Obsoletes:	%{_lib}seed0 < 3.2.0-2

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{devname}
Summary:	GObject JavaScriptCore bridge - development library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}seed-devel < 3.2.0-2

%description -n %{devname}
This packages contains the headers and libraries for %{name}.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--enable-gtk-doc \
	--disable-static \
	--with-webkit=3.0

%make

%install
%makeinstall_std

%files
%doc README AUTHORS
%{_bindir}/seed
%{_libdir}/seed-gtk3
%{_datadir}/seed-gtk3
%{_mandir}/man1/seed.1*

%files -n %{libname}
%{_libdir}/libseed-gtk3.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_libdir}/libseed-gtk3.so
%{_libdir}/pkgconfig/seed.pc
%{_includedir}/seed-gtk3
%{_datadir}/gtk-doc/html/seed

