%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	TFM
Summary:	Font::TFM perl module
Summary(pl):	Modu³ perla Font::TFM
Name:		perl-Font-TFM
Version:	0.130
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::TFM - read and work with TeX font metric files.

%description -l pl
Font::TFM umo¿liwia pracê na plikach metryk fontów TeXa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Font/TFM.pm
%{_mandir}/man3/*
