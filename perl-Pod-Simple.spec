#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Pod
%define		pnam	Simple
Summary:	Pod::Simple - framework for parsing Pod
Summary(pl.UTF-8):	Pod::Simple - szkielet dla analizy Pod
Name:		perl-Pod-Simple
Version:	3.32
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f05e92d19c8a7301910f133424e74ece
URL:		https://metacpan.org/release/Pod-Simple
%if %{with tests}
BuildRequires:	perl(Test) >= 1.25
BuildRequires:	perl(Text::Wrap) >= 98.112902
BuildRequires:	perl-Pod-Escapes >= 1.04
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules. The Pod format is
explained in the perlpod.3pm man page; the most common formatter is
called "perldoc".

%description -l pl.UTF-8
Pod::Simple jest biblioteką Perla do analizy tekstu w języku
znaczników Pod ("plain old documentation"), w którym zazwyczaj pisana
jest dokumentacja Perla i modułów Perla. Format Pod jest objaśniony na
stronie podręcznika perlpod.3pm; najpopularniejszym programem do
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

# packaged as man
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Pod/{Simple,Simple/Subclassing}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Pod/Simple.pm
%dir %{perl_vendorlib}/Pod/Simple
%{perl_vendorlib}/Pod/Simple/*.pm
%{_mandir}/man3/Pod::Simple*.3pm*
