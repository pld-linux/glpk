Summary:	Solver LP and MIP problems
Summary(pl):	Narzêdzie do rozwi±zywania problemów LP i MIP
Name:		glpk
Version:	4.0
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	84485df00ca5eda302032e8ce92c29fd
URL:		http://www.gnu.org/software/glpk/glpk.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GLPK package is intended for solving linear programming (LP) and
mixed integer linear programming (MIP) problems. It is a set of
routines organized in the form of a library and written in the ANSI C
programming language.

%description -l pl
Pakiet GLPK s³u¿y do rozwi±zywania problemów programowania liniowego
(LP) oraz mieszanych problemów ca³kowitoliczbowego programowania
liniowego (MIP). Jest to zestaw narzêdzi zorganizowanych w formie
biblioteki i napisanych w ANSI C.

%package devel
Summary:	Solver LP and MIP problems - developers libraries.
Summary(pl):	Narzêdzie do rozwi±zywania problemów LP i MIP - biblioteki.
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Solver LP and MIP problems - libraries for developers

%description devel -l pl
Narzêdzie do rozwi±zywania problemów LP i MIP - biblioteki dla
programistów.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS doc/*
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
