%include	/usr/lib/rpm/macros.perl
%define		pdir	Font
%define		pnam	TFM
Summary:	Font::TFM Perl module
Summary(cs):	Modul Font::TFM pro Perl
Summary(da):	Perlmodul Font::TFM
Summary(de):	Font::TFM Perl Modul
Summary(es):	Módulo de Perl Font::TFM
Summary(fr):	Module Perl Font::TFM
Summary(it):	Modulo di Perl Font::TFM
Summary(ja):	Font::TFM Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Font::TFM ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Font::TFM
Summary(pl):	Modu³ Perla Font::TFM
Summary(pt):	Módulo de Perl Font::TFM
Summary(pt_BR):	Módulo Perl Font::TFM
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Font::TFM
Summary(sv):	Font::TFM Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Font::TFM
Summary(zh_CN):	Font::TFM Perl Ä£¿é
Name:		perl-Font-TFM
Version:	0.130
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3ae79cc6321df135e14ea50227543415
Patch0:		%{name}-fontpath.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font::TFM - read and work with TeX font metric files.

%description -l pl
Font::TFM umo¿liwia pracê na plikach metryk fontów TeXa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Font/TFM.pm
%{_mandir}/man3/*
