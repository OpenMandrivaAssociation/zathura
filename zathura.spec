%define debug_package %{nil}
Summary:	A lightweight PDF viewer
Name:		zathura
Version:	0.4.9
Release:	1
Group:		Office
License:	zlib
URL:		http://zathura.pwmt.org/projects/zathura
Source0:  https://pwmt.org/projects/zathura/download/zathura-%{version}.tar.xz
# Old
#Source0:	http://zathura.pwmt.org/attachments/download/10/%{name}-%{version}.tar.xz

BuildRequires:  librsvg2
BuildRequires:  meson
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(girara-gtk3)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(synctex)

%description
Zathura is a highly configurable and functional PDF viewer based on the Poppler
rendering library and the GTK+ toolkit. The idea behind zathura is an
application that provides a minimalist and space saving interface as well as
an easy usage that mainly focuses on keyboard interaction.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install


%files
%doc LICENSE README
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/applications/*



%changelog
* Thu May 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.0.8.5-1
+ Revision: 800395
- imported package zathura

