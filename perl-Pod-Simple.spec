#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Pod
%define	pnam	Simple
Summary:	Pod::Simple - framework for parsing Pod
Summary(pl):	Pod::Simple - szkielet dla analizy Pod
Name:		perl-Pod-Simple
Version:	0.96
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-Pod-Escapes >= 1.03
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
Pod::Simple jest bibliotek± Perla do analizy tekstu w jêzyku
znaczników Pod ("plain old documentation"), w którym zazwyczaj pisana
jest dokumentacja Perla i modu³ów Perla. Format Pod jest obja¶niony na
stronie podrêcznika perlpod.3pm; najpopularniejszym programem do
formatowania tej dokumentacji jest "perldoc".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
