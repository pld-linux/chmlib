Summary:	chmlib - library designed for accessing MS ITSS files
Summary(pl.UTF-8):	chmlib - biblioteka pozwalająca na dostęp do plików MS ITSS
Name:		chmlib
Version:	0.40
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://www.jedrea.com/chmlib/%{name}-%{version}.tar.gz
# Source0-md5:	96b8e9ac52015902941862171f5daa4c
Patch0:		%{name}-morearchs.patch
URL:		http://www.jedrea.com/chmlib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chmlib is a small library designed for accessing MS ITSS files. The
ITSS file format is used for Microsoft HTML Help files (.chm), which
have been the predominant medium for software documentation from
Microsoft during the past several years, having superceded the
previously used .hlp file format.

%description -l pl.UTF-8
chmlib to niewielka biblioteka przeznaczona do odczytu plików MS ITSS.
Format ITSS jest używany w plikach Microsoft HTML Help (.chm), które
stały się dominującym medium dla elektronicznej dokumentacji
udostępnianej przez Microsoft w ostatnim czasie, zastępując poprzednio
używane pliki .hlp.

%package devel
Summary:	chmlib header files
Summary(pl.UTF-8):	Pliki nagłówkowe chmlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed for building programs that use chmlib.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia programów z użyciem chmlib.

%package static
Summary:	chmlib static library
Summary(pl.UTF-8):	Biblioteka statyczna chmlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of chmlib.

%description static -l pl.UTF-8
Statyczna wersja chmlib.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure \
	--enable-examples

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libchm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libchm.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libchm.so
%{_libdir}/libchm.la
%{_includedir}/chm_lib.h
%{_includedir}/lzx.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libchm.a
