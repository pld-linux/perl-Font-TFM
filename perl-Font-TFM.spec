%include	/usr/lib/rpm/macros.perl
%define	pdir	Font
%define	pnam	TFM
Summary:	Font-TFM perl module
Summary(pl):	Modu� perla Font-TFM
Name:		perl-Font-TFM
Version:	0.110
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fontsdir.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font-TFM - read and work with TeX font metric files.

%description -l pl
Font-TFM umo�liwia prac� na plikach metryk font�w TeXa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
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
