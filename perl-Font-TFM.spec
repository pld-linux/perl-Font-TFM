#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Font
%define		pnam	TFM
Summary:	Font::TFM - read information from TeX font metric files
Summary(pl.UTF-8):	Font::TFM - odczyt informacji z plików metryk fontów TeX-a
Name:		perl-Font-TFM
Version:	0.130
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3ae79cc6321df135e14ea50227543415
Patch0:		%{name}-fontpath.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::TFM Perl module is for reading and working with TeX font metric
files.

%description -l pl.UTF-8
Moduł Perla Font::TFM umożliwia pracę na plikach metryk fontów TeXa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL </dev/null \
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
%doc Changes README
%{perl_vendorlib}/Font/TFM.pm
%{_mandir}/man3/*
