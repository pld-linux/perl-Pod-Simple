#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Simple
Summary:	Pod::Simple - framework for parsing Pod
Summary(pl):	Pod::Simple - szkielet dla analizy Pod
Name:		perl-Pod-Simple
Version:	2.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e7a74806215bc993ab1e8e7da49c9a2b
%if %{with tests}
BuildRequires:	perl-Pod-Escapes >= 1.03
%endif
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(overload()'

%description
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules. The Pod format is
explained in the perlpod.3pm man page; the most common formatter is
called "perldoc".

%description -l pl
Pod::Simple jest bibliotek� Perla do analizy tekstu w j�zyku
znacznik�w Pod ("plain old documentation"), w kt�rym zazwyczaj pisana
jest dokumentacja Perla i modu��w Perla. Format Pod jest obja�niony na
stronie podr�cznika perlpod.3pm; najpopularniejszym programem do
formatowania tej dokumentacji jest "perldoc".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Pod/Simple.pm
%dir %{perl_vendorlib}/Pod/Simple
%{perl_vendorlib}/Pod/Simple/*.pm
%{_mandir}/man3/*
