%define name seed
%define version 0.3.1
%define release %mkrel 1

%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary: GObject JavaScriptCore bridge
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch: seed-0.3.1-libffi.patch
Patch1: seed-0.3.1-no-werror.patch
Patch2: seed-0.3.1-fix-linking.patch
#gw libseed is LGPL, seed is GPL
License: LGPLv3+ and GPLv3+
Group: Development/Other
Url: http://live.gnome.org/Seed
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ffi5-devel
BuildRequires: gobject-introspection-devel
BuildRequires: webkitgtk-devel
BuildRequires: readline-devel
BuildRequires: sqlite3-devel
BuildRequires: gtk-doc

%description
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.


%package -n %libname
Group: System/Libraries
Summary: GObject JavaScriptCore bridge - shared library

%description -n %libname
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.

%package -n %develname
Summary: GObject JavaScriptCore bridge - development library
Group: Development/C
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %develname
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the
GObject type system. In a more concrete sense, Seed enables you to
immediately write applications around a significant portion of the
GNOME platform, and easily embed JavaScript as a scripting-language in
your GObject library.


%prep
%setup -q -n %name-0.3
%patch -p1
%patch1 -p1
%patch2 -p1 -b .fix-linking
libtoolize --copy --force
autoreconf

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/{*.a,seed/*.a}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS
%_bindir/seed
%_bindir/seed_turtle
%_datadir/seed
%_libdir/seed

%files -n %libname
%defattr(-,root,root)
%_libdir/libseed.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%_libdir/libseed.so
%_libdir/libseed.la
%_libdir/pkgconfig/seed.pc
%_includedir/seed
%_datadir/gtk-doc/html/seed