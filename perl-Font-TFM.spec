%include	/usr/lib/rpm/macros.perl
Summary:	Font-TFM perl module
Summary(pl):	Modu³ perla Font-TFM
Name:		perl-Font-TFM
Version:	0.073
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Font/Font-TFM-%{version}.tar.gz
Patch:		perl-Font-TFM-fontsdir.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Font/TFM
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Font/TFM.pm
%{perl_sitearch}/auto/Font/TFM

%{_mandir}/man3/*
