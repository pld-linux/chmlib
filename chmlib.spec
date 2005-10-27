Summary:	chmlib - library designed for accessing MS ITSS files
Summary(pl):	chmlib - biblioteka pozwalaj±ca na dostêp do plików MS ITSS
Name:		chmlib
Version:	0.37.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://66.93.236.84/~jedwin/projects/chmlib/%{name}-%{version}.tbz
# Source0-md5:	073f4cbb7cee68dc56b2e9b707503625
Patch0:		%{name}-morearchs.patch
Patch1:		%{name}-LIBDIR.patch
URL:		http://66.93.236.84/~jedwin/projects/chmlib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chmlib is a small library designed for accessing MS ITSS files. The
ITSS file format is used for Microsoft HTML Help files (.chm), which
have been the predominant medium for software documentation from
Microsoft during the past several years, having superceded the
previously used .hlp file format.

%description -l pl
chmlib to niewielka biblioteka przeznaczona do odczytu plików MS ITSS.
Format ITSS jest u¿ywany w plikach Microsoft HTML Help (.chm), które
sta³y siê dominuj±cym medium dla elektronicznej dokumentacji
udostêpnianej przez Microsoft w ostatnim czasie, zastêpuj±c poprzednio
u¿ywane pliki .hlp.

%package devel
Summary:	chmlib header files
Summary(pl):	Pliki nag³ówkowe chmlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed for building programs that use chmlib.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia programów z u¿yciem chmlib.

%package static
Summary:	chmlib static library
Summary(pl):	Biblioteka statyczna chmlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of chmlib.

%description static -l pl
Statyczna wersja chmlib.

%prep
%setup -q -n %{name}-0.37
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure

%{__make}

%{__make} examples \
	LIBDIR=src/.libs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
