Summary:	Solver LP and MIP problems
Summary(pl):	Narz�dzie do rozwi�zywania problem�w LP i MIP
Name:		glpk
Version:	4.0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	84485df00ca5eda302032e8ce92c29fd
URL:		http://www.gnu.org/software/glpk/glpk.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GLPK package is intended for solving linear programming (LP) and
mixed integer linear programming (MIP) problems. It is a set of routines
organized in the form of a library and written in the ANSI C programming
language.

%description -l pl
Pakiet GLPK s�u�y do rozwi�zywania problem�w programowania liniowego
(LP) oraz mieszanych problem�w ca�kowitoliczbowego programowania
liniowego (MIP). Jest to zestaw narz�dzi zorganizowanych w formie
biblioteki i napisanych w ANSI C.

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
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.a
%{_includedir}/*.h
%doc README NEWS doc/*
