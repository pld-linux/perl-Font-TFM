%include	/usr/lib/rpm/macros.perl
Summary:	Font-TFM perl module
Summary(pl):	Modu³ perla Font-TFM
Name:		perl-Font-TFM
Version:	0.100
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Font/Font-TFM-%{version}.tar.gz
Patch0:		%{name}-fontsdir.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font-TFM - read and work with TeX font metric files.

%description -l pl
Font-TFM umo¿liwia pracê na plikach metryk fontów TeXa.

%prep
%setup -q -n Font-TFM-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Font/TFM.pm
%{_mandir}/man3/*
