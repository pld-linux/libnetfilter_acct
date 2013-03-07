Summary:	netfilter extended accounting infrastructure library
Summary(pl.UTF-8):	Biblioteka rozszerzonej infrastruktury do rozliczania dla netfiltra
Name:		libnetfilter_acct
Version:	1.0.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.netfilter.org/projects/libnetfilter_acct/files/%{name}-%{version}.tar.bz2
# Source0-md5:	2118d9514c079839ebd9cb3144ad2ad7
URL:		http://www.netfilter.org/projects/libnetfilter_acct/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	libmnl-devel >= 1.0.0
BuildRequires:	libtool >= 2:2.0
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libmnl >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetfilter_acct is the userspace library providing interface to
extended accounting infrastructure.

%description -l pl.UTF-8
libnetfilter_acct to biblioteka przestrzeni użytkownika udostępniająca
interfejs do rozszerzonej infrastruktury do rozliczania.

%package devel
Summary:	Header files for libnetfilter_acct library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnetfilter_acct
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmnl-devel >= 1.0.0

%description devel
Header files for libnetfilter_acct library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnetfilter_acct.

%package static
Summary:	Static libnetfilter_acct library
Summary(pl.UTF-8):	Statyczna biblioteka libnetfilter_acct
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_acct library.

%description static -l pl.UTF-8
Statyczna biblioteka libnetfilter_acct.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libnetfilter_acct.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetfilter_acct.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_acct.so
%{_libdir}/libnetfilter_acct.la
%{_includedir}/libnetfilter_acct
%{_pkgconfigdir}/libnetfilter_acct.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetfilter_acct.a
