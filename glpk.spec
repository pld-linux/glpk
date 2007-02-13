Summary:	Solver LP and MIP problems
Summary(pl.UTF-8):	Narzędzie do rozwiązywania problemów LP i MIP
Name:		glpk
Version:	4.11
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://ftp.gnu.org/pub/gnu/glpk/%{name}-%{version}.tar.gz
# Source0-md5:	8f3ceb60b8a488cb93d5acd31fb780ac
URL:		http://www.gnu.org/software/glpk/glpk.html
BuildRequires:	autoconf
BuildRequires:	automake
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
Summary:	Solver LP and MIP problems - developers libraries
Summary(pl.UTF-8):	Narzędzie do rozwiązywania problemów LP i MIP - biblioteki.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Solver LP and MIP problems - libraries for developers

%description devel -l pl.UTF-8
Narzędzie do rozwiązywania problemów LP i MIP - biblioteki dla
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
