#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Graphics
%define		pnam	ColorNames
Summary:	Defines RGB values for common color names
Summary(pl.UTF-8):	Wartości RGB dla popularnych nazw kolorów
Name:		perl-Graphics-ColorNames
Version:	2.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graphics/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	047eabbb48d7c29cfebac6f9da8478f6
URL:		http://search.cpan.org/dist/Graphics-ColorNames/
BuildRequires:	perl-Module-Load
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Defines RGB values for common color names.

%description -l pl.UTF-8
Wartości RGB dla popularnych nazw kolorów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Graphics/*.pm
%dir %{perl_vendorlib}/Graphics/ColorNames
%{perl_vendorlib}/Graphics/ColorNames/*.pm
%{_mandir}/man3/*
