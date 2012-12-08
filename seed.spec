%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	GObject JavaScriptCore bridge
Name:		seed
Version:	3.2.0
Release:	2
License:	LGPLv3+ and GPLv3+
Group:		Development/Other
Url:		http://live.gnome.org/Seed
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch0:		seed-3.2.0-linkage.patch

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection
BuildRequires:	gtk-doc
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
BuildRequires:	readline-devel
BuildRequires:	mpfr-devel

Requires:	%{libname} = %{version}-%{release}

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

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary:	GObject JavaScriptCore bridge - development library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This packages contains the headers and libraries for %{name}.

%prep
%setup -q
%apply_patches

%build
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



%changelog
* Mon Nov 21 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.0-1
+ Revision: 732222
- added -p0 to fix linking (mga)
- fixed BRs
- new version 3.2.0
- cleaned up specs
- removed defattr
- removed clean & check sections
- shortened lib & devel descriptions
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 3.0.0-2
+ Revision: 686122
- rebuild for new webkit

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 649872
- new version 3.0.0

* Tue Mar 22 2011 Funda Wang <fwang@mandriva.org> 2.91.90-1
+ Revision: 647523
- New version 2.91.90

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574615
- new version
- drop patches
- we build with webkit 1.x/gtk+2.0 for now

* Fri Aug 06 2010 Funda Wang <fwang@mandriva.org> 2.30.0-3mdv2011.0
+ Revision: 566657
- final patches

* Fri Aug 06 2010 Funda Wang <fwang@mandriva.org> 2.30.0-2mdv2011.0
+ Revision: 566635
- BR gnome-common
- fix linkage
- add upstream git master patch to build with latest gir

* Mon Mar 29 2010 Funda Wang <fwang@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528709
- update to new version 2.30.0

* Tue Feb 23 2010 Funda Wang <fwang@mandriva.org> 2.29.91.1-1mdv2010.1
+ Revision: 509885
- new version 2.29.91.1

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.90-1mdv2010.1
+ Revision: 502715
- update to new version 2.29.90

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 2.29.6-1mdv2010.1
+ Revision: 496494
- update to new version 2.29.6

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 2.29.5.3-1mdv2010.1
+ Revision: 490058
- update to new version 2.29.5.3

* Fri Jan 08 2010 Götz Waschk <waschk@mandriva.org> 2.29.5.2-1mdv2010.1
+ Revision: 487446
- update to new version 2.29.5.2

* Sat Jan 02 2010 Götz Waschk <waschk@mandriva.org> 2.29.5.1-1mdv2010.1
+ Revision: 484947
- update to new version 2.29.5.1

* Thu Dec 17 2009 Götz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 479671
- update to new version 2.29.4

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.3-1mdv2010.1
+ Revision: 475426
- update to new version 2.29.3

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458791
- Release 2.28.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446172
- update to new version 2.28.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437441
- update to new version 2.27.92

* Sat Aug 22 2009 Götz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 419417
- update to new version 2.27.91

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414478
- update to new version 2.27.90

* Sat Jul 11 2009 Götz Waschk <waschk@mandriva.org> 0.8.5-1mdv2010.0
+ Revision: 394732
- update build deps
- new version
- add man page

* Fri May 29 2009 Götz Waschk <waschk@mandriva.org> 0.8-1mdv2010.0
+ Revision: 381153
- new version
- update deps
- update file list
- fix installation
- update deps

* Mon May 18 2009 Götz Waschk <waschk@mandriva.org> 0.7-2mdv2010.0
+ Revision: 376858
- fix installation on x86_64
- update build deps
- new version
- drop patches
- bump deps
- disable --no-undefined

* Thu Mar 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.3.1-5mdv2009.1
+ Revision: 354388
- Rebuild for new webkit major

* Wed Feb 25 2009 Götz Waschk <waschk@mandriva.org> 0.3.1-4mdv2009.1
+ Revision: 344844
- fix patch 2

* Thu Jan 22 2009 Götz Waschk <waschk@mandriva.org> 0.3.1-3mdv2009.1
+ Revision: 332451
- import seed


