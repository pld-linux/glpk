# Note: as of 4.49 old API was removed making all glpk users (ppl and octave) not to build.
#	Please don't STBR glpk >= 4.49 until ppl and octave are ported to new glpk API
Summary:	Solver LP and MIP problems
Summary(pl.UTF-8):	Narzędzie do rozwiązywania problemów LP i MIP
Name:		glpk
Version:	4.55
Release:	2
License:	GPL v3+
Group:		Applications/Math
Source0:	http://ftp.gnu.org/gnu/glpk/%{name}-%{version}.tar.gz
# Source0-md5:	c632a7a631b8aed02e28eafcd99477f7
Patch0:		%{name}-dl.patch
Patch1:		%{name}-sonames.patch
URL:		http://www.gnu.org/software/glpk/glpk.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	mysql-devel >= 5.5.10
BuildRequires:	unixODBC-devel >= 2.3.1
%ifarch %{x8664} ppc64 sparc64 s390x
Suggests:	libodbc.so.2()(64bit)
Suggests:	libmysqlclient.so.18()(64bit)
%else
Suggests:	libodbc.so.2
Suggests:	libmysqlclient.so.18
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GLPK package is intended for solving linear programming (LP) and
mixed integer linear programming (MIP) problems. It is a set of
routines organized in the form of a library and written in the ANSI C
programming language.

%description -l pl.UTF-8
Pakiet GLPK służy do rozwiązywania problemów programowania liniowego
(LP) oraz mieszanych problemów całkowitoliczbowego programowania
liniowego (MIP). Jest to zestaw narzędzi zorganizowanych w formie
biblioteki i napisanych w ANSI C.

%package devel
Summary:	Solver LP and MIP problems - header file
Summary(pl.UTF-8):	Narzędzie do rozwiązywania problemów LP i MIP - plik nagłówkowy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Solver LP and MIP problems - development files.

%description devel -l pl.UTF-8
Narzędzie do rozwiązywania problemów LP i MIP - pliki dla
programistów.

%package static
Summary:	Solver LP and MIP problems - static library
Summary(pl.UTF-8):	Narzędzie do rozwiązywania problemów LP i MIP - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Solver LP and MIP problems - static library.

%description static -l pl.UTF-8
Narzędzie do rozwiązywania problemów LP i MIP - biblioteka statyczna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-dl=dlfcn \
	--enable-mysql \
	--enable-odbc=unix \
	--with-gmp

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
%doc AUTHORS ChangeLog NEWS README THANKS doc/{*.txt,*.pdf,notes}
%attr(755,root,root) %{_bindir}/glpsol
%attr(755,root,root) %{_libdir}/libglpk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglpk.so.36

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglpk.so
%{_libdir}/libglpk.la
%{_includedir}/glpk.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libglpk.a
