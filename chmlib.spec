Summary:	chmlib - library designed for accessing MS ITSS files
Summary(pl):	chmlib - biblioteka pozwalaj�ca na dost�p do plik�w MS ITSS
Name:		chmlib
Version:	0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://64.81.172.220/~jedwin/projects/chmlib/%{name}-%{version}.tbz
URL:		http://64.81.172.220/~jedwin/projects/chmlib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chmlib is a small library designed for accessing MS ITSS files. The
ITSS file format is used for Microsoft Html Help files (.chm), which
have been the predominant medium for software documentation from
Microsoft during the past several years, having superceded the
previously used .hlp file format.

%description -l pl
chmlib to niewielka biblioteka przeznaczona do odczytu plik�w MS ITSS.
Format ITSS jest u�ywany w plikach Microsoft Html Help (.chm), kt�re
sta�y si� dominuj�cym medium dla elektronicznej dokumentacji
udost�pnianej przez Microsoft w ostatnim czasie, zast�puj�c poprzednio
u�ywane pliki .hlp.

%package devel
Summary:	chmlib header files
Summary(pl):	Pliki nag��wkowe chmlib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files needed for building programs that use chmlib.

%description devel -l pl
Pliki nag��wkowe potrzebne do tworzenia program�w z u�yciem chmlib.

%package static
Summary:	chmlib static library
Summary(pl):	Biblioteka statyczna chmlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of chmlib.

%description static -l pl
Statyczna wersja chmlib.

%prep
%setup -q

%build
%{__make} all examples \
	CFLAGS="%{rpmcflags} -DCHM_MT -DCHM_USE_PREAD -DCHM_USE_IO64 -L.libs" \
	LDFLAGS="%{rpmldflags} -lpthread" \
	CC="%{__cc}" LD="%{__cc}" \
	INSTALLPREFIX="%{_prefix}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir}}

%{__make} install \
	INSTALLPREFIX=$RPM_BUILD_ROOT%{_prefix}

install *_chmLib chm_http $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
