%define api_version 2.2
%define lib_major	8
%define lib_name	%mklibname soup- %{api_version} %{lib_major}
%define develname %mklibname -d soup- %{api_version} 
%define oname libsoup
Summary: SOAP (Simple Object Access Protocol) implementation
Name: libsoup-2.2
Version: 2.2.104
Release: %mkrel 3
License: GPL/LGPL
Group: System/Libraries
URL: http://www.gnome.org/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{oname}-%{version}-buildroot
BuildRequires: glib2-devel
BuildRequires: gnutls-devel
BuildRequires: gtk-doc
BuildRequires: libxml2-devel

%description
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

%package -n %{lib_name}
Summary:        Libraries for soup
Group:          System/Libraries

%description -n %{lib_name}
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains libraries used by soup.

%package -n %develname
Summary:        Development libraries, header files and utilities for soup
Group:          Development/GNOME and GTK+
Provides:	%{oname}-%{api_version}-devel = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	glib2-devel
Conflicts:	%{_lib}soup-2.2_7-devel
Obsoletes: %mklibname -d soup- 2.2 8

%description -n %develname
Soup is a SOAP (Simple Object Access Protocol) implementation in C. 

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains the files necessary to develop applications with soup.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc README COPYING AUTHORS
%{_libdir}/*.so.%{lib_major}*

%files -n %develname
%defattr(-,root,root,-)
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/%{oname}
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*

